# Kubernetes RBAC and ServiceAccount Configuration

This repository contains Role, RoleBinding, and ServiceAccount YAML configurations for **development (dev), staging (stg), and production (prd)** environments in Kubernetes. These configurations define permissions and access control for application teams across different environments.

---

## File Structure

| File | Environment | Type | Purpose |
|------|------------|------|---------|
| `_role_dev.yaml` | dev | Role | Grants full access to development workloads for rapid iteration. |
| `_role_stg.yaml` | stg | Role | Provides controlled access to staging workloads for testing and validation. |
| `_role_prd.yaml` | prd | Role | Provides read-only access to production workloads for monitoring. |
| `_rolebinding-dev.yaml` | dev | RoleBinding | Binds the `dev-team` group to the dev Role. |
| `_rolebinding-stg.yaml` | stg | RoleBinding | Binds the `stg-team` group to the staging Role. |
| `_rolebinding-prd.yaml` | prd | RoleBinding | Binds the `prod-team` group to the production Role. |
| `_serviceaccount-dev.yaml` | dev | ServiceAccount | ServiceAccount for applications in dev. |
| `_serviceaccount-stg.yaml` | stg | ServiceAccount | ServiceAccount for applications in staging. |
| `_serviceaccount-prd.yaml` | prd | ServiceAccount | ServiceAccount for applications in production with token disabled for security. |

---

## Roles

### Development Role (`_role_dev.yaml`)
- Full access to workloads and config resources (`pods`, `deployments`, `services`, `configmaps`, `secrets`, etc.)  
- Allows viewing logs and executing commands inside pods for debugging.  
- Suitable for rapid development and testing in the `dev` namespace.  

### Staging Role (`_role_stg.yaml`)
- Allow read/write access to workloads for validation and testing, and perform limited manual fixes for issues missed in dev environment, which should later be codified.
- Read-only access to secrets.  
- Logs are viewable; `exec` is restricted.  
- Ensures controlled testing before production deployment.  

### Production Role (`_role_prd.yaml`)
- Read-only access to workloads and configs.  
- No direct write or exec permissions.  
- Designed to prevent accidental modification in the `prd` namespace.  

---

## RoleBindings

- Bind environment-specific user groups to their corresponding roles.
- Ensures that only authorized teams have access to each environment.

| Namespace | RoleBinding | Group |
|-----------|------------|-------|
| dev | `app-rolebinding` | dev-team |
| stg | `app-rolebinding` | stg-team |
| prd | `app-rolebinding` | prod-team |

---

## ServiceAccounts

- Each environment has a dedicated ServiceAccount for workloads.
- Production ServiceAccount disables automatic token mounting for added security.

| Namespace | ServiceAccount | Notes |
|-----------|---------------|-------|
| dev | `app-sa` | Standard ServiceAccount for development pods. |
| stg | `app-sa` | Standard ServiceAccount for staging pods. |
| prd | `app-sa` | Token automount disabled to enhance security. |

---

## Usage

1. Apply roles and role bindings:

```bash
kubectl apply -f _role_dev.yaml
kubectl apply -f _rolebinding-dev.yaml
kubectl apply -f _serviceaccount-dev.yaml