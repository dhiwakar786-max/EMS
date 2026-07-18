# Employee Management System — FastAPI layered boilerplate

Structure only. No business logic implemented.

```
app/
├── main.py
├── core/
│   └── config.py                    # settings
│
├── presentation/                    # HTTP layer
│   ├── dependencies.py              # FastAPI Depends wiring
│   ├── schemas/                     # request / response DTOs
│   └── api/v1/                      # controllers (routes)
│
├── application/                     # Application layer
│   └── services/                    # use cases (EmployeeService, …)
│
├── domain/                          # Domain layer
│   ├── entities/                    # business objects
│   └── exceptions.py                # domain errors
│
└── infrastructure/                  # technical adapters
    ├── database/                    # engine / session
    └── models/                      # SQLAlchemy ORM models
```

## Flow

```
HTTP → presentation → application → domain
                         ↓
                   infrastructure (ORM / DB)
```

- **Domain**: entities + rules only  
- **Application**: use cases; uses `Session` + ORM models, returns domain entities  
- **Presentation**: routes + Pydantic schemas; calls application services  

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```
