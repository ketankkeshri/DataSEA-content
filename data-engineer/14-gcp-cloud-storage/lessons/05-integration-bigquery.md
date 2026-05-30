# Integration BigQuery

Integrating Google Cloud Storage (GCS) with BigQuery allows you to analyze large datasets efficiently and cost-effectively. For data engineers, this synergy simplifies data pipelines, enabling real-time analytics and powerful insights.

## Setting Up the Integration

Before diving into code, ensure you have the necessary permissions. You need the `bigquery.dataEditor` role for your service account to load data from GCS into BigQuery.

1. **Create a BigQuery Dataset**:
   ```bash
   bq mk my_dataset
   ```

2. **Upload Data to GCS**:
   For example, let’s say you have a CSV file named `sales_data.csv` in your local directory. You can upload it to GCS like this:
   ```bash
   gsutil cp sales_data.csv gs://my_bucket/sales_data/
   ```

3. **Load Data into BigQuery**:
   Now, you can load this data into your BigQuery dataset. Here’s how:
   ```bash
   bq load --source_format=CSV \
   my_dataset.sales_data \
   gs://my_bucket/sales_data/sales_data.csv \
   schema_field1:STRING,schema_field2:INTEGER,schema_field3:FLOAT
   ```

### Querying the Data

Once the data is loaded, you can run SQL queries against it. Here’s a straightforward query to get you started:
```sql
SELECT 
    schema_field1,
    COUNT(*) AS total_sales
FROM 
    `my_project.my_dataset.sales_data`
GROUP BY 
    schema_field1
ORDER BY 
    total_sales DESC
LIMIT 10;
```

This query will return the top 10 products by sales, which can be critical for business decisions.

## Automating the Process

To streamline this integration, consider using Cloud Functions or Dataflow. Below is a simple Cloud Function that triggers on new files uploaded to your GCS bucket and loads them into BigQuery automatically.

```python
from google.cloud import bigquery
from google.cloud import storage

def load_data_to_bigquery(event, context):
    bucket_name = event['bucket']
    file_name = event['name']
    
    client = bigquery.Client()
    dataset_id = 'my_dataset'
    table_id = 'sales_data'
    
    uri = f'gs://{bucket_name}/{file_name}'
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
    )
    
    load_job = client.load_table_from_uri(uri, f'{dataset_id}.{table_id}', job_config=job_config)
    load_job.result()  # Wait for the job to complete
```

Deploy this function to automatically load data into BigQuery whenever a new file is uploaded to the specified GCS bucket. 

## Common pitfalls

- **Schema Mismatch**: Ensure the schema defined in BigQuery matches the data types in your CSV. A mismatch will lead to load errors.
- **Large File Sizes**: Loading overly large files can time out. Split files into smaller chunks for smoother ingestion.
- **Service Account Permissions**: Double-check that your service account has the required permissions to write to BigQuery and read from GCS.

## In a nutshell

- Integrating GCS with BigQuery enhances data analytics capabilities.
- Use `bq` commands to load data efficiently.
- Automate data loading with Cloud Functions for real-time processing.
- Always verify schema compatibility to avoid ingestion issues.
- Monitor permissions to ensure seamless operations.