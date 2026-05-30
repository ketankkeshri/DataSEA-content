# Entrypoint Vs Cmd

Understanding the difference between `ENTRYPOINT` and `CMD` in Docker is crucial for DataOps and MLOps professionals. These directives dictate how your container runs and can significantly impact your deployment strategy.

## What is ENTRYPOINT?

`ENTRYPOINT` defines the main command that gets executed when a container starts. It sets the container's executable, making it the primary way to run your application. 

You can set it in two ways: with an exec form or a shell form.

### Exec Form

Using the exec form allows you to specify the command and its arguments as a JSON array. This is the recommended approach because it avoids issues with signal handling.

```dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

# Setting ENTRYPOINT
ENTRYPOINT ["python", "app.py"]
```

### Shell Form

The shell form runs the command in a shell, which can lead to unexpected behaviors, especially with signal handling.

```dockerfile
ENTRYPOINT python app.py
```

## What is CMD?

`CMD` provides default arguments to the `ENTRYPOINT` or specifies a command to run if no arguments are provided. If you provide arguments to the container at runtime, they will override the `CMD` values.

### Basic Usage

If you only use `CMD`, it defines what to run when the container starts:

```dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

# Setting CMD
CMD ["python", "app.py"]
```

### With ENTRYPOINT

When combined with `ENTRYPOINT`, `CMD` can provide default arguments:

```dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "app.py"]
CMD ["--port", "8080"]
```

In this example, if you run the container without any arguments, it executes `python app.py --port 8080`. However, if you specify a different port, that value will replace `8080`.

## Common pitfalls

- **Confusion between ENTRYPOINT and CMD**: Remember, `ENTRYPOINT` is your main command, while `CMD` provides default arguments or commands.
- **Overriding CMD unintentionally**: If you specify a command when running the container, it will override `CMD`, which might lead to unexpected behavior.
- **Signal handling issues**: Using shell form for `ENTRYPOINT` can lead to problems with signal propagation, making it hard to stop containers gracefully.

## In a nutshell

- `ENTRYPOINT` sets the main command for the container.
- `CMD` provides default arguments or commands.
- Use exec form for `ENTRYPOINT` for better signal handling.
- `CMD` can be overridden by command-line arguments when running the container.
- Understand the interplay between `ENTRYPOINT` and `CMD` to avoid deployment issues.