# Dashboards

Dashboards are the heartbeat of data visualization, allowing data analysts to present insights in a visually compelling way. Mastering dashboards in Metabase can elevate your analytics game, making it easy to share key metrics and insights with stakeholders.

## Building Your First Dashboard

Creating a dashboard in Metabase is straightforward. Start by gathering the key metrics you want to show. For example, let’s assume you have an `orders` table with the following fields: 

- `order_id`
- `customer_id`
- `order_date`
- `total_amount`
- `status`

Here’s how to create a simple dashboard that displays total sales and the number of orders.

1. **Create Questions**: First, create the questions that will populate your dashboard.

```sql
-- Total Sales
SELECT 
    SUM(total_amount) AS total_sales 
FROM 
    orders
WHERE 
    status = 'completed';

-- Total Orders
SELECT 
    COUNT(order_id) AS total_orders 
FROM 
    orders
WHERE 
    status = 'completed';
```

2. **Add Questions to Dashboard**: Once you have your questions, navigate to the dashboard section and click on “New Dashboard.” Name your dashboard, then use the “Add a Question” button to insert your previously created questions.

3. **Customize Visualization**: Metabase offers various visualization options. For total sales, a line chart might be ideal, while a number display can work for total orders. Select your desired visualization from the options available and adjust the settings to match your preferences.

## Sharing and Embedding Dashboards

Once your dashboard is ready, sharing it with your team or embedding it in another application is a breeze. Metabase provides a few options for this.

1. **Sharing Links**: You can share a public link to your dashboard. Just click on the “Sharing” button and copy the link. This link will show the latest data and is perfect for stakeholders who need real-time insights.

2. **Embedding**: For a more integrated approach, you can embed the dashboard in your web application. This requires setting up signed embedding for added security. Here’s a quick overview of how to do that:

```javascript
// Example of embedding dashboard with signed URL
const embedUrl = "https://your-metabase-instance.com/embed/dashboard/1";
const signedUrl = `${embedUrl}?embed_token=YOUR_GENERATED_TOKEN`;

// Use the signedUrl in an iframe
<iframe src={signedUrl} width="800" height="600"></iframe>
```

Make sure to replace `YOUR_GENERATED_TOKEN` with an actual token generated from your Metabase instance.

## Common pitfalls

- **Overloading with Metrics**: Avoid cramming too many visualizations into one dashboard. It can overwhelm users. Stick to the most critical metrics.
- **Ignoring User Roles**: Ensure that the right stakeholders have access to the dashboard. Use Metabase’s permissions to restrict access based on user roles.
- **Not Updating Data Sources**: Remember to keep your data sources updated. A dashboard loses value if it’s displaying stale data.

## In a nutshell

- Dashboards are essential for visualizing key metrics.
- Create impactful questions to populate your dashboard.
- Utilize sharing and embedding features for wider accessibility.
- Avoid clutter and maintain user-focused designs.
- Regularly update data sources to ensure accuracy.