```markdown
# REST APIs for DEs (06-rest-apis) — Cheatsheet

## [Section 1: HTTP Basics]

| Thing             | Syntax                      | Notes                                           |
|-------------------|-----------------------------|-------------------------------------------------|
| GET Request       | `requests.get(url)`        | Fetches data from a specified resource.        |
| POST Request      | `requests.post(url, data)` | Sends data to a server to create/update a resource. |
| PUT Request       | `requests.put(url, data)`  | Updates a resource at the specified URL.       |
| DELETE Request    | `requests.delete(url)`     | Deletes the specified resource.                 |
| Status Codes      | `response.status_code`     | Check response status (e.g., 200, 404, 500).  |

## [Section 2: Using the Requests Library]

```python
import requests

# Example GET request
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()  # Parse JSON response
```

## [Pagination and Retries]

| Thing             | Syntax                               | Notes                                                      |
|-------------------|--------------------------------------|------------------------------------------------------------|
| Pagination        | `params={'page': page_number}`      | Use query parameters to request specific pages.            |
| Retry Logic       | `retry_count = 5`                   | Retry the request if it fails (e.g., due to rate limits). |

```python
import requests
from time import sleep

url = 'https://api.example.com/data'
retry_count = 5

for attempt in range(retry_count):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        break
    sleep(2)  # Wait before retrying
```

## [Rate Limiting]

| Thing             | Syntax                               | Notes                                                      |
|-------------------|--------------------------------------|------------------------------------------------------------|
| Limit Requests     | `time.sleep(seconds)`                | Pause between requests to avoid hitting rate limits.       |

```python
import time

for i in range(10):
    response = requests.get('https://api.example.com/data')
    time.sleep(1)  # Sleep 1 second between requests
```

## [OAuth Authentication]

| Thing             | Syntax                               | Notes                                                      |
|-------------------|--------------------------------------|------------------------------------------------------------|
| OAuth Flow        | Use OAuth libraries (e.g., `requests-oauthlib`) | Handle auth token exchange to access protected resources.  |

```python
from requests_oauthlib import OAuth1

auth = OAuth1('client_key', 'client_secret', 'resource_owner_key', 'resource_owner_secret')
response = requests.get('https://api.example.com/protected', auth=auth)
```

## [Gotchas]

- ⚠️ Ensure you handle different HTTP status codes appropriately.
- ⚠️ Be aware of API rate limits to avoid 429 errors (Too Many Requests).
- ⚠️ Review the API documentation for authentication requirements.

## [Mental model]

1. **HTTP Methods**: Use GET for reading, POST for creating, PUT for updating, DELETE for removing resources.
2. **Error Handling**: Always check response status codes and implement retry logic for robustness.
3. **Authentication**: Use OAuth for secure access to protected API endpoints.
```