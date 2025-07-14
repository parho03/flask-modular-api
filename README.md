# Flask Modular API Structure with Optional Bridge Layer

## 🧩 Overview

This is a scalable and modular **Flask API boilerplate** built for production-ready backend services.  
It features clean separation of concerns, modular architecture, and optional multi-language support via a `bridge/` layer.

---

## 🔄 Key Architectural Layers

| Folder        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `resources/`  | Handles HTTP endpoints (controllers)                                        |
| `services/`   | Core business logic (pure Python)                                           |
| `bridge/`     | Interfaces with external non-Python modules (e.g., Rust, C++ via FFI/PyO3) |
| `models/`     | SQLAlchemy or data models                                                   |
| `schemas/`    | Marshmallow (or other) input/output validators                              |
| `utils/`      | Reusable helper utilities (JWT, hashing, etc.)                              |
| `decorators/` | Request validation, token enforcement                                       |
| `middleware.py` | Custom request/response middleware                                       |
| `errors.py`   | Centralized error handling                                                  |

---

## 📁 Folder Structure

```
flask-api-structure/
├── app/
│   ├── services/                     # ✅ Business logic (pure Python)
│   │   └── authentication/
│   │       └── __init__.py
│
│   ├── bridge/                       # 🛠 Interface to non-Python logic (e.g., Rust)
│   │   └── rust_crypto/
│   │       └── __init__.py          # e.g., wrapped Rust module using PyO3/cffi
│
│   ├── decorators/                  # 🔐 Custom decorators (auth, validation)
│   │   ├── __init__.py
│   │   ├── token_validation.py
│   │   └── payload_verification.py
│
│   ├── models/                      # 🧬 SQLAlchemy or data models
│   │   ├── __init__.py
│   │   └── user.py
│
│   ├── resources/                   # 🌐 API endpoints (Flask routes)
│   │   ├── __init__.py
│   │   └── authentication.py
│
│   ├── schemas/                     # ✅ Marshmallow schemas for validation
│   │   └── __init__.py
│
│   ├── utils/                       # 🧰 Utility functions (JWT, responses)
│   │   ├── __init__.py
│   │   ├── jwt_helpers.py
│   │   ├── response.py
│   │   └── security.py
│
│   ├── __init__.py
│   ├── config.py                   # ⚙️ Environment/config management
│   ├── errors.py                   # ❗ Error handlers
│   ├── middleware.py               # 🔄 Middleware hooks
│   └── routes.py                   # 📍 Route registration
│
├── tests/                           # 🧪 Unit tests
│   ├── __init__.py
│   └── test_auth.py
│
├── api.ini                          # 🔧 Config file
├── requirements.txt                 # 📦 Python dependencies
├── run.py                           # 🚀 Dev server runner
├── wsgi.py                          # 🌀 WSGI entry for production (gunicorn)
└── README.md                        # 📘 This file
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-api-structure.git
cd flask-api-structure
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python run.py
```

### 5. Run with Gunicorn (Production)

```bash
gunicorn wsgi:app
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 🔐 Security Features

- JWT Token Validation
- Request Payload Verification
- Token-based route protection using decorators

You can customize the logic in:
- `app/utils/jwt_helpers.py`
- `app/decorators/token_validation.py`
- `app/decorators/payload_verification.py`

---

## 🧠 When to Use `services/` vs `bridge/`

| Folder       | Use it for...                                                       |
|--------------|----------------------------------------------------------------------|
| `services/`  | Business logic entirely in Python (e.g., auth, DB operations, etc.) |
| `bridge/`    | Wrapping/using Rust, C++, Go modules with `cffi`, `ctypes`, `PyO3`, etc. |

If you're not integrating other languages, ignore `bridge/` and put logic in `services/`.

---

## 📚 License

MIT License. Use freely, modify, and contribute.

---

## 🧱 Future Extensions

- Add `Dockerfile` and `docker-compose.yml`
- Support Swagger/OpenAPI auto-documentation
- Add GitHub Actions CI/CD
