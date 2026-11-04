<h1 align="center">BasicRL</h1>

<p align="center"><strong>从张量基础到视觉控制，动手学习强化学习。</strong></p>

<p align="center">6 个主题 · 12 份 Notebook · 6 份解答 / 20 页 · 可选 Colab 启动</p>

<div align="center">

**简体中文** · [English](README.md)

[学习路线](#学习路线) · [快速开始](#快速开始) · [理论参考](#理论参考) · [Colab 教程](docs/COLAB.md) · [文档导航](docs/README.zh-CN.md) · [MIT](LICENSE)

</div>

BasicRL 是一套面向自学的强化学习练习与参考解答。从 NumPy 和 PyTorch 起步，逐步学习模仿学习、策略梯度、Actor-Critic、世界模型与视觉控制。每个主题将题目、实现和推导放在一起，方便先动手，再对照理解。

| 动手练习 | 理解推导 | 对照实现 |
| :--- | :--- | :--- |
| 带有待完成任务的 Notebook | 写明假设与中间步骤的 PDF 解答 | 参考 Notebook 与可编辑的 LaTeX 源码 |

## 学习路线

按顺序完成六个主题，或从熟悉的部分开始。Notebook、理论题与解答使用英文；导航提供中英文版本。

| 主题 | 你会学习什么 | 学习资源 |
| :--- | :--- | :--- |
| **00 · [NumPy 与 PyTorch](assignments/00-numpy-pytorch/README.zh-CN.md)** | 张量形状、图像拼接、线性回归与模型保存 | [练习](assignments/00-numpy-pytorch/exercises/notebook.ipynb) · [实现](assignments/00-numpy-pytorch/solutions/notebook.ipynb) · [PDF](assignments/00-numpy-pytorch/solutions/solutions.pdf) |
| **01 · [模仿学习](assignments/01-imitation-learning/README.zh-CN.md)** | BC、DAgger、分布偏移与折扣成本 | [练习](assignments/01-imitation-learning/exercises/notebook.ipynb) · [实现](assignments/01-imitation-learning/solutions/notebook.ipynb) · [PDF](assignments/01-imitation-learning/solutions/solutions.pdf) |
| **02 · [策略梯度](assignments/02-policy-gradients/README.zh-CN.md)** | REINFORCE、reward-to-go、baseline 与奖励塑形 | [练习](assignments/02-policy-gradients/exercises/notebook.ipynb) · [实现](assignments/02-policy-gradients/solutions/notebook.ipynb) · [PDF](assignments/02-policy-gradients/solutions/solutions.pdf) |
| **03 · [Actor-Critic](assignments/03-actor-critic/README.zh-CN.md)** | 价值基线、DDPG、SAC 与近似策略改进 | [练习](assignments/03-actor-critic/exercises/notebook.ipynb) · [实现](assignments/03-actor-critic/solutions/notebook.ipynb) · [PDF](assignments/03-actor-critic/solutions/solutions.pdf) |
| **04 · [基于模型的强化学习](assignments/04-model-based-rl/README.zh-CN.md)** | PPO、世界模型、模型误差与数据聚合 | [练习](assignments/04-model-based-rl/exercises/notebook.ipynb) · [实现](assignments/04-model-based-rl/solutions/notebook.ipynb) · [PDF](assignments/04-model-based-rl/solutions/solutions.pdf) |
| **05 · [视觉状态估计与控制](assignments/05-visual-control/README.zh-CN.md)** | CNN 状态估计、估计状态控制与端到端图像策略 | [练习](assignments/05-visual-control/exercises/notebook.ipynb) · [实现](assignments/05-visual-control/solutions/notebook.ipynb) · [PDF](assignments/05-visual-control/solutions/solutions.pdf) |

## 理论参考

推荐将 [Modern Adaptive Control and Reinforcement Learning（MACRL）](https://macrl-book.github.io/assets/pdf/macrl.pdf) 作为理论入门参考，与本仓库的练习配合阅读，逐步把实现细节与背后的数学思想联系起来。

## 快速开始

### 在 Colab 中运行

1. 下载并解压维护者导出的 `basicrl-study.zip`，在 [Google Colab](https://colab.research.google.com/) 中上传你选择的 Notebook。
2. 执行顶部的 **Optional: Google Colab setup** 单元格，按提示上传完整资料 ZIP。
3. 运行依赖安装单元格，再按顺序完成练习或运行参考实现。

启动步骤会准备对应主题的目录和机器人渲染库。运行时选择、GPU 使用、结果保存与常见问题见 **[Colab 使用教程](docs/COLAB.md)**。练习版中的 `NotImplementedError` 是待实现的任务。

### 在本地运行

建议使用 Python 3.11。在仓库根目录创建独立环境：

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements/basics.txt
jupyter lab
```

机器人主题另外安装：

```bash
python -m pip install -r requirements/robotics.txt
```

从所选 Notebook 的目录启动内核，让本地模块、依赖文件和专家权重按相对路径解析。MuJoCo、环境版本与离屏渲染配置见 [环境指南](docs/ENVIRONMENT.md)。

## 怎样使用这些资料

1. **先尝试。** 从 `exercises/` 开始，完成编程任务；有理论题的主题再独立写出推导。
2. **再对照。** 阅读 `solutions/` 中的实现与 PDF，检查符号、张量形状和算法约定。
3. **做实验。** 修改数据、超参数或训练预算，记录回报、成功率和自己的解释。

> **关于实验结果**：已有图表与数值来自历史运行，未用修订后的代码重新训练。不同主题的目标、奖励和终止规则也有差异。把它们作为学习案例；评估当前代码时，请重新运行对应实验。

已执行的检查、实现修正及验证边界见 [整理与验证记录](docs/MAINTENANCE.md)。

## 文件结构

```text
BasicRL/
├── README.md / README.zh-CN.md       # 英文默认入口与中文版
├── assignments/
│   └── <topic>/
│       ├── README.md / README.zh-CN.md
│       ├── exercises/            # Notebook、理论题与待完成代码
│       └── solutions/            # 参考实现、LaTeX、PDF 与历史曲线
├── docs/                         # Colab、环境与维护说明
├── requirements/                 # 基础与机器人依赖
├── latex/                        # 解答共用排版
└── scripts/                      # Colab 启动、编译、检查与导出
```

基础主题的 `q1.py`、`q2.py` 随练习版和参考版分别存放。模仿学习的共享专家权重位于该主题的 `assets/expert.pt`。

<details>
<summary><strong>维护资料：编译 PDF、检查与导出</strong></summary>

安装 Tectonic 或含 `latexmk` 的 TeX 发行版，以及用于文本检查的 Poppler 后，在仓库根目录运行：

```bash
python3 scripts/build_solutions.py
python3 scripts/check_materials.py
python3 scripts/export_release.py
```

编译中间文件保存在 `.build/`；最终 PDF 写回各主题的 `solutions/`。导出的 `dist/basicrl-study.zip` 包含中英文 README、Notebook 和解答，不包含 Git 历史、本地环境及生成的训练 checkpoint。

</details>

## 授权说明

本项目的原创内容采用 [MIT License](LICENSE)。继承的题目、代码、专家权重及外部依赖保留各自适用的权利与授权条款，详见 [NOTICE](NOTICE)。
