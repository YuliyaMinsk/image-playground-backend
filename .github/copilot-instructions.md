**Project:** Image Playground Backend
**Purpose:** FastAPI-based backend for AI image generation playground. Provides a unified API for image generation through multiple providers (Stub, Cheap API, Gemini) with configurable modes, rate limiting, and prompt validation.


## 1. Project Overview

* **Runtime:** Python 3.11+

* **Framework:** FastAPI + uvicorn (ASGI server)

* **Entry point:** `src/main.py` (FastAPI app)

* **Project structure:**

  * `src/api/` — FastAPI routes (`/health`, `/api/generate-image`)
  * `src/providers/` — image generation providers (Stub, Cheap, Gemini)
  * `src/services/` — business logic (rate limiting, prompt validation, provider orchestration)
  * `src/config/` — configuration and settings
  * `src/utils/` — utilities (cyrillic detection, logging helpers)
  * `tests/` — pytest test suite

* **Configuration via `.env`:**

  * `IMAGE_PROVIDER_MODE` — provider selection: `stub | cheap | nano`
  * `DAILY_LIMIT` — requests per day
  * `PROMPT_LANGUAGE_MODE` — cyrillic handling: `strict | warn | ignore`
  * `HOST`, `PORT` — server binding

* **Dependencies (pyproject.toml):**

  * Runtime: `fastapi`, `uvicorn[standard]`, `python-dotenv`
  * Dev: `ruff`, `pytest`

* **Generation modes:**

  * `quality`, `fast`, `free`, `animals` — mapped to provider capabilities and behavior.

---

## 2. Coding Rules & Guardrails

**Never modify without explicit request:**

* `.env` and environment variable schema
* `pyproject.toml` (dependencies, project metadata)
* Core structure of `src/` (no new top-level folders)
* API keys or secrets

**General coding standards:**

* Use **type hints everywhere** (Python 3.11+ style, explicit return types).
* Endpoints must be `async def`.
* Use **Pydantic models** for all request/response schemas.
* Keep endpoints thin: business logic belongs in `src/services/`.
* Use **dependency injection** for services/config.
* No hardcoded provider names, limits or modes — always read from config/env.
* Run `ruff` and keep functions small, focused and readable.
* Comments in **English**, docstrings and README in **English**.


## 3. Git Workflow

* Branches: `main` (stable), `develop` (active), `feature-*`, `fix-*`.
* Commit prefixes: `feat:`, `fix:`, `doc:`, `refactor:`.
* Do **not** commit directly to `main` unless explicitly requested.


## 4. Copilot / Chat Interaction: “Architect First”

**Default rule:**
Do **not** generate code by default. Start with reasoning.

When asked for a change, feature, refactor, test or script:

### Step 1 — Analysis

Provide **short, structured reasoning**:

* **Idea:** what should be done
* **Why:** purpose / value
* **Alternatives:** 2–3 options where meaningful
* **Trade-offs:** risks and downsides
* **When to choose each option**

(Keep it concise, not an essay.)

### Step 2 — Plan

Provide a brief plan (no code):

* Approach step-by-step
* Expected components
* Affected files/dirs
* Dependency impact (if any)

### Step 3 — Ask for Approval

Always end with a direct question, e.g.:

* “Should I implement option A, B or C?”
* “Do you want me to generate the code for this plan?”

Only generate code after explicit approval like:
`approve`, `yes`, `go ahead`, `generate`, `implement`, `давай`, `да`.

### Step 4 — Restricted actions

Do **not** perform the following without explicit permission:

* Full rewrites of core modules (`src/main.py`, providers in `src/providers/`)
* Architectural changes (new database, GraphQL, major refactors)
* Adding Docker/CI/CD/Kubernetes configs
* Changing `pyproject.toml` dependencies or adding new packages
* Creating new top-level directories or changing project layout
* Changing `.env` schema (adding/removing vars, changing semantics)
* Adding authentication/authorization layers (JWT, OAuth, etc.)
* Introducing caching layers (Redis, Memcached, etc.)


## 5. Testing Guidelines

* Use **pytest** as the testing framework.
* Use FastAPI `TestClient` for API tests.
* **Mock external providers** to avoid:

  * Real API calls
  * Rate limiting issues
  * Paid usage

**Test structure:**

* `tests/test_api.py` — endpoint tests (status, validation, error responses)
* `tests/test_services.py` — services (rate limiting, prompt validation, provider selection)
* `tests/test_providers.py` — provider interface tests (mocked responses)

Focus on:

* JSON response structure
* Correct HTTP status codes (200, 400, 429, 500)
* Proper handling of invalid input and rate-limit scenarios.


## 6. API & Domain Rules

**Endpoints:**

* Use `POST` for image generation (`/api/generate-image`).
* Use `GET /health` for health checks.
* Status codes:

  * `200` — success
  * `400` — bad request / invalid input
  * `429` — rate limit exceeded
  * `500` — internal provider/system error
* Include clear, machine-readable error messages in JSON body.

**Provider pattern:**

* All providers implement a **common interface** (same method signatures).
* Provider selected via `IMAGE_PROVIDER_MODE`.
* Prefer graceful fallback (e.g. to stub) if main provider fails, when appropriate.

**Rate limiting:**

* Count requests per day in service layer.
* On exceed: return `429` with clear error payload.
* Reset logic is daily (implementation details can be discussed before coding).

**Prompt validation:**

* Detect cyrillic characters in prompts.
* Behavior via `PROMPT_LANGUAGE_MODE`:

  * `strict` — reject cyrillic (`400` + explanation)
  * `warn` — accept, log a warning and/or include warning in response
  * `ignore` — no validation


## 7. Output Style

* Default flow: **analysis → plan → question → (optional) code**.
* Generate code **only after explicit approval**.
* Use **English** for comments, docstrings, and documentation.
* Keep comments minimal but meaningful; add more only when explanation is requested.
* Ask for clarification if unsure about:

  * Provider behavior / priorities
  * Expected API response format
  * Rate limit strategy details
  * Environment variable naming, defaults, or semantics


## 8. Goal

Treat this project as an **AI engineering collaboration**, not auto-completion:

* Propose thoughtful API and provider designs.
* Do not introduce infrastructure (Docker, Kubernetes, monitoring, DBs, queues) unless explicitly requested.
* Avoid over-engineering; focus on small, safe, incremental changes.
* Respect working code and configuration — improve, do not break.
* Be security-conscious: never expose API keys and always validate inputs.
