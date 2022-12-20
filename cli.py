from enum import Enum
from pathlib import Path
import platform
import subprocess
import time

from alembic import command
from alembic.config import Config
import typer as typer


app = typer.Typer()


class ProcessManager(str, Enum):
    uvicorn = "uvicorn"
    gunicorn = "gunicorn"


@app.command()
def make_migrations(message: str = None):
    alembic_cfg = Config(
        Path(__file__).parent.joinpath("alembic.ini").absolute().as_posix()
    )
    command.revision(alembic_cfg, message=message, autogenerate=True)


@app.command()
def migrate(rev_id: str = "head"):
    alembic_cfg = Config(
        Path(__file__).parent.joinpath("alembic.ini").absolute().as_posix()
    )
    command.upgrade(alembic_cfg, rev_id)


@app.command()
def api(
    manager: ProcessManager = ProcessManager.uvicorn,
    port: int = 5000,
    host: str = "127.0.0.1",
    # reload: bool = True,
    # workers: int = 1,
):
    if platform.system() == "Windows" or manager == ProcessManager.uvicorn:
        run_args = [
            ProcessManager.uvicorn,
            "app.main:app",
            "--host",
            f"{host}",
            "--port",
            f"{port}",
            "--reload"
            # f"{reload}",
            # "--workers",
            # f"{workers}",
        ]
        proc = subprocess.Popen(run_args, stdout=None, stderr=subprocess.STDOUT)

        while proc.poll() is None:
            time.sleep(60)
    else:
        run_args = [
            ProcessManager.gunicorn,
            "app.main:app",
            "--bind",
            f"{host}:{port}",
            # "--reload"
            # f"{reload}",
            # "--workers",
            # f"{workers}",
            # "--worker-class",
            # "uvicorn.workers.UvicornWorker",
        ]
        proc = subprocess.Popen(run_args, stdout=None, stderr=subprocess.STDOUT)

        while proc.poll() is None:
            time.sleep(60)


if __name__ == "__main__":
    app()
