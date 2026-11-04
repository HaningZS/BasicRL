[← 学习路线](../../README.zh-CN.md)

# 01 · 模仿学习：BC 与 DAgger

**简体中文** · [English](README.md)

用专家示范学习连续动作策略，再通过交互式数据聚合，理解学习者偏离示范分布后的行为。

## 学习目标

- 分析 BC 与 DAgger 在恢复问题中的精确折扣成本。
- 完成行为克隆的监督训练与验证 checkpoint 选择。
- 执行学习者动作、查询专家标签并聚合训练数据。

## 资料入口

| 资料 | 用途 |
| :--- | :--- |
| [编程练习](exercises/notebook.ipynb) | 独立完成实现任务 |
| [理论题](exercises/questions.md) | 先自行推导，再对照解答 |
| [参考 Notebook](solutions/notebook.ipynb) | 对照算法实现与训练流程 |
| [解答 PDF](solutions/solutions.pdf) | 阅读推导、假设与实验分析 |
| [LaTeX 源码](solutions/solutions.tex) | 编辑或重新编译解答 |

## 运行提示

需要 MuJoCo。专家权重已放在本主题的 `assets/expert.pt`，两个 notebook 都通过 `../assets/expert.pt` 读取，无须额外下载。

**Colab：** 按 [教程](../../docs/COLAB.md) 打开 Notebook，先运行顶部的可选启动单元格，上传完整资料包，再安装依赖。

**本地：** 从所选 Notebook 的目录启动内核；依赖与渲染设置见 [环境指南](../../docs/ENVIRONMENT.md)。

## 结果与解读

保留了随机策略、专家、BC、DAgger 的历史返回值和 BC 验证曲线。参考实现按验证损失选择 checkpoint，历史结果未随修订后的代码重跑。

历史图表位于 [figures/](solutions/figures/)。评估当前实现时，请重新运行对应实验。

[← 上一主题](../00-numpy-pytorch/README.zh-CN.md) · [← 学习路线](../../README.zh-CN.md) · [下一主题 →](../02-policy-gradients/README.zh-CN.md)
