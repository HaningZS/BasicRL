[← 学习路线](../../README.zh-CN.md)

# 03 · Actor-Critic 与近似策略改进

**简体中文** · [English](README.md)

把学习到的价值基线引入策略更新，比较 DDPG 与 SAC，并分析价值近似误差如何影响贪心策略。

## 学习目标

- 证明近似策略改进的单边误差界及有限时域版本。
- 实现完整轨迹回报的优势基线、DDPG 和 SAC。
- 区分回合终止与时间截断，检查 replay、目标网络和动作分布。

## 资料入口

| 资料 | 用途 |
| :--- | :--- |
| [编程练习](exercises/notebook.ipynb) | 独立完成实现任务 |
| [理论题](exercises/questions.md) | 先自行推导，再对照解答 |
| [参考 Notebook](solutions/notebook.ipynb) | 对照算法实现与训练流程 |
| [解答 PDF](solutions/solutions.pdf) | 阅读推导、假设与实验分析 |
| [LaTeX 源码](solutions/solutions.tex) | 编辑或重新编译解答 |

## 运行提示

需要 MuJoCo。基础 actor-critic 使用完整轨迹回报与学习到的 baseline。参考实现修正了优势形状、折扣、缓冲区接口、设备 buffer 和 SAC 回合重置。

**Colab：** 按 [教程](../../docs/COLAB.md) 打开 Notebook，先运行顶部的可选启动单元格，上传完整资料包，再安装依赖。

**本地：** 从所选 Notebook 的目录启动内核；依赖与渲染设置见 [环境指南](../../docs/ENVIRONMENT.md)。

## 结果与解读

保留了历史损失图与评估输出。它们早于参考实现的修订，不能作为当前代码训练效果的验证。

历史图表位于 [figures/](solutions/figures/)。评估当前实现时，请重新运行对应实验。

[← 上一主题](../02-policy-gradients/README.zh-CN.md) · [← 学习路线](../../README.zh-CN.md) · [下一主题 →](../04-model-based-rl/README.zh-CN.md)
