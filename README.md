# beatdapp
Beatdapp Take-Home Assignment – Platform Engineering Golden Path


### Techniques & Design Principles

1. Strong Decoupling: Keeps files small for easier updates, reviews, and rollbacks. Improves clarity, maintainability, and CI/GitOps safety. Scales cleanly across environments and cloud providers

### Limitations & Considerations
1. CI/CD Timeouts: When running workflows on GitHub Actions (GHA), be mindful of session and job timeouts, especially for long-running Kubernetes operations.
2. EKS Version Constraints: Certain EKS versions may require workarounds, such as combining Bash commands, due to version-specific limitations in tooling or API behavior.



### Developer Workflow Policy – “Golden Path”
The purpose of this policy is to define a safe, controlled, and automated workflow for code changes and deployments, minimizing the risk of unintended modifications to production environments while maintaining development efficiency.

#### Scope
This policy applies to all developers, reviewers, and CI/CD pipelines responsible for deploying code to development, staging, and production environments.

    Policy Statements
    1. Code Deployment
        - Developers do not have direct access to production deployments. (Should be managed in IAM Role in AWS)
            - Manual deployment commands such as kubectl apply -f * are prohibited in STAGE and PRODUCTION.
            - Deployment to production occurs only after pipeline enforcement and approval.
        - All code changes must be deployed through the CI/CD pipeline (e.g., GitHub Actions).
        
    2. Code Review
        - Every change must be reviewed and approved by at least two reviewers.
        - Pull requests should be small and focused. This ensures that managers or approvers can quickly understand the change without needing deep technical knowledge, making it easier to review and approve policy implementations efficiently.
        - Changes to production-specific files from the development branch are automatically rejected by reviewers. (Separation of PR between environment is REQUIRED)

    3. Branching Strategy
        - Branching may be environment-specific, featured-specific or managed in a single branch. (Culture)
        - The chosen strategy must be documented, agreed upon, and consistently applied by the team. (Culture)

    4. Environment-Specific Restrictions
        - Developers working in the development environment may modify only dev-specific files. (Culture)
        - Production access are restricted and require review and pipeline approval before deployment. 

    5. Automated Deployment
        - CI/CD pipelines enforce all deployment rules, approval workflows, and environment restrictions.
        - Deployment steps are auditable and controlled, improving visibility between dev, staging, and production environments.
        - Manual changes to production are strictly prohibited to minimize the risk of errors.

    6. Naming Conventions
        - Files and resources must follow consistent naming conventions indicating the target environment.
        - Proper naming reduces the risk of accidental modifications to production files.

    7. Approval & Control
        - The CI/CD workflow connects to production only after approval.
        - All deployment controls, including environment restrictions and audit logging, are enforced through the pipeline.


    Responsibilities
    Developers: Follow branching, naming, and environment-specific modification rules. Submit changes via pull requests for review.
    Reviewers: Ensure all changes comply with policy, reject unauthorized production changes, and approve eligible pull requests.
    CI/CD Maintainers: Maintain automated deployment pipelines that enforce approvals, audits, and environment controls.

    Summary
    This policy establishes a predictable, secure, and team-approved workflow: commit → review → automated deployment. It prioritizes automation to reduce risk while supporting efficient development. Manual changes to production are discouraged due to the higher potential for errors.