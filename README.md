# IAM Provisioning Workflows

Automated identity lifecycle workflows triggered by HR system events (hire, transfer, termination).
Integrates with Saviynt EIC for provisioning orchestration across enterprise applications.

## Overview

This repository contains workflow definitions and provisioning scripts that handle:
- **Joiner** – Account creation, role assignment, and access provisioning on Day 1
- **Mover** – Role recertification and access adjustment on internal transfers
- **Leaver** – Immediate deprovisioning and access revocation on termination

## Tech Stack
- Python 3.11
- Saviynt REST API
- Workday HR System (event source)
- ServiceNow (ticketing integration)

## Folder Structure
```
workflows/
  joiner/   – New hire provisioning logic
  mover/    – Transfer and role change handlers
  leaver/   – Offboarding and deprovisioning
config/     – Environment-specific settings
tests/      – Unit and integration tests
```

## Team Owners
| Role | Team |
|---|---|
| Platform Engineering | @boston-code/iam-platform |
| Security & Compliance | @boston-code/security |

## Getting Started
```bash
pip install -r requirements.txt
cp config/settings.example.yml config/settings.yml
python workflows/joiner/provision.py --env staging
```
