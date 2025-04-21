# file: project_path.py
import os
import inspect
import shutil
from pathlib import Path
from typing import Optional


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"


class ProjectPath:

    def __init__(self):
        self._ready = False

    def init(
        self,
        project: Optional[str] = None,
        root_dir: Optional[str | Path] = None,
        fresh_temp: bool = True,
    ):
        caller_root = self._caller_dir()
        project = project or caller_root.name
        root_dir = Path(root_dir).expanduser().resolve() if root_dir else caller_root

        self.PROJ_PATH = Path(root_dir).expanduser().resolve().parent
        self.WORK_PATH = self.PROJ_PATH / "work"
        self.DATA_PATH = self.PROJ_PATH / "data"
        self.TEMP_PATH = self.PROJ_PATH / "temp"
        self.LOG_PATH = self.PROJ_PATH / "log"
        self.LLM_PATH = Path("~/LLM").expanduser().resolve()

        for p in (self.WORK_PATH, self.DATA_PATH, self.LOG_PATH):
            p.mkdir(parents=True, exist_ok=True)
        if fresh_temp and self.TEMP_PATH.exists():
            shutil.rmtree(self.TEMP_PATH)
        self.TEMP_PATH.mkdir(exist_ok=True)

        self._ready = True
        self._announce(project)

    def _caller_dir(self) -> Path:
        this_file = Path(__file__).resolve()
        for frame in inspect.stack():
            fpath = Path(frame.filename).resolve()
            if fpath != this_file:
                return fpath.parent
        return Path.cwd()

    def _announce(self, proj_name: str):
        c = Color
        print(f"{c.RED}{'-'*60}{c.END}")
        print(f"Path initialized for {c.GREEN}{proj_name}{c.END}")
        for attr in ("PROJ", "WORK", "DATA", "TEMP", "LOG", "LLM"):
            print(f"{attr:<5}: {c.BLUE}{getattr(self, attr+'_PATH')}{c.END}")
        print(f"{c.RED}{'-'*60}{c.END}")

    def __getattr__(self, item):
        if not self._ready:
            raise RuntimeError("Call PATH.init(...) before using any attributes.")
        if item in self.__dict__:
            return self.__dict__[item]
        raise AttributeError(item)


# 单例
PATH = ProjectPath()