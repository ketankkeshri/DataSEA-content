# Intro

Great Expectations is a powerful tool for ensuring data quality in your data pipelines. As data professionals, we need to build trust in our data, and Great Expectations helps us achieve that by allowing us to define, test, and document expectations about our data. This lesson dives into the foundational aspects of Great Expectations, setting the stage for effective data validation and monitoring.

## What is Great Expectations?

Great Expectations is an open-source Python-based framework designed to help data teams validate, document, and profile their data. It enables you to create expectations—assertions about your data—so you can catch issues early in your data pipelines.

### Key Features

- **Expectation Suites**: Group related expectations together, making it easier to manage and apply them.
- **Data Validation**: Automatically test incoming data against defined expectations, ensuring it meets quality standards.
- **Documentation**: Generate human-readable documentation of your data expectations, making it easier for stakeholders to understand data quality.

Here's a simple example of creating a basic expectation suite:

```python
import great_expectations as ge

# Create a DataFrame
data = {
    "order_id": [1, 2, 3, 4],
    "amount": [100, 150, None, 200],
    "customer_id": [1, 2, 1, 3],
}
df = ge.from_pandas(pd.DataFrame(data))

# Create an Expectation Suite
suite = df.expectation_suite
suite.add_expectation(
    expectation_type="expect_column_values_to_be_in_set",
    kwargs={
        "column": "customer_id",
        "value_set": [1, 2, 3],
    }
)
```

## Why Use Great Expectations?

In today's world of data-driven decision-making, ensuring data quality is crucial. Great Expectations provides a systematic approach to validate your data before it enters production. This minimizes the risks associated with bad data, such as incorrect analytics, faulty machine learning models, and ultimately, poor business decisions.

### Benefits for Data Teams

- **Proactive Quality Control**: Catch data issues before they impact downstream processes.
- **Collaboration**: Share expectations and insights with your team and stakeholders easily.
- **Integration**: Works seamlessly with popular data stacks, making it a flexible choice for modern data workflows.

## Common pitfalls

- **Neglecting Documentation**: Failing to generate and share documentation can lead to misunderstandings about data quality expectations.
- **Overly Complex Expectations**: Keep expectations simple and targeted. Complex expectations can become difficult to manage and understand.
- **Ignoring Context**: Data quality is context-dependent. Ensure expectations align with business goals and data usage.

## In a nutshell

- Great Expectations helps manage data quality by defining, validating, and documenting expectations.
- Expectation suites group related checks, making maintenance easier.
- Proactive validation minimizes risks associated with bad data.
- Effective documentation fosters collaboration across teams.
- Keep expectations simple and relevant to the data context.