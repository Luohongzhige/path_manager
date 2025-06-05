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
        root_dir: Optional[str | Path] = None,
        fresh_temp: bool = True,
    ):
        if root_dir is not None:
            root_dir = Path(root_dir).expanduser().resolve()
            proj_root = self._find_work_root(root_dir)
        else:
            caller_dir = self._caller_dir()
            proj_root = self._find_work_root(caller_dir)
        
        self.PROJ_PATH = proj_root
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
        self._announce(proj_root.name)


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

    def _find_work_root(self, start_path: Path) -> Path:
        """从 start_path 开始向上查找 work 目录，返回 work 目录的父目录（即项目主目录）"""
        cur = start_path.resolve()
        while cur != cur.parent:
            if cur.name == "work":
                return cur.parent
            cur = cur.parent
        raise RuntimeError(f"未能从 {start_path} 向上找到 work 目录，请确认代码放在项目 work 目录下或其子目录！")
