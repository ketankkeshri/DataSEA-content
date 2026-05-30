```markdown
# Container Initialization — Cheatsheet

## Section 1: Core Concepts

| Thing                  | Syntax                                      | Notes                                           |
|-----------------------|---------------------------------------------|-------------------------------------------------|
| Dockerfile            | `FROM <base-image>`                         | Starting point for your Docker image.          |
| Multi-stage Build     | `FROM <image> AS <stage-name>`             | Use multiple stages to optimize builds.         |
| Layer Caching         | `RUN <command>`                             | Docker caches layers to speed up builds.        |
| ENTRYPOINT            | `ENTRYPOINT ["executable", "param1", "param2"]` | Defines the default command to run.            |
| CMD                   | `CMD ["param1", "param2"]`                 | Default parameters for the ENTRYPOINT command.  |

## Section 2: Common Operations

```dockerfile
# Example Dockerfile with multi-stage build and caching
# Stage 1: Build
FROM python:3.10 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2: Run
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /app .
ENTRYPOINT ["python"]
CMD ["app.py"]
```

## Gotchas

- ⚠️ Multi-stage builds can increase image size if not properly managed. Always use `--squash` for optimization.
- ⚠️ Remember that `CMD` can be overridden by command-line arguments when you run the container.

## Mental model

- **Multi-stage build**: Separate build and runtime environments to keep images lightweight.
- **Layer caching**: Docker only rebuilds layers that have changed, saving time and resources.
- **ENTRYPOINT vs CMD**: Use `ENTRYPOINT` for the main executable; `CMD` for default arguments.
```