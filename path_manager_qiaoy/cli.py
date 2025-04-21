import sys, os
from pathlib import Path

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "init":
        print("Usage: proj init {proj_name}")
        sys.exit(1)

    proj_name = sys.argv[2]
    base_path = Path.cwd() / proj_name
    work_path = base_path / "work"
    start_py = work_path / "start.py"

    try:
        work_path.mkdir(parents=True, exist_ok=False)
        with open(start_py, 'w') as f:
            f.write('from path_manager_qiaoy import PATH\n')
            f.write('PATH.init()\n')
        print(f"✅ Project '{proj_name}' initialized at {base_path}")
        print(f"📝 Created: {start_py}")
        #run the start.py script
        os.system(f"python {start_py}")
        print(f"Run the script with: python {start_py}")
    except FileExistsError:
        print(f"⚠️ Project '{proj_name}' already exists at {base_path}")
