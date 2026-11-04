"""Prepare an uploaded material bundle inside a hosted Google Colab runtime."""

import os
from pathlib import Path
import subprocess
import sys


TOPICS = {
    "00-numpy-pytorch", "01-imitation-learning", "02-policy-gradients",
    "03-actor-critic", "04-model-based-rl", "05-visual-control",
}


def prepare_notebook(root, topic, section):
    """Resolve notebook-relative files and prepare Colab's headless renderer.

    Dependency installation stays in the notebook's pip cell. System package
    installation here runs only for robotics topics in a hosted Colab session.
    """
    if "google.colab" not in sys.modules:
        raise RuntimeError("This helper is for Colab; use docs/ENVIRONMENT.md locally.")
    if topic not in TOPICS or section not in {"exercises", "solutions"}:
        raise ValueError("Choose a topic and either exercises or solutions.")
    root = Path(root).resolve()
    working_dir = root / "assignments" / topic / section
    if not (working_dir / "notebook.ipynb").is_file():
        raise FileNotFoundError("Upload the complete basicrl-study.zip material bundle.")
    if not (root / "requirements" / "basics.txt").is_file():
        raise FileNotFoundError("The uploaded material bundle is incomplete.")

    os.chdir(working_dir)
    working_path = str(working_dir)
    if working_path in sys.path:
        sys.path.remove(working_path)
    sys.path.insert(0, working_path)
    # A learner may switch between exercise and solution notebooks in one VM.
    # Resolve these modules from the newly selected directory on the next import.
    for module in ("q1", "q2"):
        sys.modules.pop(module, None)

    if topic != "00-numpy-pytorch":
        backend = os.environ.setdefault("MUJOCO_GL", "osmesa")
        if backend in {"osmesa", "egl"}:
            os.environ["PYOPENGL_PLATFORM"] = backend
        marker = root.parent / ".basicrl-colab-system-ready"
        if not marker.is_file():
            subprocess.run(["apt-get", "-qq", "update"], check=True)
            subprocess.run(
                ["apt-get", "-qq", "install", "-y", "libosmesa6", "libegl1",
                 "libgl1", "libglfw3", "ffmpeg"], check=True,
            )
            marker.touch()
        print(f"MuJoCo renderer: {backend} (set before importing MuJoCo)")

    print(f"Working directory: {working_dir}")
    print(f"Python: {sys.version.split()[0]}")
    print("Next: run the dependency-install cell, then continue from top to bottom.")
