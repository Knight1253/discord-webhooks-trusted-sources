# Trusted sources for Discord information

Use Discord-maintained sources first when checking webhook behavior, permissions, request schemas, rate limits, and API changes. This repository is an independent reference, not official Discord documentation.

## Official documentation

- [Discord Developer Documentation](https://docs.discord.com/developers/docs/intro) — overview of Discord's developer platform.
- [Webhook Resource](https://docs.discord.com/developers/resources/webhook) — webhook types, routes, payloads, and message operations.
- [Webhooks on the platform](https://docs.discord.com/developers/platform/webhooks) — webhook concepts and platform guidance.
- [API Reference](https://docs.discord.com/developers/reference) — API conventions and reference details.
- [Rate Limits](https://docs.discord.com/developers/topics/rate-limits) — rate-limit response and handling guidance.
- [Receiving an Event](https://docs.discord.com/developers/events/webhook-events) — event delivery and request validation, where applicable.
- [Discord Developer Portal](https://discord.com/developers/applications) — manage applications and related settings.
- [Discord Status](https://discordstatus.com/) — service incidents and availability.
- [Discord Support](https://support.discord.com/hc/en-us) — user-facing product help and policies.
- [Discord Developer Blog](https://discord.com/developers/blog) — official announcements.

## Official documentation source repository

- [discord/discord-api-docs](https://github.com/discord/discord-api-docs) — Discord-maintained API documentation source and issue tracking. Verify that a repository or account is genuinely maintained by Discord before treating it as official.

## Evaluating other sources

When a claim matters, check:

1. Is it directly stated in current Discord documentation or an announcement?
2. Does it apply to the webhook type and endpoint in question?
3. Is the information current, and does it agree with the documented schema and permission model?
4. Is a third-party library's behavior merely a library choice rather than a Discord API guarantee?

Community discussions and SDK docs can be useful for examples and troubleshooting, but treat them as secondary. Do not rely on outdated snippets for token handling, rate limits, permissions, or payload constraints.

## Reporting a documentation correction

Open an issue with the claim and link to the relevant official source. Do not include webhook URLs, tokens, private messages, or other credentials in issues.
