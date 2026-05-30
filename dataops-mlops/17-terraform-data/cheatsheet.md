```markdown
# Terraform for Stateful Data Stacks — Cheatsheet

## [Section 1: Core Syntax]

| Thing                         | Syntax                                  | Notes                                                     |
|-------------------------------|-----------------------------------------|-----------------------------------------------------------|
| Define a StatefulSet          | `resource "kubernetes_stateful_set" "example" { ... }` | Manages deployment and scaling of a set of pods.         |
| VolumeClaimTemplate           | `{ name: "data", size: "1Gi" }`       | Defines persistent storage for StatefulSets.              |
| Update Strategy               | `update_strategy { type = "RollingUpdate" }` | Controls how updates are applied.                         |
| Pod Management Policy         | `pod_management_policy = "OrderedReady"` | Ensures pods are started in order.                        |
| Labels and Annotations        | `metadata { labels = { app = "myapp" } annotations = { version = "v1" } }` | Metadata for resource management.                         |

## [Section 2: Common Operations]

```hcl
# Creating a StatefulSet with Persistent Volume
resource "kubernetes_persistent_volume" "data" {
  metadata {
    name = "data-pv"
  }
  spec {
    capacity {
      storage = "1Gi"
    }
    access_modes = ["ReadWriteOnce"]
    host_path {
      path = "/data"
    }
  }
}

resource "kubernetes_persistent_volume_claim" "data" {
  metadata {
    name = "data-pvc"
  }
  spec {
    access_modes = ["ReadWriteOnce"]
    resources {
      requests {
        storage = "1Gi"
      }
    }
  }
}

resource "kubernetes_stateful_set" "myapp" {
  metadata {
    name = "myapp"
  }
  spec {
    service_name = "myapp"
    replicas     = 3
    selector {
      match_labels = {
        app = "myapp"
      }
    }
    template {
      metadata {
        labels = {
          app = "myapp"
        }
      }
      spec {
        container {
          name  = "myapp"
          image = "myapp:latest"
          ports {
            container_port = 80
          }
          volume_mount {
            name      = "data"
            mount_path = "/data"
          }
        }
      }
    }
    volume_claim_template {
      metadata {
        name = "data"
      }
      spec {
        access_modes = ["ReadWriteOnce"]
        resources {
          requests {
            storage = "1Gi"
          }
        }
      }
    }
  }
}
```

## [Gotchas]

- ⚠️ Ensure your Persistent Volume and Claim are correctly bound; otherwise, pods won't start.
- ⚠️ StatefulSets require a Headless Service for pod networking; don't forget to define that!

## [Mental model]

- **StatefulSets** maintain sticky identities for pods, meaning each pod gets a unique name and stable storage.
- **VolumeClaimTemplates** ensure that each pod gets its own Persistent Volume.
- **Scaling** must be handled carefully; scaling down may leave dangling volumes if not managed.
```