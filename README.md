# beatdapp
Beatdapp Take-Home Assignment – Platform Engineering Golden Path


### Techniques & Design Principles

1. Strong Decoupling: Keeps files small for easier updates, reviews, and rollbacks. Improves clarity, maintainability, and CI/GitOps safety. Scales cleanly across environments and cloud providers

### Limitations & Considerations
1. CI/CD Timeouts: When running workflows on GitHub Actions (GHA), be mindful of session and job timeouts, especially for long-running Kubernetes operations.
2. EKS Version Constraints: Certain EKS versions may require workarounds, such as combining Bash commands, due to version-specific limitations in tooling or API behavior.