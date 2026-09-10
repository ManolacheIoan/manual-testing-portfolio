# [BUG] /cms/notifications endpoint returns 404 instead of 200/204 for empty state

## Environment
- Site: altex.ro
- Browser: Chrome 152.0.7977.83
- Date: 2026-09-10

## Steps to Reproduce
1. Navigate to altex.ro homepage
2. Open DevTools > Network tab, filter XHR/Fetch
3. Observe request to GET /cms/notifications/?type=homepage

## Actual Result
Response status: 404 Not Found

## Expected Result
When there is no active homepage notification/banner, the API should return 200 OK with an empty body/array, or 204 No Content — not 404, which technically implies the requested resource itself doesn't exist.

## Severity
Low / Minor — no visible impact on user experience, but incorrect use of HTTP semantics could cause issues for API consumers relying on status codes for error handling.

## Evidence
See screenshots/001-notifications-headers.png