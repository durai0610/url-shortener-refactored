# CHANGES.md

## Summary of Implementation - URL Shortener (Task 2)

### What Was Implemented
- URL Shortener (`POST /api/shorten`)
- Redirection logic (`GET /<short_code>`)
- Analytics endpoint (`GET /api/stats/<short_code>`)
- In-memory data store using Python dictionary
- Thread-safe access using `threading.Lock()`
- URL validation using regex
- Random short code generation
- 5+ test cases using Pytest

### AI Usage
- ChatGPT used for guidance on Flask routing, thread-safe design, and testing.
- All code was written manually and tested.

