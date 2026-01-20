# Kubernetes PriorityClasses

## Overview
This folder contains Kubernetes **PriorityClass** manifest files used to control **pod scheduling priority and preemption behavior** within the cluster. PriorityClasses ensure that critical workloads are scheduled first and can preempt lower-priority pods when cluster resources are constrained.

These definitions establish a **baseline workload priority model** that can be reused consistently across environments.

---
## PriorityClass Manifests

Each manifest uses the Kubernetes `PriorityClass` resource:

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: <priority-name>
value: <integer>
globalDefault: <true|false>
description: "<description>"
```

---
## Defined Priority Classes

| Priority Name | Value     | Global Default | Purpose                                                                      |
| ------------- | --------- | -------------- | ---------------------------------------------------------------------------- |
| `critical`    | 1,000,000 | false          | Cluster-critical services such as APIs, controllers, and core infrastructure |
| `high`        | 500,000   | false          | Business-critical workloads that must remain highly available                |
| `medium`      | 100,000   | false          | Standard application workloads                                               |
| `low`         | 10,000    | true           | Best-effort, background jobs, and non-critical workloads                     |

> **Note:** `low` is set as the `globalDefault`, meaning pods without an explicit `priorityClassName` will automatically receive this priority.

---
## Usage

To apply all PriorityClass manifests:

```bash
kubectl apply -f .
```

To apply a specific PriorityClass:

```bash
kubectl apply -f <priorityclass-file>.yaml
```

To verify PriorityClasses were created:

```bash
kubectl get priorityclasses
```

---

## How to Use in Workloads

Reference a PriorityClass in your Pod or Deployment spec:

```yaml
spec:
  priorityClassName: high
```

Pods with higher priority values:

* Are scheduled before lower-priority pods
* May **preempt** lower-priority pods if the cluster runs out of resources

---

## Best Practices

* Reserve `critical` for **cluster-level and platform s
