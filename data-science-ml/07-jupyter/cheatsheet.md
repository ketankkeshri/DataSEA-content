```markdown
# Jupyter Productivity — Cheatsheet

## [Core syntax]

| Thing              | Syntax                             | Notes                                      |
|--------------------|------------------------------------|--------------------------------------------|
| Create a notebook   | `jupyter notebook`                 | Launches the Jupyter Notebook interface.   |
| Open a specific notebook | `jupyter notebook your_notebook.ipynb` | Opens the specified notebook directly.    |
| Save notebook       | `Ctrl + S`                         | Saves the current notebook.                |
| Run cell            | `Shift + Enter`                   | Executes the current cell and selects the next one. |
| Insert cell below   | `B` (in command mode)             | Adds a new cell below the selected cell.  |
| Delete cell         | `D, D` (in command mode)          | Deletes the selected cell.                 |

## [Magics]

| Magic Command       | Syntax                             | Notes                                      |
|---------------------|------------------------------------|--------------------------------------------|
| List all magics     | `%lsmagic`                        | Displays all available magic commands.     |
| Time execution       | `%time` or `%timeit`             | Measures execution time of a single statement or multiple runs. |
| Run script           | `%run your_script.py`            | Executes a Python script in the current notebook environment. |
| Load a module        | `%load your_module.py`           | Loads the contents of a Python file into a cell. |

## [Reproducibility]

| Concept             | Description                         | Notes                                      |
|---------------------|------------------------------------|--------------------------------------------|
| Version control      | Use Git to track notebook changes. | Use `.gitignore` to exclude checkpoints.  |
| Environment management | Use `requirements.txt` or `environment.yml` | Specify package versions for reproducibility. |

## [Papermill]

| Command             | Syntax                             | Notes                                      |
|---------------------|------------------------------------|--------------------------------------------|
| Execute notebook     | `papermill input_notebook.ipynb output_notebook.ipynb` | Runs a notebook and saves the results in a new file. |
| Parameterize notebook | Use `parameters` in the notebook | Pass parameters to customize execution. |

## [Nbconvert]

| Command             | Syntax                             | Notes                                      |
|---------------------|------------------------------------|--------------------------------------------|
| Convert to HTML      | `jupyter nbconvert --to html your_notebook.ipynb` | Converts notebook to an HTML file.        |
| Convert to PDF       | `jupyter nbconvert --to pdf your_notebook.ipynb` | Converts notebook to a PDF file.          |

## [Gotchas]

- ⚠️ Running `%run` will reset the notebook's state. Use with caution!
- ⚠️ Output files from `nbconvert` may not reflect the latest changes unless saved first.

## [Mental model]

1. **Notebooks** are interactive documents combining code, output, and narrative.
2. **Magics** enhance functionality with special commands for quick tasks.
3. **Reproducibility** ensures consistent results across different environments.
```