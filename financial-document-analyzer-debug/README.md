#  Financial Document Analyzer – CrewAI Debug Challenge

##  Project Overview

This project is a fully debugged and refactored Financial Document Analyzer system built using:

- FastAPI (API layer)
- CrewAI (multi-agent orchestration)
- OpenAI (LLM)
- LangChain PDF Loader
- Python

The system accepts financial PDF documents, processes them through a multi-agent CrewAI pipeline, and generates structured financial insights.

This submission focuses on identifying, debugging, and fixing major architectural and dependency issues in the original codebase.

---

#  System Architecture

User Upload → FastAPI → CrewAI Crew → Agents → Tools → Response

### Components:

- **FastAPI Backend**
  - Handles file upload and query input
  - Exposes REST API endpoints

- **CrewAI Crew**
  - Sequential execution process
  - Financial Analyst Agent

- **Custom Tools**
  - PDF Reader Tool
  - Investment Analysis Tool
  - Risk Assessment Tool

---

#  Bugs Identified & Fixed

## 1️⃣ Dependency Conflicts

### Problem:
- Conflicts between:
  - opentelemetry versions
  - pydantic-core versions
  - openai package versions
  - crewai and crewai-tools

### Fix:
- Removed strict version pinning where unnecessary
- Simplified requirements.txt
- Removed incompatible telemetry packages
- Rebuilt environment from scratch

---

## 2️⃣ CrewAI Import Errors

### Problem:
```
ImportError: cannot import name 'Agent'
```

### Fix:
- Updated imports to match latest CrewAI structure
- Used `from crewai import Agent`

---

## 3️⃣ Tool Validation Errors (Pydantic)

### Problem:
```
ValidationError: tools.0 Input should be a valid dictionary or BaseTool
```

### Fix:
- Refactored tools to use `@tool` decorator
- Ensured each tool includes proper docstrings
- Converted class-based tools into functional tools

---

## 4️⃣ Missing python-multipart Error

### Problem:
```
Form data requires "python-multipart"
```

### Fix:
- Added `python-multipart` to requirements.txt

---

## 5️⃣ Indentation & Runtime Errors

- Fixed indentation mismatches
- Removed outdated tool references
- Corrected variable naming issues
- Removed undefined objects

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Shivathamme/financial-document-analyzer.git
cd financial-document-analyzer
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

# 📡 API Documentation

Once server is running, open:

```
http://127.0.0.1:8000/docs
```

FastAPI Swagger UI provides interactive API documentation.

---

# 🔌 API Endpoints

## GET /

Health check endpoint.

### Response:
```json
{
  "message": "Financial Document Analyzer API is running"
}
```

---

## POST /analyze

Upload financial document and optional query.

### Form Data:
- file (PDF)
- query (optional text)

### Response:
```json
{
  "status": "success",
  "analysis": "...",
  "file_processed": "filename.pdf"
}
```

---

# 🏗 Improvements Made Beyond Bug Fixes

- Refactored tools into proper CrewAI-compliant structure
- Cleaned dependency tree
- Rebuilt environment cleanly
- Ensured reproducible installation
- Structured project for clarity

---

# 🔐 Security Considerations

- No API keys stored in repository
- .env excluded via .gitignore
- venv excluded from version control


  