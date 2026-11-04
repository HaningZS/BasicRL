[← 学习路线](../../README.zh-CN.md)

# 02 · 策略梯度与奖励塑形

**简体中文** · [English](README.md)

从 score-function 恒等式推导策略梯度，理解因果性、baseline 与折扣约定，再实现两种 REINFORCE。

## 学习目标

- 用条件期望推导 reward-to-go 与 baseline 的无偏性。
- 理解奖励塑形的终止条件，以及重要性采样的支持条件。
- 实现 REINFORCE，并为起始状态折扣目标保留外层 `gamma**t`。

## 资料入口

| 资料 | 用途 |
| :--- | :--- |
| [编程练习](exercises/notebook.ipynb) | 独立完成实现任务 |
| [理论题](exercises/questions.md) | 先自行推导，再对照解答 |
| [参考 Notebook](solutions/notebook.ipynb) | 对照算法实现与训练流程 |
| [解答 PDF](solutions/solutions.pdf) | 阅读推导、假设与实验分析 |
| [LaTeX 源码](solutions/solutions.tex) | 编辑或重新编译解答 |

## 运行提示

需要 MuJoCo。先对照 PDF 中的目标定义，再检查 reward-to-go 内部的相对折扣和外层 `gamma**t` 是否同时使用。

**Colab：** 按 [教程](../../docs/COLAB.md) 打开 Notebook，先运行顶部的可选启动单元格，上传完整资料包，再安装依赖。

**本地：** 从所选 Notebook 的目录启动内核；依赖与渲染设置见 [环境指南](../../docs/ENVIRONMENT.md)。

## 结果与解读

保留了两种 REINFORCE 的历史 loss 曲线。其符号和单调性不能代替回报评估；这些曲线早于折扣处理的修正。

历史图表位于 [figures/](solutions/figures/)。评估当前实现时，请重新运行对应实验。

[← 上一主题](../01-imitation-learning/README.zh-CN.md) · [← 学习路线](../../README.zh-CN.md) · [下一主题 →](../03-actor-critic/README.zh-CN.md)
