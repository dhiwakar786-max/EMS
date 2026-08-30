# EMS Frontend (React + Vite)

React 19 UI for the Employee Management System FastAPI backend.

## Run

Backend (from repo root):

```bash
source .venv/bin/activate
uvicorn app.main:app --reload --port 8001
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Open http://127.0.0.1:5173

Vite proxies `/api` and `/health` to `http://127.0.0.1:8001`.
