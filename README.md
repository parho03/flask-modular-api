# Flask Modular API Template

A scalable and modular Flask API architecture that supports clean separation of concerns through **service-oriented** or **cross-language bridge-based** modules. This boilerplate is ideal for projects that need flexibility, security, and maintainability — whether fully Python-based or integrating with external languages like **Rust**, **Go**, or **C++**.

---

## 📁 Project Structure

> The structure varies based on the selected `architecture_mode` — either `"services"` (pure Python logic) or `"bridge"` (external integrations).

<details>
<summary><strong>🧩 Common Structure</strong></summary>

```plaintext
flask_modular_api_template/
├── app/
│   ├── resources/                  # HTTP endpoint logic
│   ├── decorators/                # Custom decorators (e.g., token checks)
│   ├── models/                    # SQLAlchemy models
│   ├── schemas/                   # Data validation & serialization (e.g., Marshmallow)
│   ├── utils/                     # Reusable utility functions
│   ├── config.py                  # Configuration setup
│   ├── errors.py                  # Global error handlers
│   ├── middleware.py              # Middleware logic
│   ├── routes.py                  # Blueprint registration
│   └── __init__.py
├── tests/                         # Unit/integration tests
├── api.ini                        # Configuration file
├── requirements.txt               # Dependencies
├── run.py                         # Dev server entrypoint
├── wsgi.py                        # WSGI production entrypoint
└── README.md
```

</details>

---

<details>
<summary><strong>🛠️ If <code>architecture_mode = "services"</code></strong></summary>

```plaintext
app/
└── services/                      # Pure Python logic layer
    ├── authentication/
    │   └── __init__.py
    ├── billing/
    │   └── __init__.py
    └── notifications/
        └── __init__.py
```

</details>

<details>
<summary><strong>🔗 If <code>architecture_mode = "bridge"</code></strong></summary>

```plaintext
app/
└── bridge/                        # External logic via FFI (e.g., Rust/C++)
    ├── authentication/
    │   ├── __init__.py
    │   └── authentication_rust_bridge.py
    ├── billing/
    │   ├── __init__.py
    │   └── billing_rust_bridge.py
    └── notifications/
        ├── __init__.py
        └── notifications_rust_bridge.py
```

</details>

---

## 🚀 Quick Start

### 1. Generate Project Structure

Use the included Python script to generate the scaffold:

```bash
python scaffold_api.py
```

Inside `scaffold_api.py`, configure the following:

```python
base_path = "your_project_name"
modules = ["authentication", "billing", "notifications"]
architecture_mode = "services"  # or "bridge"
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Development Server

```bash
python run.py
```

---

## 🧪 Testing

```bash
pytest
```

---

## 🧱 Technologies Used

- **Flask** — Python web framework
- **JWT** — Authentication (optional)
- **Modular Design** — Clean, pluggable modules
- **Optional Rust Integration** — For performance-critical logic
- **Pytest** — Testing framework

---

## 🧠 Naming Convention Tips

- Use `services/` for native, testable Python business logic.
- Use `bridge/` for FFI bindings (Rust, Go, etc.) via tools like `PyO3`, `ctypes`, or `cffi`.

You **should not** use both at once — choose based on your project needs.

---

## 📦 Repository Name Suggestion

**`flask-modular-api-template`**

> Cleanly separates web, logic, and optional FFI bridges for secure, extensible backends.

---

## 📜 License

MIT © YourNameHere
