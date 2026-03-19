# DataOps Pipeline Docker

This project demonstrates how to containerize a data pipeline using Docker. The pipeline ingests, transforms, validates, and processes data, all within a reproducible Docker environment.

## Features
- Modular pipeline structure (ingest, transform, validate)
- Uses Python virtual environment for dependency management
- Pre-commit hooks and linting for code quality
- Example datasets and scripts for testing
- Dockerfile for containerization

## Getting Started
1. **Clone the repository**
2. **Build the Docker image:**
   To create a Docker image for this pipeline, use the following command:
   ```
   docker build -t dataops-pipeline .
   ```
   - `docker build` tells Docker to create an image from the Dockerfile in the current directory.
   - `-t dataops-pipeline` names the image "dataops-pipeline" for easy reference.
   - `.` specifies the build context (the current directory).

   After building, you can list your images with:
   ```
   docker images
   ```
3. **Run the container:**
   ```
   docker run --rm -v $(pwd)/data:/app/data dataops-pipeline
   ```

## Project Structure
- `src/` — Pipeline modules
- `data/` — Raw and processed data
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container build instructions
- `tests/` — Unit tests

## Purpose
This repository is intended as a template for containerizing data pipelines, ensuring reproducibility and portability across environments.

## License
MIT License
