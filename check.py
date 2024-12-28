from pathlib import Path
import subprocess
import logging
import sys

SCRIPT_DIR = Path(__file__).parent
LOGGER = logging.getLogger(__name__)


def _find_python_files() -> list[Path]:
    return list(SCRIPT_DIR.glob("day*/*.py")) + [Path(__file__)]


def _run(name: str, cmd: list[str]) -> bool:
    LOGGER.info(f"*** Running {name} ***")
    try:
        subprocess.run(cmd, check=True, text=True, capture_output=True)
        LOGGER.info(f"{name} OK")
        return True
    except subprocess.CalledProcessError as exc:
        LOGGER.error(f"{name} fail code {exc.returncode}")
        LOGGER.error(exc.output)
        return False


def _pytest() -> bool:
    cmd = ["pytest"]
    return _run("pytest", cmd)


def _pylint(python_files: list[Path]) -> bool:
    cmd = ["pylint"] + [str(p) for p in python_files]
    return _run("pylint", cmd)


def _mypy(python_files: list[Path]) -> bool:
    cmd = ["mypy", "--strict"] + [str(p) for p in python_files]
    return _run("mypy", cmd)


def main() -> int:
    logging.basicConfig(level=logging.INFO)
    python_files = _find_python_files()
    check_results = [_pytest(), _pylint(python_files), _mypy(python_files)]
    return 0 if all(check_results) else 1


if __name__ == "__main__":
    sys.exit(main())
