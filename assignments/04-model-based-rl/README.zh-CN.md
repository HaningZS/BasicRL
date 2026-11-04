[← 学习路线](../../README.zh-CN.md)

# 04 · 基于模型的强化学习

**简体中文** · [English](README.md)

从真实环境中的专家策略收集转移数据，训练世界模型，再研究模型内训练的策略如何迁移到真实环境。

## 学习目标

- 训练 PPO 专家并收集对齐的状态、动作和下一状态。
- 拟合转移模型，在学习到的环境中训练策略。
- 聚合学习者数据，并在一致的评估协议下比较回报与成功率。

## 资料入口

| 资料 | 用途 |
| :--- | :--- |
| [编程练习](exercises/notebook.ipynb) | 独立完成实现任务 |
| [参考 Notebook](solutions/notebook.ipynb) | 对照算法实现与训练流程 |
| [解答 PDF](solutions/solutions.pdf) | 阅读推导、假设与实验分析 |
| [LaTeX 源码](solutions/solutions.tex) | 编辑或重新编译解答 |

## 运行提示

需要 MuJoCo。每个向量子环境拥有独立 simulator；真实与模型环境统一使用 50 步限制，模型在回合内保持目标坐标不变。

**Colab：** 按 [教程](../../docs/COLAB.md) 打开 Notebook，先运行顶部的可选启动单元格，上传完整资料包，再安装依赖。

**本地：** 从所选 Notebook 的目录启动内核；依赖与渲染设置见 [环境指南](../../docs/ENVIRONMENT.md)。

## 结果与解读

保留两轮世界模型学习和 PPO 曲线。聚合后学习者的历史真实环境指标高于记录的专家指标；这一次比较不构成普遍性能保证。

历史图表位于 [figures/](solutions/figures/)。评估当前实现时，请重新运行对应实验。

[← 上一主题](../03-actor-critic/README.zh-CN.md) · [← 学习路线](../../README.zh-CN.md) · [下一主题 →](../05-visual-control/README.zh-CN.md)
