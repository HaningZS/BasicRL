<h1 align="center">BasicRL</h1>

<p align="center"><strong>Learn reinforcement learning by building, from tensors to visual control.</strong></p>

<p align="center">6 topics · 12 notebooks · 6 solution PDFs / 20 pages · Optional Colab setup</p>

<div align="center">

[简体中文](README.zh-CN.md) · **English**

[Learning path](#learning-path) · [Quick start](#quick-start) · [Theory reference](#theory-reference) · [Colab guide · 中文](docs/COLAB.md) · [Documentation](docs/README.md) · [MIT](LICENSE)

</div>

BasicRL is a collection of reinforcement learning exercises and worked solutions for independent study. Start with NumPy and PyTorch, then explore imitation learning, policy gradients, actor-critic methods, world models, and visual control. Each topic keeps its exercises, implementations, and derivations together so you can try a problem before comparing approaches.

| Build | Understand | Compare |
| :--- | :--- | :--- |
| Notebooks with implementation tasks | PDF solutions with assumptions and intermediate steps | Reference notebooks and editable LaTeX sources |

## Learning path

Follow the six topics in order, or start with a familiar subject. Notebooks, theory questions, and worked solutions are in English. Navigation is available in English and Chinese.

| Topic | What you will learn | Resources |
| :--- | :--- | :--- |
| **00 · [NumPy & PyTorch](assignments/00-numpy-pytorch/README.md)** | Tensor shapes, image assembly, linear regression, and checkpoints | [Exercise](assignments/00-numpy-pytorch/exercises/notebook.ipynb) · [Code](assignments/00-numpy-pytorch/solutions/notebook.ipynb) · [PDF](assignments/00-numpy-pytorch/solutions/solutions.pdf) |
| **01 · [Imitation Learning](assignments/01-imitation-learning/README.md)** | BC, DAgger, distribution shift, and discounted costs | [Exercise](assignments/01-imitation-learning/exercises/notebook.ipynb) · [Code](assignments/01-imitation-learning/solutions/notebook.ipynb) · [PDF](assignments/01-imitation-learning/solutions/solutions.pdf) |
| **02 · [Policy Gradients](assignments/02-policy-gradients/README.md)** | REINFORCE, reward-to-go, baselines, and reward shaping | [Exercise](assignments/02-policy-gradients/exercises/notebook.ipynb) · [Code](assignments/02-policy-gradients/solutions/notebook.ipynb) · [PDF](assignments/02-policy-gradients/solutions/solutions.pdf) |
| **03 · [Actor-Critic](assignments/03-actor-critic/README.md)** | Value baselines, DDPG, SAC, and approximate policy improvement | [Exercise](assignments/03-actor-critic/exercises/notebook.ipynb) · [Code](assignments/03-actor-critic/solutions/notebook.ipynb) · [PDF](assignments/03-actor-critic/solutions/solutions.pdf) |
| **04 · [Model-Based RL](assignments/04-model-based-rl/README.md)** | PPO, world models, model error, and data aggregation | [Exercise](assignments/04-model-based-rl/exercises/notebook.ipynb) · [Code](assignments/04-model-based-rl/solutions/notebook.ipynb) · [PDF](assignments/04-model-based-rl/solutions/solutions.pdf) |
| **05 · [Visual State Estimation & Control](assignments/05-visual-control/README.md)** | CNN state estimation, estimated-state control, and image policies | [Exercise](assignments/05-visual-control/exercises/notebook.ipynb) · [Code](assignments/05-visual-control/solutions/notebook.ipynb) · [PDF](assignments/05-visual-control/solutions/solutions.pdf) |

## Theory reference

For an introductory theory reference, read [Modern Adaptive Control and Reinforcement Learning (MACRL)](https://macrl-book.github.io/assets/pdf/macrl.pdf) alongside these exercises. Use the book to build intuition and connect the hands-on implementations to the underlying mathematical ideas.

## Quick start

### Run in Colab

1. Download and extract the maintainer's `basicrl-study.zip` bundle, then upload your chosen notebook to [Google Colab](https://colab.research.google.com/).
2. Run its **Optional: Google Colab setup** cell and upload the complete material ZIP when prompted.
3. Run the dependency-install cell, then work through the exercise or reference implementation in order.

The setup prepares the matching topic directory and robotics rendering libraries. Runtime selection, GPU use, saving results, and troubleshooting are covered in the **[Colab guide · 中文](docs/COLAB.md)**. An exercise's `NotImplementedError` marks a task you still need to implement.

### Run locally

Use Python 3.11 and create an isolated environment from the repository root:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements/basics.txt
jupyter lab
```

For the robotics topics, also install:

```bash
python -m pip install -r requirements/robotics.txt
```

Start the kernel in your chosen notebook's directory so local modules, requirements, and expert weights resolve correctly. MuJoCo setup, environment versions, and headless rendering are described in the [environment guide · 中文](docs/ENVIRONMENT.md).

## How to study

1. **Try it first.** Start in `exercises/`, complete the code, and write your own derivations where theory questions are provided.
2. **Compare approaches.** Read the implementation and PDF in `solutions/`, checking notation, tensor shapes, and algorithm conventions.
3. **Experiment.** Change the data, hyperparameters, or training budget, then record returns, success rates, and your interpretation.

> **About the results:** Existing plots and numerical results come from historical runs. They have not been regenerated with the revised code. Goals, rewards, and termination rules also differ across topics. Treat the records as learning examples and rerun experiments to evaluate the current implementation.

Implementation corrections, completed checks, and validation limits are recorded in the [maintenance notes · 中文](docs/MAINTENANCE.md).

## Repository layout

```text
BasicRL/
├── README.md / README.zh-CN.md       # English default and Chinese edition
├── assignments/
│   └── <topic>/
│       ├── README.md / README.zh-CN.md
│       ├── exercises/            # Notebooks, theory, and starter code
│       └── solutions/            # Code, LaTeX, PDFs, and historical plots
├── docs/                         # Colab, environment, and maintenance guides
├── requirements/                 # Basics and robotics dependencies
├── latex/                        # Shared solution formatting
└── scripts/                      # Colab setup, builds, checks, and export
```

The foundations topic keeps separate exercise and solution copies of `q1.py` and `q2.py`. The imitation-learning topic shares an expert checkpoint at `assets/expert.pt`.

<details>
<summary><strong>Maintain the materials: build, check, and export</strong></summary>

Install Tectonic or a TeX distribution containing `latexmk`, plus Poppler for PDF text checks. Then run from the repository root:

```bash
python3 scripts/build_solutions.py
python3 scripts/check_materials.py
python3 scripts/export_release.py
```

Build intermediates go to `.build/`; final PDFs are copied into each topic's `solutions/` directory. The exported `dist/basicrl-study.zip` includes both README languages, notebooks, and solutions. It excludes Git history, local environments, and generated training checkpoints.

</details>

## Licensing

Original contributions to this project are licensed under the [MIT License](LICENSE). Inherited exercises, code, expert weights, and external dependencies retain their applicable rights and license terms; see [NOTICE](NOTICE).
