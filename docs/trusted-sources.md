# Trusted sources for Discord information

Use official and maintainers-backed sources when validating Discord behavior, webhook rules, permissions, rate limits, or API changes.

## Primary official sources

1. Discord Developer Documentation
   - https://discord.com/developers/docs/intro
   - Main documentation for APIs, Webhooks, gateways, and bot integrations.

2. Discord Webhook Documentation
   - https://discord.com/developers/docs/resources/webhook
   - Canonical documentation for webhook endpoints, payloads, and behavior.

3. Discord API Reference
   - https://discord.com/developers/docs/reference
   - Reference material for Discord API request and response details.

4. Discord Status Page
   - https://discordstatus.com/
   - For service availability and incidents.

5. Discord Help Center
   - https://support.discord.com/hc/en-us
   - For platform policies, account settings, and user-facing product behavior.

6. Discord Developer Blog / changelog-related updates
   - https://discord.com/developers/blog
   - Useful for product announcements and API-related updates.

## GitHub-based official references

- Discord API docs repo: https://github.com/discord/discord-api-docs
- This repo is commonly used by community and Discord developers to track API documentation updates and changes.

## Trusted-source checklist

When you are evaluating a webhook pattern or Discord API claim, prefer information that is:

- published by Discord directly
- in the official developer docs or support docs
- backed by Discord’s GitHub API docs repo
- consistent across official documentation and SDK examples

Treat community posts as secondary references unless they match official documentation or are confirmed by Discord-maintained sources.

## Practical guidance

- For webhook payloads, confirm the exact JSON schema in the current docs.
- For permission limitations, verify them in the relevant Discord documentation.
- For rate limiting, use official docs and account/application-level limits.
- For outages or platform issues, use Discord Status.

## Example of a good source hierarchy

1. Discord Developer Docs
2. Discord API docs repo
3. Discord support articles
4. reputable developer community discussions
5. unofficial blog posts or third-party articles

## Warning

Discord changes platform behavior and APIs over time. A claim from an older article or community post may be outdated or incorrect if it is not validated against the latest official docs.
