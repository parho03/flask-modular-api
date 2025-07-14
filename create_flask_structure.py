import os

# 🔧 Set your project name here
base_path = "flask_modular_api_template"

# 🧩 Example module names (customize these)
modules = [
    "authentication",
    "billing",
    "notifications"
]

# 🚦 Set architecture mode: "services" for native Python logic,
# or "bridge" for cross-language integration (e.g., Rust, C++)
architecture_mode = "services"  # or "bridge"

# 📁 Base structure
structure = {
    "api.ini": "",
    "run.py": "",
    "wsgi.py": "",
    "requirements.txt": "",
    "README.md": "",
    "app/__init__.py": "",
    "app/config.py": "",
    "app/routes.py": "",
    "app/errors.py": "",
    "app/middleware.py": "",
    "app/utils/__init__.py": "",
    "app/utils/response.py": "",
    "app/utils/security.py": "",
    "app/utils/jwt_helpers.py": "",
    "app/models/__init__.py": "",
    "app/models/user.py": "",
    "app/schemas/__init__.py": "",
    "app/resources/__init__.py": "",
    "app/decorators/__init__.py": "",
    "app/decorators/token_validation.py": "",
    "app/decorators/payload_verification.py": "",
    "tests/__init__.py": "",
    "tests/test_auth.py": "",
}

# 🔄 Add resource files for each module
for module in modules:
    structure[f"app/resources/{module}.py"] = f"# API endpoints for {module}\n"

# 🔁 Depending on mode, add either service or bridge structure
if architecture_mode == "services":
    structure["app/services/__init__.py"] = ""
    for module in modules:
        structure[f"app/services/{module}/__init__.py"] = f"# {module.title()} service logic\n"

elif architecture_mode == "bridge":
    structure["app/bridge/__init__.py"] = ""
    for module in modules:
        structure[f"app/bridge/{module}/__init__.py"] = f"# {module.title()} bridge logic\n"
        structure[f"app/bridge/{module}/{module}_rust_bridge.py"] = f"# Rust bridge for {module}\n"

else:
    raise ValueError("❌ Invalid architecture_mode. Choose 'services' or 'bridge'.")

# 🏗 Create directories and files
for path, content in structure.items():
    full_path = os.path.join(base_path, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Project scaffold created at ./{base_path}/ using '{architecture_mode}' mode.")
