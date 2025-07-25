# DevSecOps Python App with GCP Deployment

This project includes:

- Python + Flask app
- GitHub Actions DevSecOps pipeline:
  - GitGuardian (Secrets)
  - Semgrep (SAST)
  - pip-audit (SCA)
  - Docker Build + Scan (Trivy)
  - GCP Deploy (Cloud Run)
  - DAST with OWASP ZAP

## 🛠 GitHub Secrets Required:

| Secret Name       | Description |
|-------------------|-------------|
| GCP_SA_KEY         | JSON key of GCP service account |
| GCP_PROJECT_ID     | Your GCP project ID |
| GCP_REGION         | e.g. us-central1 |

Push code to `main` branch to trigger pipeline.
