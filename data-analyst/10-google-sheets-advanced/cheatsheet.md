```markdown
# Google Sheets Advanced — Cheatsheet

## [Section 1: Query Function]

| Thing           | Syntax                                           | Notes                                |
|-----------------|--------------------------------------------------|--------------------------------------|
| Basic Query     | `=QUERY(data, query, [headers])`               | Fetches data based on a SQL-like query. |
| Select Columns   | `=QUERY(data, "SELECT A, B WHERE C > 10")`   | Replace A, B, C with your column labels. |
| Order By        | `=QUERY(data, "SELECT * ORDER BY A DESC")`    | Sort results by column A in descending order. |
| Filter          | `=QUERY(data, "SELECT * WHERE A CONTAINS 'text'")` | Filters rows containing 'text' in column A. |

## [Section 2: Import Range]

| Thing           | Syntax                                          | Notes                                |
|-----------------|-------------------------------------------------|--------------------------------------|
| Basic Import    | `=IMPORTRANGE("spreadsheet_url", "range")`   | Imports data from another sheet.   |
| Example         | `=IMPORTRANGE("1ABC23xyz", "Sheet1!A1:B10")` | Replace with your actual URL and range. |
| Permissions      | Must allow access to the sheet on first use.   | You'll need to authorize the connection. |

## [Section 3: Apps Script Intro]

| Thing           | Syntax                                          | Notes                                |
|-----------------|-------------------------------------------------|--------------------------------------|
| Open Script     | `Extensions > Apps Script`                     | Opens the Apps Script editor.       |
| Basic Function   | `function myFunction() { Logger.log('Hello, world!'); }` | Create a simple log function.       |
| Trigger          | `ScriptApp.newTrigger('myFunction').timeBased().everyMinutes(5).create();` | Sets a trigger to run every 5 minutes. |

## [Section 4: Automation]

| Thing           | Syntax                                          | Notes                                |
|-----------------|-------------------------------------------------|--------------------------------------|
| Create Trigger   | `ScriptApp.newTrigger('functionName').forSpreadsheet(spreadsheet).onEdit().create();` | Runs a function on spreadsheet edit. |
| Send Email      | `MailApp.sendEmail('email@example.com', 'Subject', 'Body');` | Sends an email via script.          |
| Schedule Task   | `ScriptApp.newTrigger('myFunction').timeBased().everyHours(1).create();` | Runs a function every hour.         |

## [Gotchas]

- ⚠️ Remember to enable the Google Sheets API if using Apps Script.
- ⚠️ `IMPORTRANGE` might take a moment to update after changes.
- ⚠️ Queries are case-sensitive; ensure correct casing when filtering.

## [Mental model]

- **Query Function**: Think of it as a mini-database inside your sheet. Filter, sort, and manipulate data like SQL.
- **Import Range**: Bridge between sheets. Use to consolidate or analyze data from multiple sources.
- **Apps Script**: Your own automation robot. Write functions to automate repetitive tasks and enhance functionality.

```