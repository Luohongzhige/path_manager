# path_manager

A unified project directory helper with smart detection and folder creation.

```python
from path_manager import PATH
PATH.init()
print(PATH.DATA)
```

---

## Usage
- Automatically detects the project root.
- Creates `work/`, `data/`, `log/`, `temp/` folders under your project root.

---

## Release
Push a tag like `v0.1.0` to trigger a release build:

```bash
git tag v0.1.0
git push origin v0.1.0
```

The GitHub Action will build and attach a `.whl` and `.tar.gz` to the release.

# === LICENSE ===
MIT License
