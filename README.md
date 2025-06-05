# path_manager

A unified project directory helper with smart detection and folder creation.

```python
from path_manager_qiaoy import ProjectPath
PATH = ProjectPath()
PATH.init()
print(PATH.DATA_PATH)
```

---

## Usage
- Automatically detects the project root.
- Creates `work/`, `data/`, `log/`, `temp/` folders under your project root.

---
# Download and Install

use `pip install -i https://test.pypi.org/simple/ path-manager-qiaoy` to download the lastest version from TestPyPI.

run `proj init {your_proj_name}` to init a project

# === LICENSE ===
MIT License
