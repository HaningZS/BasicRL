[← 学习路线](../../README.zh-CN.md)

# 00 · NumPy 与 PyTorch 基础

**简体中文** · [English](README.md)

从数组与张量的基本操作开始，练习形状推理，再完成一个带模型保存与加载的回归模型。

## 学习目标

- 解释按行计算距离时的归约轴与广播行为。
- 用向量化操作拼接方格与视频帧，保持像素顺序。
- 完成回归训练、checkpoint 选择与加载评估。

## 资料入口

| 资料 | 用途 |
| :--- | :--- |
| [编程练习](exercises/notebook.ipynb) | 独立完成实现任务 |
| [参考 Notebook](solutions/notebook.ipynb) | 对照算法实现与训练流程 |
| [解答 PDF](solutions/solutions.pdf) | 阅读推导、假设与实验分析 |
| [LaTeX 源码](solutions/solutions.tex) | 编辑或重新编译解答 |
| [形状与拼接](solutions/q1.py) · [回归与 checkpoint](solutions/q2.py) | 基础 Python 参考模块 |

## 运行提示

CPU 即可。练习版与参考版各有同目录的 `q1.py`、`q2.py`；导入前确认文件路径与当前学习版本一致。

**Colab：** 按 [教程](../../docs/COLAB.md) 打开 Notebook，先运行顶部的可选启动单元格，上传完整资料包，再安装依赖。

**本地：** 从所选 Notebook 的目录启动内核；依赖与渲染设置见 [环境指南](../../docs/ENVIRONMENT.md)。

## 结果与解读

此主题未提供历史回归训练曲线。用实际训练损失和 checkpoint 加载后的预测检查自己的实现。

[← 学习路线](../../README.zh-CN.md) · [下一主题 →](../01-imitation-learning/README.zh-CN.md)
