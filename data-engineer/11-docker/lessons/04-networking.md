# Networking

Networking is a crucial aspect of Docker that allows containers to communicate with each other and the outside world. Understanding Docker networking is essential for data engineers working with microservices or containerized applications, as it directly impacts application performance and scalability.

## Docker Networking Basics

Docker networking enables containers to connect and interact seamlessly. By default, Docker creates a virtual bridge network called `bridge`, which allows containers to communicate with each other on the same host. Here's how you can see the networks on your Docker host:

```bash
docker network ls
```

You’ll see a list of networks, including the default ones like `bridge`, `host`, and `none`. 

### Creating a Custom Network

Creating a custom network can help you manage communication between containers more effectively. Here's how to create a new Docker network:

```bash
docker network create my_custom_network
```

To run a container attached to this network, use:

```bash
docker run -d --name my_container --network my_custom_network nginx
```

Now, any other containers connected to `my_custom_network` can easily communicate with `my_container` using its container name.

## Container Communication

Containers in the same network can communicate using their names as hostnames. Let’s say you have two containers: `app` and `db`. Here’s how you might run them:

```bash
docker run -d --name db --network my_custom_network postgres
docker run -d --name app --network my_custom_network my_app_image
```

In your application code, you can connect to the database using `db` as the hostname:

```python
import psycopg2

connection = psycopg2.connect(
    host="db",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
```

This setup allows for easy inter-container communication, crucial for applications relying on microservices architecture.

## Common pitfalls

- **Not specifying the network:** If you forget to specify a network, your containers may be isolated on different networks, preventing them from communicating.
- **Confusing container names with hostnames:** Remember, when connecting to a service in another container, use the container name as the hostname, not the IP address.
- **Default network limitations:** The default `bridge` network has limitations on DNS resolution and might not suit complex applications needing custom routing.

## In a nutshell

- Docker networking allows containers to communicate via defined networks.
- Use `docker network create` to set up custom networks for better management.
- Inter-container communication uses container names as hostnames.
- Be aware of common pitfalls to avoid networking issues in production.
- Mastering Docker networking is key for scalable and efficient data engineering workflows.