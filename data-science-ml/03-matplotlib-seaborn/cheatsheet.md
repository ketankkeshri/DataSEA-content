```markdown
# Matplotlib & Seaborn — Cheatsheet

## [Core syntax]

| Thing                     | Syntax                                           | Notes                                     |
|---------------------------|--------------------------------------------------|-------------------------------------------|
| Import Matplotlib          | `import matplotlib.pyplot as plt`               | Standard import for plotting.             |
| Import Seaborn            | `import seaborn as sns`                         | Simplifies statistical visualizations.    |
| Create a figure           | `plt.figure(figsize=(width, height))`          | Set figure dimensions.                     |
| Show plot                 | `plt.show()`                                    | Displays the current figure.              |

## [Common plots]

```python
# Line Plot
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar Plot
plt.bar(categories, values)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Histogram
plt.hist(data, bins=10)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

## [Seaborn Statistical Plots]

```python
# Scatter Plot
sns.scatterplot(data=df, x='feature1', y='feature2', hue='category')
plt.title("Scatter Plot")
plt.show()

# Box Plot
sns.boxplot(data=df, x='category', y='value')
plt.title("Box Plot")
plt.show()

# Pair Plot
sns.pairplot(df, hue='category')
plt.show()
```

## [Customization]

| Customization            | Syntax                                                | Notes                                      |
|-------------------------|------------------------------------------------------|--------------------------------------------|
| Set title               | `plt.title("Title")`                                | Add a title to the plot.                   |
| Set axis labels         | `plt.xlabel("X-axis")`, `plt.ylabel("Y-axis")`     | Label the axes.                            |
| Change color            | `plt.plot(x, y, color='red')`                       | Set line color.                            |
| Add legend              | `plt.legend(['Label1', 'Label2'])`                 | Create a legend for the plot.             |
| Save plot               | `plt.savefig("filename.png")`                       | Save the figure as an image file.         |

## [Gotchas]

- ⚠️ Make sure to call `plt.show()` to display your plots, especially in scripts.
- ⚠️ Pay attention to the order of commands. Some commands (like `plt.title()`) must come after the plot command.

## [Mental model]

- **Figure**: The entire window or image.
- **Axes**: The area where data is plotted; a figure can have multiple axes.
- **Plot Types**: Different types of visualizations (e.g., line, bar, scatter) that can be created using the axes.
```