```markdown
# Metabase & Embedding — Cheatsheet

## [Core concepts]

| Thing               | Syntax                         | Notes                                   |
|---------------------|--------------------------------|-----------------------------------------|
| Create a dashboard   | `POST /api/dashboard`          | Requires `name` and `source` fields.   |
| Add a chart         | `POST /api/chart`             | Use `dashboard_id` to link it.          |
| Embed a dashboard    | `https://yourmetabase.com/embed/dashboard/:id` | Ensure proper permissions are set.     |
| Signed embedding     | `https://yourmetabase.com/embed/dashboard/:id?sig=...` | Use JWT for security.                  |

## [Common operations]

```python
# Create a dashboard
import requests
import json

url = "https://yourmetabase.com/api/dashboard"
headers = {
    "Content-Type": "application/json",
    "X-Metabase-Session": "your_session_token"
}
data = {
    "name": "My Dashboard",
    "description": "This is my dashboard",
    "collection_id": 1
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())

# Embed a chart
embed_url = "https://yourmetabase.com/embed/chart/:id"
print(f"Embed this chart: {embed_url}")
```

## [Gotchas]

- ⚠️ Ensure your Metabase instance is configured for embedding; check settings in the admin panel.
- ⚠️ Signed embedding requires generating a secure JWT; don't expose your secret key in client-side code.

## [Mental model]

- **Dashboards** contain **charts**.
- **Embedding** allows integration into external apps.
- **Signed embedding** secures access to sensitive data.
```