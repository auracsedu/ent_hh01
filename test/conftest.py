import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def run():
    """run("problem_06", "입력 문자열") -> 출력 줄 리스트 (각 줄 끝 공백은 제거)"""

    def _run(name: str, stdin: str) -> list[str]:
        result = subprocess.run(
            [sys.executable, str(ROOT / f"{name}.py")],
            input=stdin,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            cwd=ROOT,
            timeout=5,
        )
        assert result.returncode == 0, result.stderr
        return [line.rstrip() for line in result.stdout.rstrip().splitlines()]

    return _run
