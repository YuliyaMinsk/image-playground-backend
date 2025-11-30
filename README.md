# Image Playground Backend

Backend API for AI Image Playground — a sandbox for generating images with AI.

## Features

- Single endpoint for image generation
- Multiple provider support (Stub, Cheap API, Gemini)
- Generation modes: quality, fast, free, animals
- Daily rate limiting
- Cyrillic prompt detection

## Quick Start

### Prerequisites

- Python 3.11+

### Installation
```bash
# Clone repository
git clone https://github.com/YuliyaMinsk/image-playground-backend.git
cd image-playground-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
make install

# Copy environment config
cp .env.example .env

# Run development server
make dev
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/api/generate-image` | Generate image |

## Project Structure
```
src/
├── api/          # FastAPI endpoints
├── providers/    # Image generation providers
├── services/     # Business logic
├── config/       # Configuration
└── utils/        # Utilities
```

## License

MIT