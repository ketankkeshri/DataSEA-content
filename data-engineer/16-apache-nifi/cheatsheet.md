```markdown
# Apache NiFi — Cheatsheet

## [Section 1: Processors]

| Processor | Purpose | Configuration |
|-----------|---------|---------------|
| `GetFile` | Ingest files from the filesystem | Set `Input Directory`, `File Filter` |
| `PutFile` | Write files to the filesystem | Set `Output Directory` |
| `ExecuteSQL` | Run SQL queries against a database | Set `Database Connection Pooling Service` |
| `RouteOnAttribute` | Route flow files based on attributes | Define rules in `Routing` properties |
| `MergeContent` | Merge multiple flow files | Set `Correlation Attribute Name` |

## [Section 2: Flow Design]

```xml
<flow>
    <processor>
        <name>GetFile</name>
        <config>
            <inputDirectory>/path/to/input</inputDirectory>
        </config>
    </processor>
    <processor>
        <name>PutFile</name>
        <config>
            <outputDirectory>/path/to/output</outputDirectory>
        </config>
    </processor>
</flow>
```

## [Monitoring]

- Use the **Bulletin Board** to check for warnings and errors.
- Monitor processor statistics (e.g., **Input/Output Count**, **Processing Time**) on the **Status** tab.
- Leverage the **NiFi Registry** for version control of flows.

## [Gotchas]

- ⚠️ Ensure proper file permissions for `GetFile` and `PutFile` processors.
- ⚠️ Watch out for backpressure; configure thresholds to prevent flow file backlog.
- ⚠️ Be cautious with circular references in flow designs, as they can lead to infinite loops.

## [Mental model]

1. **FlowFiles** are the core data units, carrying data and attributes.
2. **Processors** transform FlowFiles, performing actions like ingesting, processing, and routing.
3. **Connections** link processors and determine how FlowFiles move through the flow.
```