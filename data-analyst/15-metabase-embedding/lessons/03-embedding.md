# Embedding

Embedding data visualizations into applications can significantly enhance user experience and engagement. This lesson dives into how to effectively embed Metabase reports and dashboards within your web applications, allowing data analysts to provide insights seamlessly.

## Understanding Embedding in Metabase

Embedding allows you to integrate Metabase's powerful visualization capabilities directly into your applications. This is especially useful for product teams that want to provide real-time data insights without requiring users to navigate away from their primary interface. 

To get started, you'll first need to create a Metabase dashboard or report. Once you have that, you can generate an embed code that can be placed within your application. Here’s how you typically do it:

1. **Create a Dashboard/Report**: Use Metabase to create a dashboard that contains the visualizations you want to embed.
2. **Generate Embed Code**: Navigate to the sharing options of your dashboard and select “Embed this dashboard.”
3. **Use the Embed Link**: This will provide you with an HTML iframe code to use in your application.

Here's a basic example of what the generated embed code might look like:

```html
<iframe
    src="https://your-metabase-instance.com/embed/dashboard/1?embed=true"
    frameborder="0"
    width="800"
    height="600"
></iframe>
```

## Implementing Secure Embedding

While embedding is powerful, it’s crucial to secure your embedded content to prevent unauthorized access to your data. Metabase provides a feature called signed embedding, which generates a secure link that includes a signature to verify that the request is legitimate. 

You can implement signed embedding by following these steps:

1. **Enable Signed Embedding**: In the Metabase admin settings, enable the signed embedding option.
2. **Set Up a Secret Key**: Define a secret key in your application that Metabase will use to generate the signature.
3. **Generate Signed URL**: When generating the URL for your iframe, append a query parameter that includes the signature.

Here’s a Python example to generate a signed URL:

```python
import hmac
import hashlib
import base64
import time

def generate_signed_url(dashboard_id, secret_key):
    base_url = f"https://your-metabase-instance.com/embed/dashboard/{dashboard_id}?embed=true"
    timestamp = int(time.time())
    signature = base64.urlsafe_b64encode(
        hmac.new(secret_key.encode(), f"{base_url}{timestamp}".encode(), hashlib.sha256).digest()
    ).decode()
    
    return f"{base_url}&timestamp={timestamp}&sig={signature}"

# Usage
dashboard_id = 1
secret_key = 'your_secret_key_here'
signed_url = generate_signed_url(dashboard_id, secret_key)
print(signed_url)
```

## Common pitfalls

- **Ignoring Security**: Not using signed embedding can expose your data to unauthorized users.
- **Iframe Size Issues**: Make sure your iframe dimensions are optimal for user experience; poorly sized iframes can lead to a frustrating experience.
- **Cross-Origin Resource Sharing (CORS)**: Ensure that your Metabase instance allows CORS requests from your application domain to avoid loading issues.

## In a nutshell

- Embed Metabase dashboards to enhance user engagement with data insights.
- Use secure signed embedding to protect your data from unauthorized access.
- Test your iframe dimensions for optimal presentation.
- Manage CORS settings to ensure seamless integration.