# Virtualenv Pip

Managing dependencies is crucial for any data engineering project. Using virtual environments with `pip` allows you to isolate project dependencies, ensuring that your code runs consistently across different setups. This is essential for avoiding the "works on my machine" syndrome.

## What is Virtualenv?

`virtualenv` is a tool that creates isolated Python environments. Each virtual environment has its own Python interpreter and dependencies, independent of the global Python installation. This means you can have multiple projects on the same machine, each with its own set of libraries.

### Setting Up Virtualenv

1. **Install virtualenv** (if not already installed):
   ```bash
   pip install virtualenv
   ```

2. **Create a new virtual environment**:
   ```bash
   virtualenv myenv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Deactivate the virtual environment when done**:
   ```bash
   deactivate
   ```

Once activated, any packages installed using `pip` will only affect this environment.

## Using Pip with Virtualenv

Now that you have your virtual environment set up, let’s see how to use `pip` to manage dependencies.

### Installing Packages

With your virtual environment activated, you can install packages like this:
```bash
pip install pandas numpy
```

This installs `pandas` and `numpy` only in the `myenv` environment. You can check the installed packages with:
```bash
pip list
```

### Saving and Loading Dependencies

To keep track of your project’s dependencies, you can create a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

To install all dependencies from this file later:
```bash
pip install -r requirements.txt
```

### Example: Setting Up a Data Project

Let’s say you’re building a data pipeline that uses `pandas` for data manipulation and `numpy` for numerical computations. Here’s a simple setup:

1. Create a new virtual environment:
   ```bash
   virtualenv data-pipeline-env
   ```

2. Activate it:
   ```bash
   source data-pipeline-env/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install pandas numpy
   ```

4. Create your `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

Now you can share your `requirements.txt` with teammates, ensuring everyone has the same setup!

## Common pitfalls

- **Forget to activate the environment**: Always check that your virtual environment is activated before running your scripts or installing packages.
- **Installing globally instead of in the virtualenv**: If you forget to activate your virtual environment, `pip` will install packages globally, which can lead to version conflicts.
- **Not using `requirements.txt`**: Skipping this step can make it hard to recreate the environment later or for teammates to set up the project.

## In a nutshell

- Use `virtualenv` to create isolated Python environments.
- Activate your environment to manage dependencies specific to your project.
- Use `pip freeze > requirements.txt` to keep track of your dependencies.
- Always remember to activate your virtual environment before working on your project.