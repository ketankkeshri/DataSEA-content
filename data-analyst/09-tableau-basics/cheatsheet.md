```markdown
# Tableau Basics — Cheatsheet

## [Section 1: Core Concepts]

| Thing                | Syntax                                               | Notes                                          |
|---------------------|-----------------------------------------------------|------------------------------------------------|
| Connecting to Data  | Use "Connect" pane to select data source           | Supports Excel, SQL, Google Sheets, etc.      |
| Filters              | Drag to Filters shelf or right-click > Filter      | Filters data displayed in visualizations       |
| Groups               | Right-click > Create Group                          | Combine multiple dimension members into one    |
| Sets                 | Right-click > Create Set                            | Custom subsets of data based on conditions     |
| Calculated Fields    | `IF [Field] > value THEN "Label" END`             | Create new fields based on existing data       |

## [Section 2: Marks Shelf]

```plaintext
# Marks Shelf Options
- Color: Drag field here to color code marks
- Size: Adjust size of marks based on a measure
- Label: Add text labels to marks
- Detail: Break down marks into more granularity
- Tooltip: Customize tooltips for better info display
```

## [Section 3: Dashboards]

```plaintext
# Dashboard Actions
- Drag sheets to dashboard area
- Use "Tiled" or "Floating" layouts
- Add actions: Dashboard > Actions > Add Action
- Filter actions: filter data across sheets with selections
```

## [Gotchas]

- ⚠️ Calculated fields are only evaluated when used in a visualization; test frequently.
- ⚠️ Filters on a dashboard can impact performance; use them wisely.

## [Mental Model]

- **Data Source → Sheets → Dashboards**
- Each sheet can be a separate view of the same data.
- Dashboards are collections of sheets that provide a holistic view.
```