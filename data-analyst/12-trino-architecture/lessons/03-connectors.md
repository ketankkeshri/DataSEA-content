# Connectors

Connectors are the lifeblood of Trino, enabling it to communicate with various data sources. Understanding how these connectors work is crucial for data engineers and analysts who want to leverage Trino's capability to query across different databases seamlessly.

## What are Connectors?

Connectors in Trino are plugins that allow the query engine to connect to a specific data source. This can include databases like MySQL, PostgreSQL, and even cloud storage systems like AWS S3. Each connector abstracts the underlying data source's specifics, allowing users to write SQL queries as if they were querying a single database.

### How Connectors Work

When a query is executed, Trino uses the appropriate connector to fetch the data. The connectors translate the SQL queries into the native query language of the data source, retrieve the data, and then return it to Trino for further processing.

Here's a basic example of how you would configure a MySQL connector in Trino:

```properties
connector.name=mysql
connection-url=jdbc:mysql://localhost:3306
connection-user=root
connection-password=your_password
```

In this configuration:
- `connector.name` specifies the type of connector.
- `connection-url` is the JDBC URL for your MySQL database.
- `connection-user` and `connection-password` are your credentials.

## Configuring Connectors

To use a connector in Trino, you need to set it up correctly in your `catalog` directory. Each connector has its own configuration file, typically in `.properties` format. Here's how you can set up a PostgreSQL connector:

```properties
connector.name=postgresql
connection-url=jdbc:postgresql://localhost:5432/mydb
connection-user=myuser
connection-password=mypassword
```

### Best Practices for Connector Configuration

- **Use Environment Variables:** For sensitive data like passwords, consider using environment variables instead of hardcoding them in configuration files.
- **Test Connections:** Always test your connector configurations to ensure they work before running complex queries.
- **Monitor Performance:** Keep an eye on query performance, as poorly configured connectors can lead to slow query times.

## Common pitfalls

- **Misconfigured JDBC URLs:** A small typo in your connection URL can lead to connection failures. Double-check your syntax!
- **Driver Issues:** Ensure that the correct JDBC driver is available for your data source. Missing drivers can cause errors at runtime.
- **Incompatible Data Types:** Some connectors may have limitations or specific requirements for data types. Always consult the connector documentation for compatibility.

## In a nutshell

- Connectors enable Trino to query multiple data sources seamlessly.
- Each connector requires specific configuration settings in the `catalog` directory.
- Best practices include using environment variables for sensitive data and monitoring performance.
- Common pitfalls include misconfigured URLs, missing drivers, and incompatible data types.