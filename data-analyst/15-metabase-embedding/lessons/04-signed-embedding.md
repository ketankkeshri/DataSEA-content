# Signed Embedding

Securing your embedded analytics is crucial, especially when sharing sensitive data with stakeholders. Signed embedding in Metabase allows you to securely embed dashboards and reports while ensuring that only authorized users can access them.

## What is Signed Embedding?

Signed embedding involves generating a unique signature for your embedded dashboards, which verifies the authenticity of the request. This helps prevent unauthorized access and ensures that the data displayed is tailored to the user’s permissions. By using signed URLs, you can control who sees what, enhancing both security and user experience.

### How to Implement Signed Embedding

To implement signed embedding in Metabase, you need to follow these steps:

1. **Generate a Secret Key**: This key is used to sign your embedded URLs. Store it securely.
2. **Create an Embedding URL**: Construct a URL for your dashboard.
3. **Sign the URL**: Use your secret key to sign the URL, ensuring that the dashboard can only be accessed by those with the correct permissions.

Here’s an example to illustrate the process:

```python
import hashlib
import hmac
import base64
import json
from urllib.parse import urlencode

# Configuration
secret_key = b'your_secret_key'
base_url = 'https://your-metabase-instance.com/embed/dashboard'
dashboard_id = 1
user_email = 'user@example.com'

# Create the payload
payload = {
    'resource': {
        'dashboard': dashboard_id,
    },
    'params': {
        'user_email': user_email,
    },
    'exp': int(time.time()) + 3600,  # 1 hour expiration
}

# Generate the signature
signature = base64.urlsafe_b64encode(
    hmac.new(secret_key, json.dumps(payload).encode(), hashlib.sha256).digest()
).decode()

# Create the signed URL
signed_url = f"{base_url}/{dashboard_id}#embed/dashboard/{dashboard_id}?signature={signature}&{urlencode(payload)}"

print(signed_url)
```

### Understanding the Code

- **Secret Key**: Always keep this private. It's the backbone of your security.
- **Payload**: Contains the dashboard ID, user parameters, and expiration time. Adjust the expiration as necessary for your use case.
- **Signature**: It's generated using HMAC with SHA-256 to ensure it's tamper-proof.
- **Signed URL**: This URL can now be embedded in your applications or websites.

## Common pitfalls

- **Exposed Secret Key**: Never hard-code your secret key in the client-side code. Use environment variables or secure vault services.
- **Expired URLs**: Make sure to set an appropriate expiration time. Too short, and users may encounter errors; too long, and security is compromised.
- **Lack of User-Specific Data**: Always tailor the data presented in the embedded dashboard to the user. Failing to do so can lead to data leaks.

## In a nutshell

- Signed embedding enhances security for embedded dashboards.
- Generate a unique signature using a secret key.
- Create a signed URL that includes user-specific parameters.
- Watch out for common pitfalls like exposed keys and expired URLs.
- Tailor embedded data to ensure users only see what they should.