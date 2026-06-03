# Backend Automation Platform

**Technologies:** Python AsyncIO, FastAPI, PostgreSQL, Docker, GitHub API, Qdrant

## Overview

A modular automation framework designed to map codebase dependencies and assist engineering teams in identifying structural logic changes across repositories. The platform features an event-driven workflow integration that streams live execution statuses, improving and delivering automated tracking documentation to team stakeholders.

## Key Features

- **Dependency Mapping**: Analyze and visualize codebase dependencies across multiple repositories
- **Change Detection**: Identify structural logic changes and their impact on dependent components
- **Event-Driven Workflows**: Real-time execution status streaming and automation tracking
- **Documentation Generation**: Automated tracking and documentation delivery for stakeholders
- **Vectorized Search**: Leverage Qdrant for semantic code analysis and similarity matching
- **GitHub Integration**: Native GitHub API integration for repository analysis

## Architecture

### Core Components

1. **Dependency Mapper** (`src/dependency_mapper/`): Analyzes repository structure and identifies dependencies
2. **Change Detector** (`src/change_detector/`): Detects and analyzes structural logic changes
3. **Event Stream** (`src/event_stream/`): Manages real-time event-driven workflows
4. **Documentation Engine** (`src/documentation/`): Generates automated documentation and reports
5. **Vector Store** (`src/vector_store/`): Qdrant integration for semantic analysis
6. **GitHub Integration** (`src/github_api/`): GitHub API client and event handling

## Tech Stack

- **Framework**: FastAPI for high-performance async APIs
- **Concurrency**: Python AsyncIO for non-blocking operations
- **Database**: PostgreSQL for persistent storage
- **Vector Database**: Qdrant for semantic search and embeddings
- **Containerization**: Docker for deployment and scalability
- **API Integration**: GitHub API for repository analysis

## Getting Started

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- PostgreSQL 13+
- GitHub API token

### Installation

1. Clone the repository
2. Copy `.env.example` to `.env` and configure environment variables
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start services using Docker Compose:
   ```bash
   docker-compose up -d
   ```
5. Run database migrations:
   ```bash
   python -m alembic upgrade head
   ```

## API Documentation

Once the server is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Configuration

See `.env.example` for all available configuration options.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
