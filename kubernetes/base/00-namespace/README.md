# Kubernetes Namespaces

## Overview
This folder contains Kubernetes manifest files used to create and manage **environment-specific namespaces**. Namespaces help logically separate resources, apply policies, and manage access across different deployment stages.

The namespaces defined here represent common application lifecycle environments:

* **dev** – Development environment
* **stg** – Staging / pre-production environment
* **prd** – Production environment

---

## Namespace Manifests

Each manifest uses the Kubernetes `Namespace` resource:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: <namespace-name>
```

### Defined Namespaces

| Namespace | Purpose                                             |
| --------- | --------------------------------------------------- |
| `dev`     | Used for development and testing by engineers       |
| `stg`     | Used for staging, QA, and pre-production validation |
| `prd`     | Used for production workloads                       |

---

## Usage

To apply all namespace manifests:

```bash
kubectl apply -f .
```

To apply a specific namespace only:

```bash
kubectl apply -f <namespace-file>.yaml
```

To verify namespaces were created:

```bash
kubectl get namespaces
```