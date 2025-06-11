# Setup Instructions for PyPI Publishing

## Prerequisites

1. **PyPI Account**: You need a PyPI account at https://pypi.org/
2. **PyPI API Token**: Generate an API token from your PyPI account settings
3. **GitHub Repository**: Push this code to a GitHub repository

## Configuration Steps

### 1. Create PyPI API Token

1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name it something like "omar6995-browserforge-github-actions"
4. Set the scope to "Entire account" (or specific to this project once it's published)
5. Copy the generated token (it starts with `pypi-`)

### 2. Configure GitHub Repository Secrets

1. Go to your GitHub repository
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Create a secret named `PYPI_API_TOKEN` with the value being your PyPI API token

### 3. Publish to PyPI

1. Go to your GitHub repository
2. Navigate to Actions tab
3. Find the "Publish to PyPI" workflow
4. Click "Run workflow"
5. Optionally specify a version (e.g., "1.2.4") or leave empty to use the current version in pyproject.toml
6. Click "Run workflow"

## Package Details

- **Package Name**: `omar6995-browserforge`
- **Current Version**: 1.2.3 (as specified in pyproject.toml)
- **Installation**: Once published, users can install with `pip install omar6995-browserforge`

## Local Testing

Before publishing, you can test the package locally:

```bash
# Install Poetry if you don't have it
pip install poetry

# Install dependencies
poetry install

# Build the package
poetry build

# Check the built package
poetry run twine check dist/*
```

## Notes

- The workflow will automatically create a GitHub release when publishing succeeds
- You can specify a new version during manual trigger, or it will use the version in pyproject.toml
- Make sure to update the version in pyproject.toml before publishing if you want to increment it
