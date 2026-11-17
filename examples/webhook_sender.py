#!/usr/bin/env python3
"""Send one JSON message through a Discord incoming webhook.

The webhook URL is a credential. Supply it through WEBHOOK_URL and never log
or commit it. This small example does not automatically retry requests.
"""

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen


def webhook_url_from_env():
    url = os.environ.get("WEBHOOK_URL", "")
    parts = urlsplit(url)
    path_parts = parts.path.strip("/").split("/")
    if (
        parts.scheme != "https"
        or parts.hostname != "discord.com"
        or parts.username is not None
        or parts.password is not None
        or parts.port is not None
        or len(path_parts) != 4
        or path_parts[0] != "api"
        or path_parts[1] != "webhooks"
        or not path_parts[2]
        or not path_parts[3]
    ):
        raise ValueError(
            "Set WEBHOOK_URL to an HTTPS Discord incoming webhook URL "
            "(https://discord.com/api/webhooks/ID/TOKEN)."
        )
    return url


def add_query_options(url, thread_id, wait):
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    if thread_id:
        query["thread_id"] = thread_id
    if wait:
        query["wait"] = "true"
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def load_payload(args):
    if args.payload_file:
        with open(args.payload_file, "r", encoding="utf-8") as payload_file:
            payload = json.load(payload_file)
        if not isinstance(payload, dict):
            raise ValueError("The payload JSON must be an object.")
    else:
        payload = {
            "content": args.content,
            "allowed_mentions": {"parse": []},
        }

    if args.username:
        payload["username"] = args.username
    if args.avatar_url:
        payload["avatar_url"] = args.avatar_url
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--content", help="Text for a single message")
    group.add_argument("--payload-file", help="Path to a JSON object payload")
    parser.add_argument("--username", help="Custom display name for this message")
    parser.add_argument("--avatar-url", help="Custom avatar image URL for this message")
    parser.add_argument("--thread-id", help="Post to an existing thread, when supported")
    parser.add_argument("--wait", action="store_true", help="Ask Discord to return the created message")
    parser.add_argument("--timeout", type=float, default=15.0, help="HTTP timeout in seconds (default: 15)")
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")

    try:
        url = add_query_options(webhook_url_from_env(), args.thread_id, args.wait)
        payload = load_payload(args)
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request = Request(
            url,
            data=body,
            headers={"Content-Type": "application/json", "User-Agent": "discord-webhook-reference/1.0"},
            method="POST",
        )
        with urlopen(request, timeout=args.timeout) as response:
            response_body = response.read()
            if response_body:
                print(response_body.decode("utf-8", errors="replace"))
            else:
                print(f"Message sent (HTTP {response.status}).")
        return 0
    except HTTPError as error:
        # Do not print the request URL: it contains the webhook token.
        detail = error.read().decode("utf-8", errors="replace")
        print(f"Discord returned HTTP {error.code}: {detail}", file=sys.stderr)
        if error.code == 429:
            print("Respect Discord's retry timing; this example does not retry automatically.", file=sys.stderr)
        return 1
    except (URLError, TimeoutError) as error:
        print(f"Request failed: {error}", file=sys.stderr)
        return 1
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Input/configuration error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
