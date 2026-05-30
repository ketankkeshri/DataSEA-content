```markdown
# Great Expectations — Cheatsheet

## [Section 1: Core Concepts]

| Thing                   | Syntax/Description                                               | Notes                                                   |
|------------------------|---------------------------------------------------------------|---------------------------------------------------------|
| Expectation Suite      | `expectation_suite = context.create_expectation_suite("suite_name")` | A collection of expectations for validating data.       |
| Add Expectation        | `expectation_suite.add_expectation(<expectation>)`           | Add individual expectations to the suite.               |
| Validate Data          | `validator = context.get_validator(expectation_suite)`        | Creates a validator for checking data against expectations. |
| Validation Result      | `result = validator.validate(<data>)`                         | Validates the data and returns a result object.         |
| Docs Site              | `great_expectations docs site`                                | Auto-generates documentation for your expectations.     |

## [Section 2: Common Operations]

```python
# Create an expectation suite and add expectations
import great_expectations as ge

# Initialize context
context = ge.data_context.DataContext("path/to/your/great_expectations/directory")

# Create expectation suite
expectation_suite = context.create_expectation_suite("my_suite")

# Add expectations
expectation_suite.add_expectation(
    ge.expectations.expect_column_values_to_be_in_set("column_name", ["value1", "value2"])
)

# Validate data
validator = context.get_validator(expectation_suite)
result = validator.validate(ge.read_csv("path/to/your/data.csv"))
print(result)
```

## [Gotchas]

- ⚠️ Expectation suites are mutable; changes persist unless explicitly saved.
- ⚠️ Ensure your data source is compatible with Great Expectations (e.g., Pandas, Spark).

## [Mental model]

- **Expectations** are rules for data; they live in **Expectation Suites**.
- **Validation** checks if your data adheres to these expectations.
- **Documentation** auto-generates to help maintain data quality standards.
```