```markdown
# Docker Fundamentals — Cheatsheet

## [Section 1: Core Commands]

| Thing               | Syntax                          | Notes                               |
|---------------------|---------------------------------|-------------------------------------|
| Build an image      | `docker build -t <name>:<tag> <path>` | Builds an image from Dockerfile.   |
| Run a container      | `docker run <options> <image>` | Starts a container from an image.   |
| List containers      | `docker ps`                     | Shows running containers. Use `-a` for all. |
| Stop a container     | `docker stop <container_id>`    | Stops a running container.          |
| Remove a container   | `docker rm <container_id>`      | Deletes a stopped container.        |
| Remove an image      | `docker rmi <image_id>`         | Deletes an image.                   |

## [Section 2: Dockerfile Instructions]

```dockerfile
# Sample Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

## [Section 3: Networking]

| Command                    | Syntax                       | Notes                               |
|----------------------------|------------------------------|-------------------------------------|
| Create a network           | `docker network create <net>`| Creates a new network.              |
| List networks              | `docker network ls`          | Displays all networks.              |
| Connect a container to network | `docker network connect <net> <container>` | Connects a container to a network. |
| Disconnect a container     | `docker network disconnect <net> <container>` | Disconnects a container from a network. |

## [Section 4: Volumes]

| Command                    | Syntax                       | Notes                               |
|----------------------------|------------------------------|-------------------------------------|
| Create a volume            | `docker volume create <name>`| Creates a new volume.               |
| List volumes               | `docker volume ls`           | Displays all volumes.               |
| Remove a volume            | `docker volume rm <volume>`  | Deletes a volume.                   |
| Mount a volume             | `docker run -v <volume>:<path> <image>` | Mounts a volume to a container. |

## [Section 5: Docker Compose]

```yaml
# Sample docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
  
  db:
    image: postgres
    environment:
      POSTGRES_DB: example
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
```

## [Gotchas]

- ⚠️ Always specify a version in `docker-compose.yml` to avoid compatibility issues.
- ⚠️ Remember to use `.dockerignore` to exclude files from context during builds.

## [Mental model]

- **Images** are templates; **Containers** are running instances.
- Use **Volumes** for persistent storage across containers.
- **Networks** allow containers to communicate securely.
```