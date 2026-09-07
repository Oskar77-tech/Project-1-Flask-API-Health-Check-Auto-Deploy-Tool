# API Health Check & Automated Deployment Tool

A DevOps project that automatically deploys a Flask-based API to a Linux server using GitLab CI/CD, Docker and SSH automation.

## Features

- Automated deployment with GitLab CI/CD
- Docker-based application deployment
- SSH remote deployment
- Health check endpoint validation
- Automatic container replacement during deployment
- Linux server automation

## Tech Stack

- Python
- Flask
- Docker
- GitLab CI/CD
- Linux
- SSH

## Architecture

```text
Git Push
    ↓
GitLab CI/CD
    ↓
SSH Deployment
    ↓
Docker Build
    ↓
Container Restart
    ↓
Health Check Validation
```

## API Endpoints

### GET /

Returns application status.

Example response:

```json
{
  "service": "API Health Check",
  "status": "running"
}
```

### GET /health

Returns the current health status.

Example response:

```json
{
  "status": "healthy"
}
```

## CI/CD Workflow

1. Developer pushes changes to GitLab
2. GitLab CI/CD pipeline starts automatically
3. Runner connects to the deployment server via SSH
4. Repository is updated using `git pull`
5. Docker image is rebuilt
6. Existing container is stopped and replaced
7. Health check endpoint is validated

## Required CI/CD Variables

The following GitLab CI/CD variables are required:

- DEPLOY_HOST
- DEPLOY_USER
- DEPLOY_PATH
- SSH_PRIVATE_KEY

## Challenges Solved

During development I solved several real-world DevOps challenges:

- SSH key authentication between GitLab Runner and deployment server
- Automated Docker deployments
- Docker container lifecycle management
- Linux troubleshooting and debugging
- Port conflict resolution
- Health check verification after deployment

## Future Improvements

- Multi-target health checks
- Prometheus metrics integration
- Slack or Microsoft Teams notifications
- Docker Registry integration
- Kubernetes deployment

## Author

Oskar Staudacher
