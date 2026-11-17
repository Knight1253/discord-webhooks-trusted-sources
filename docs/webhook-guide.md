# Discord webhook guide

This guide gives a practical map of Discord webhook workflows. It is not an exhaustive API specification; the official Webhook Resource and API reference are authoritative and can change.

## 1. Understand webhook types

Discord's API models multiple webhook types, including incoming webhooks, channel-following webhooks, and application webhooks. They do not all have the same lifecycle or purpose. The Python example in this repository is for executing an incoming webhook URL. Application interaction callbacks and Discord-to-application event delivery have distinct protocols; consult the official docs before implementing them.

## 2. Create and manage an incoming webhook

A webhook can be created for a channel using Discord's client, or through the API. API creation and management require authorization and the relevant permissions (typically `MANAGE_WEBHOOKS`). Do not put a bot token in a client app or public repository.

The official Webhook Resource documents these endpoint families:

- Create a channel webhook: `POST /channels/{channel.id}/webhooks`
- List channel webhooks: `GET /channels/{channel.id}/webhooks`
- Get or modify a webhook: `GET` / `PATCH /webhooks/{webhook.id}`
- Delete a webhook: `DELETE /webhooks/{webhook.id}`
- Token-authenticated variants are available for some operations when the webhook ID and token are known.

Use the official endpoint documentation for authorization requirements, request bodies, and response schemas. A webhook token is a bearer secret: possession can grant the ability to act as that webhook.

## 3. Execute a webhook

An incoming webhook is executed with an HTTP `POST` to its URL, typically shaped like:

`https://discord.com/api/webhooks/{webhook.id}/{webhook.token}`

Execution uses the webhook token in the URL; it does not use a bot token. Keep the complete URL secret. Depending on the payload and endpoint options, a message can contain content, embeds, components, or uploaded files. Respect Discord's documented payload limits and allowed mention behavior.

For a simple JSON message:

```bash
curl --fail-with-body \
  -H 'Content-Type: application/json' \
  -d '{"content":"Hello from a webhook","allowed_mentions":{"parse":[]}}' \
  'https://discord.com/api/webhooks/ID/TOKEN?wait=true'
```

Replace the URL with a secret supplied at runtime; do not save a real token in this document. `wait=true` requests the created message response. For the standard no-wait response, Discord may return HTTP 204 with no body.

The example script in `examples/webhook_sender.py` supports JSON payloads, a `thread_id`, and `wait=true`:

```bash
export WEBHOOK_URL='https://discord.com/api/webhooks/ID/TOKEN'
python examples/webhook_sender.py --content 'Build completed' --wait
python examples/webhook_sender.py --payload-file payload.json --thread-id THREAD_ID
```

## 4. Threads, messages, and files

- To post to a thread, use the execution options documented by Discord, such as `thread_id` where applicable. Some forum/media channel workflows may require a thread name or have other constraints.
- Webhook-authored messages can be fetched, edited, or deleted using the webhook message routes documented in the Webhook Resource. Preserve the message ID returned when executing with `wait=true` if later operations need it.
- File uploads use multipart form data and Discord's attachment conventions; they are not the same as a JSON-only request. Consult the current upload and message-payload documentation for multipart field names, attachment metadata, and limits.
- Mention parsing can notify users or roles. Set `allowed_mentions` explicitly when content may contain untrusted text; an empty parse list disables broad automatic parsing.

Do not assume every message feature works with every webhook type, channel type, or endpoint. Check the current reference for constraints.

## 5. Authentication and incoming events

Distinguish these directions of traffic:

- **Your service → Discord:** incoming webhook execution uses the webhook URL/token.
- **Your service → Discord management endpoints:** use an authorized application/bot credential with only the permissions needed; never expose it in browser code.
- **Discord → your service:** application interactions or configured webhook events have their own request verification and response requirements. Verify signed requests as documented before trusting or processing them; do not confuse this with incoming webhook execution.

## 6. Rate limits and reliability

Discord returns rate-limit information and may return HTTP 429. Use the response's documented retry timing and rate-limit headers; do not repeatedly retry immediately or assume a fixed universal limit. Apply bounded retries, timeouts, and backoff in production, and avoid sending duplicate messages when retrying an ambiguous network failure. Treat other HTTP errors as failures and inspect Discord's response without logging credentials.

The included example makes a single request and reports errors. It does not automatically retry, avoiding accidental duplicate sends.

## 7. Security checklist

- Store webhook URLs and bot credentials in a secret manager or protected environment variables.
- Never commit secrets, paste them into logs, or expose them to client-side code.
- Rotate/recreate a webhook immediately if its URL is disclosed.
- Restrict who can create/manage webhooks in the server and channel.
- Validate and constrain message data; avoid allowing untrusted users to control mentions, embeds, or destinations.
- Use explicit `allowed_mentions` for untrusted content.
- Use HTTPS and verify Discord-originated signatures for inbound event requests.
- Keep dependencies and examples small; review changes before running them.

## Official references

See [`trusted-sources.md`](trusted-sources.md) for official documentation, API changelog sources, and source-evaluation guidance.
