# Discord Webhooks & Trusted Sources

A practical, security-first reference for Discord webhooks: how to create and manage them, send and maintain messages, work with threads and files, understand authentication and rate limits, and find authoritative documentation.

> This is an independent community resource, not affiliated with or endorsed by Discord. Discord's API evolves; verify current behavior in Discord's official docs before deploying.

## What this repo covers

- Incoming webhooks and application/webhook event concepts
- Creating, listing, fetching, modifying, and deleting webhooks
- Executing webhooks, message edits/deletes, threads, and payload basics
- Secure token handling, request validation, and rate-limit behavior
- A single-message Python CLI example using only the standard library
- Official references and guidance for evaluating secondary sources

Start with [`docs/webhook-guide.md`](docs/webhook-guide.md), then check [`docs/trusted-sources.md`](docs/trusted-sources.md).

## Quick start

Python 3.9+; no third-party packages are required.

```bash
export WEBHOOK_URL='https://discord.com/api/webhooks/ID/TOKEN'
python examples/webhook_sender.py --content 'Hello from my service'
```

You can also submit a JSON payload file:

```bash
python examples/webhook_sender.py --payload-file payload.json --thread-id THREAD_ID
```

The webhook URL is a secret. Do not put a real URL in source code, command history, screenshots, logs, or issue reports. Use a secret manager in production. If a webhook URL leaks, delete or regenerate that webhook in Discord and update your secret store.

## Example scope and production considerations

The example sends one JSON message per invocation. It intentionally does not create webhooks, accept arbitrary URLs, or implement bulk sending. It is a small reference, not a complete SDK or a substitute for application-level monitoring, secret management, input validation, and rate-limit handling.

For files, interaction webhooks, event signatures, OAuth, or full endpoint details, follow the official references in the guide. Never use a webhook to send unsolicited, deceptive, abusive, or high-volume messages.

## Contributing

Keep examples minimal and safe by default. Link claims to current official Discord documentation, never include live webhook credentials, and clearly label any community-maintained material. See [`CONTRIBUTING.md`](CONTRIBUTING.md).
