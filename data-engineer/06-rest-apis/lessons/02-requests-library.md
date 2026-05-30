# Requests Library

Interacting with REST APIs is a core skill for data engineers, enabling you to pull in data from various sources, automate tasks, and facilitate data workflows. The `requests` library in Python simplifies this process, making it easier to send HTTP requests and handle responses. 

## Getting Started with Requests

To begin, you need to install the `requests` library if you haven't already. You can do this using pip:

```bash
pip install requests
```

Once installed, using `requests` is straightforward. Here’s how to make a simple GET request to fetch data from a public API:

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

print(data)
```

In this example, we’re accessing a mock API that returns a list of posts. The `get` method sends an HTTP GET request, and the response is parsed into JSON format using the `.json()` method.

## Making POST Requests

Often, you’ll need to send data to an API. This is done using POST requests. Here’s how you can do that:

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=payload)
data = response.json()

print(data)
```

In this case, we’re sending a JSON payload to create a new post. The `json` parameter automatically sets the `Content-Type` header to `application/json`, which many APIs expect.

## Handling Responses and Errors

When dealing with APIs, it's crucial to handle responses and potential errors. The `requests` library makes this easy with built-in features:

```python
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.reason}")
```

Here, we check the status code of the response. A 200 status code means success, while any other code might indicate an error. Always implement error handling to avoid unexpected crashes in your data pipelines.

## Common pitfalls

- **Ignoring response status codes:** Always check `response.status_code` before processing data to handle errors gracefully.
- **Not setting timeouts:** Network requests can hang indefinitely. Use the `timeout` parameter in your requests to avoid blocking your application.
  
  ```python
  response = requests.get(url, timeout=5)  # 5 seconds timeout
  ```

- **Sending incorrect content types:** Ensure you’re sending data in the format the API expects (e.g., JSON vs. form data).

## In a nutshell

- Use `requests` for easy HTTP requests in Python.
- GET requests retrieve data, while POST requests send data to APIs.
- Always handle errors and check response status codes.
- Set timeouts for your requests to prevent hanging.
- Ensure you send data in the correct format for the API.