# API Authentication Concepts

Practical notes on Bearer Token authentication and status code
semantics, worked through during QA training.

## Bearer Token — what it actually is

A Bearer Token is a string issued by the server after a successful
login (email + password), which is then sent on every subsequent
request in the `Authorization` header — instead of resending
credentials each time.

Flow:
1. `POST /login` with `{"email": "...", "password": "..."}`
2. Server responds: `{"token": "abc123..."}`
3. Every following request includes: `Authorization: Bearer abc123...`

The token proves "I already authenticated" without repeating the
full login process on every call.

## Token expiration

Tokens are not permanent. Expiration is a design decision made by
the backend team, based on the sensitivity of the data — banking
APIs may expire tokens in minutes; low-risk APIs may allow days.

Two ways to get a new token after expiration:
1. Log in again manually (re-send email + password)
2. Refresh token flow: a longer-lived `refresh_token`, issued
   alongside the main token, is used automatically in the
   background to obtain a new token without re-entering credentials

## 401 vs 403 — the distinction that matters

| Status | Meaning | Example |
|---|---|---|
| 401 Unauthorized | No valid authentication provided at all | No `x-api-key` header sent |
| 403 Forbidden | Authentication provided, but rejected/invalid | `x-api-key: invalid-value` sent |

Simple way to remember: **401 = "you didn't show up"**,
**403 = "you showed up, but you're not allowed in."**

## API Key vs Bearer Token

- **API Key** — identifies an application/service
- **Bearer Token** — identifies an authenticated user

Some APIs require different auth methods for different endpoint
categories (e.g. `/api/*` requiring `x-api-key` for admin-style
operations, `/app/*` accepting Bearer Token for scoped user access).
