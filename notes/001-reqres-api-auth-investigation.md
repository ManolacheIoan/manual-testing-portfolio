# Investigation: ReqRes.in API Authentication Behavior

## Context
While testing Bearer Token auth against `/api/users/2`, discovered ReqRes.in 
has migrated `/api/*` endpoints to require `x-api-key` instead of Bearer tokens.
Bearer tokens remain valid only for `/app/*` endpoints (scoped user data access).

## Findings

| Scenario | Status Code | Error |
|---|---|---|
| Bearer token sent to `/api/*` | 401 | `missing_api_key` |
| No auth header at all | 401 | `missing_api_key` |
| `x-api-key` header present, invalid value | 403 | `invalid_api_key` |

## Key Takeaway
Distinguishes correctly between:
- **401 Unauthorized**: no valid authentication provided at all
- **403 Forbidden**: authentication provided, but rejected/insufficient

This is a well-designed API error response — includes `hint`, `next_steps`, 
and `example_curl` fields, making it easy to self-diagnose auth issues 
without external documentation.

## Tools
See `postman-collections/reqres-demo-collection.json` for the request 
collection used (login, chained Bearer Token, x-api-key variants).