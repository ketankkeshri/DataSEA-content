# Http Basics

Understanding HTTP is crucial for data engineers as it forms the backbone of REST APIs, which are essential for integrating and communicating with web services. Knowing how HTTP works can help you troubleshoot issues, optimize data flows, and design better data pipelines.

## What is HTTP?

HTTP, or Hypertext Transfer Protocol, is the protocol used for transferring data on the web. It defines how messages are formatted and transmitted, as well as how servers and browsers should respond to various commands. 

### Key HTTP Methods

The core HTTP methods you'll encounter are:

- **GET**: Retrieve data from a server. It's read-only and should not change server state.
- **POST**: Send data to a server to create a resource. This often modifies data on the server.
- **PUT**: Update an existing resource or create a new one if it doesn't exist.
- **DELETE**: Remove a resource from the server.

### Status Codes

HTTP responses come with status codes that indicate the result of a request:

- **200 OK**: The request was successful.
- **201 Created**: A new resource has been created successfully.
- **400 Bad Request**: The server could not understand the request due to invalid syntax.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: A generic error message when the server fails to fulfill a request.

## Making a Simple HTTP Request

You can use Python's `requests` library to make HTTP requests easily. Here’s a basic example to fetch data from a public API:

```python
import requests

response = requests.get('https://api.example.com/data')

if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")
```

In this example, replace `'https://api.example.com/data'` with a real API endpoint. The `requests.get` method sends a GET request, and we check the status code to see if it was successful.

## Common pitfalls

- **Ignoring status codes**: Not checking the response status can lead to silent failures. Always validate the response.
- **Using incorrect HTTP methods**: Using the wrong method (like POST instead of GET) can lead to unexpected behavior and errors.
- **Not handling exceptions**: Network issues can occur. Always wrap your requests in try-except blocks to handle exceptions gracefully.

## In a nutshell

- HTTP is the foundation of data communication on the web.
- Key methods include GET, POST, PUT, and DELETE.
- Status codes provide insight into request outcomes.
- Use the `requests` library for straightforward HTTP requests.
- Always check responses and handle exceptions to avoid pitfalls.