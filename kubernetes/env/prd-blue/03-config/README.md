## Kubernetes Secret Handling

Application credentials are injected into pods via Kubernetes Secrets rather than plaintext environment variables.

At runtime, the application references an existing secret:
```
envFrom:
  - secretRef:
      name: db-credentials
```
This keeps all sensitive values out of version control and deployment manifests.


CI/CD-Driven Secret Creation (GitHub Actions)

Secrets are created or updated dynamically during deployment using GitHub Actions.
The CI pipeline pulls sensitive values from a secure backend (e.g., svault / HashiCorp Vault) and applies them to the cluster as Kubernetes Secrets.

Example GitHub Actions step:
```
- name: Create Kubernetes Secret
  run: |
    kubectl create secret generic db-credentials \
      --from-literal=DB_USERNAME=${{ secrets.DB_USERNAME }} \
      --from-literal=DB_PASSWORD=${{ secrets.DB_PASSWORD }} \
      --dry-run=client -o yaml | kubectl apply -f -
```

