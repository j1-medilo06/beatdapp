# Repository Standards and Conventions

## Version
**0.0.1**

---
## Overview
This repository follows standardized DevOps practices to ensure consistency, maintainability, and smooth CI/CD automation.

Standardizing the folder structure with three-character environment identifiers improves maintainability, simplifies cleanup processes, and supports environment parameterization in CI/CD workflows.

---
## Folder Structure Standardization
To maintain clarity and enforce consistency, this repository **standardizes environment folders using three-character identifiers**.

---
## Rationale
Using three-character environment identifiers provides the following benefits:
- Improves long-term maintainability
- Simplifies cleanup and decommissioning processes
- Enables reliable environment parameterization in CI/CD pipelines
- Reduces configuration drift across environments

---

## Environment Codes
The following environment codes are used consistently across the repository:

|--------------------------|---------|
| Environment              |  Code   |
|--------------------------|---------|
| Development              |  `dev`  |
| Staging                  |  `stg`  |
| Production               |  `prd`  |
| User Acceptance Testing  |  `uat`  |
|--------------------------|---------|

---
## Comments
- Environment names must follow the three-character standard
- CI/CD pipelines should reference environments via variables (e.g. `ENV=dev`)
- Avoid hardcoding environment-specific values
- Git is the single source of truth for configuration


## Change Log
### 0.0.1
- Introduced standardized three-character environment identifiers
- Improved maintainability and CI/CD parameterization