# Financial Document Analyzer – CrewAI Debug Challenge

## Overview

This project is a financial document analysis system built using CrewAI and FastAPI.  
The original codebase contained multiple dependency conflicts, broken imports, tool validation errors, and runtime issues.

My task was to debug the system and make it fully functional.

The system now:

- Accepts financial PDF uploads
- Processes them using CrewAI agents
- Returns analysis via a FastAPI endpoint
- Runs successfully without dependency conflicts

---

## What I Found and Fixed

### 1. Dependency Conflicts

The project initially failed to install due to multiple version conflicts between:

- opentelemetry packages
- pydantic and pydantic-core
- openai versions
- crewai and crewai-tools

Fix:
- Simplified `requirements.txt`
- Removed strict and conflicting version pins
- Rebuilt virtual environment from scratch
- Verified clean installation

---

### 2. CrewAI Import Errors

Error:
ImportError: cannot import name 'Agent'

Cause:
Outdated import structure.

Fix:
Updated imports to:
from crewai import Agent

---

### 3. Tool Validation Errors (Pydantic)

Error:
ValidationError: Input should be a valid dictionary or BaseTool

Cause:
Tools were defined as plain functions/classes instead of CrewAI-compatible tools.

Fix:
- Refactored tools using `@tool` decorator
- Added proper docstrings (required by CrewAI)
- Converted class-based tools into functional format

---

### 4. FastAPI Multipart Error

Error:
Form data requires "python-multipart"

Fix:
Added `python-multipart` to requirements.txt

---

### 5. Indentation & Runtime Errors

- Fixed indentation mismatches
- Removed undefined variables
- Corrected tool imports
- Removed unused search tool

---
### 6. Inefficient Prompt Engineering

The original agent prompts were intentionally designed to:

- Encourage hallucinations

- Generate misleading financial advice

- Ignore user queries

- Produce exaggerated and unreliable outputs

## Problems Identified:

- Agents were instructed to "make up" financial advice

- Prompts promoted hallucinated URLs and fake market facts

- Risk and investment logic was contradictory

- No grounding in actual document content

## Fix Applied:

- Document-based reasoning

- Accurate financial interpretation

- Structured and logical analysis

- Risk-aware investment insights

- Removed hallucination instructions

- Ensured outputs align with user query

- Improved clarity and deterministic behavior

---
## How to Run the Project

### 1. Clone Repository

```
git clone https://github.com/Shivathamme/financial-document-analyzer.git
cd financial-document-analyzer
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Server

```
uvicorn main:app --reload
```

---

## API Documentation

Once running, open:

http://127.0.0.1:8000/docs

FastAPI Swagger UI provides interactive documentation.

---

## API Endpoints

### GET /

Health check endpoint.

---

### POST /analyze

Upload a financial PDF and optional query.

Returns JSON response containing analysis.

---

## Improvements Made

- Clean dependency tree
- Refactored tools properly
- Structured agents and tasks
- Ensured reproducible installation
- Verified project works from fresh environment

---

## Future Enhancements (If Extended)

- Add queue worker model for concurrent requests
- Store analysis results in database
- Improve structured financial extraction

