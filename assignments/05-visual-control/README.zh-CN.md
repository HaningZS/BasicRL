[← 学习路线](../../README.zh-CN.md)

# 05 · 视觉状态估计与控制

**简体中文** · [English](README.md)

从 RGB 图像估计状态，再比较估计状态管道与端到端图像策略，理解监督误差和闭环控制之间的联系。

## 学习目标

- 采集时间对齐的 RGB 图像与状态标签。
- 构建 CNN 状态估计器及一致的观测包装器。
- 分别评估部署时的视觉管道、真实状态诊断和端到端策略。

## 资料入口

| 资料 | 用途 |
| :--- | :--- |
| [编程练习](exercises/notebook.ipynb) | 独立完成实现任务 |
| [参考 Notebook](solutions/notebook.ipynb) | 对照算法实现与训练流程 |
| [解答 PDF](solutions/solutions.pdf) | 阅读推导、假设与实验分析 |
| [LaTeX 源码](solutions/solutions.tex) | 编辑或重新编译解答 |

## 运行提示

需要 MuJoCo 及 120×120 RGB 渲染。参考版返回不带 batch 维度的单次观测，为 [0,1] 图像关闭重复归一化，并在估计状态管道上计算部署成功率。

**Colab：** 按 [教程](../../docs/COLAB.md) 打开 Notebook，先运行顶部的可选启动单元格，上传完整资料包，再安装依赖。

**本地：** 从所选 Notebook 的目录启动内核；依赖与渲染设置见 [环境指南](../../docs/ENVIRONMENT.md)。

## 结果与解读

历史记录区分估计状态回报与真实状态输入的诊断成功率。未记录的视觉管道成功率没有填入实验表格。

历史图表位于 [figures/](solutions/figures/)。评估当前实现时，请重新运行对应实验。

[← 上一主题](../04-model-based-rl/README.zh-CN.md) · [← 学习路线](../../README.zh-CN.md)
