# Appsscript Intro

Google Apps Script is a powerful tool that can supercharge your Google Sheets experience. If you want to automate repetitive tasks, integrate with other Google services, or create custom functions, learning Apps Script is a game-changer for data analysts and engineers alike.

## What is Google Apps Script?

Google Apps Script is a JavaScript-based platform that allows you to extend and automate Google Workspace applications. With it, you can create custom scripts that run directly in your Google Sheets, enhancing your data manipulation capabilities beyond the built-in functions.

### Why Use Apps Script?

- **Automation**: Automate repetitive tasks like data entry, formatting, or report generation.
- **Integration**: Connect with other Google services (e.g., Gmail, Google Drive) to pull or push data seamlessly.
- **Custom Functions**: Create your own functions tailored to your specific data needs.

Here’s a simple example of a custom function that sums a range of numbers:

```javascript
function sumRange(range) {
  var total = 0;
  for (var i = 0; i < range.length; i++) {
    total += range[i][0]; // Access the first element in each row
  }
  return total;
}
```

You can use this function directly in your Google Sheets like this: `=sumRange(A1:A10)`.

## Getting Started with Apps Script

To create a script in Google Sheets:

1. Open your Google Sheet.
2. Click on `Extensions` > `Apps Script`.
3. This opens the Apps Script editor where you can write your code.

### Example: Automating Email Reports

Let’s say you want to send a weekly summary report via email. Here’s how you can automate that:

```javascript
function sendWeeklyReport() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var emailAddress = "your-email@example.com"; // Replace with your email

  var subject = "Weekly Report";
  var body = "Here’s your weekly summary:\n\n";

  // Loop through data to build the report body
  for (var i = 1; i < data.length; i++) {
    body += "Item: " + data[i][0] + ", Quantity: " + data[i][1] + "\n";
  }

  MailApp.sendEmail(emailAddress, subject, body);
}
```

With this script, you can set a trigger to run `sendWeeklyReport()` every week, keeping your team updated without lifting a finger.

## Common pitfalls

- **Authorization issues**: Make sure to authorize your script to access the necessary services, like Gmail or Drive.
- **Quota limits**: Google enforces limits on script executions and API calls. Be mindful of these to avoid disruptions.
- **Debugging**: Use `Logger.log()` to help identify issues in your scripts. Debugging can be tricky without proper logging.

## In a nutshell

- Google Apps Script extends Google Sheets with custom automation and integrations.
- Create custom functions and automate tasks like sending email reports.
- Always check for authorization and quota limits to avoid disruptions.
- Use logging for easier debugging and maintenance of your scripts.