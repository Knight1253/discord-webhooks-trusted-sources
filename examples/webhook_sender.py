import json
import os
import sys

import requests


def send_webhook_message():
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        print("WEBHOOK_URL is not set.")
        print("Example: export WEBHOOK_URL='https://discord.com/api/webhooks/...' ")
        sys.exit(1)

    payload = {
        "username": "Webhook Bot",
        "avatar_url": "https://cdn.discordapp.com/embed/avatars/0.png",
        "content": "Hello from the Discord webhook example in this repo!",
        "embeds": [
            {
                "title": "Status",
                "description": "This message was posted using a webhook from a local example script.",
                "color": 5814783,
            }
        ],
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

    if response.status_code in (200, 204):
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code} {response.text}")
        sys.exit(1)


if __name__ == "__main__":
    send_webhook_message()
