# 运行环境

在托管的 Google Colab 中运行时，先阅读 [Colab 教程](COLAB.md)。Notebook 顶部的启动单元格会准备文件目录，并为机器人主题安装虚拟机渲染库、默认选择 `osmesa`；以下说明主要面向本地环境。

## Python 与依赖

使用 Python 3.11。基础主题安装 `requirements/basics.txt`；机器人主题安装 `requirements/robotics.txt`。后者固定 Gymnasium 1.1.1、Stable-Baselines3 2.6.0，以及 Gymnasium-Robotics 上游 `1.3.2` 标签对应的完整 commit，以保留 `FetchReach-v4` 和一致的接口。该标签没有独立的 PyPI 发行版，因此通过 Git 安装，需要本机已安装 Git；它的 Python 模块版本仍可能显示 `1.3.1`。底层 PyTorch、torchvision 的配对由安装器按平台解析。版本依据见 [上游源文件](https://github.com/Farama-Foundation/Gymnasium-Robotics/blob/5fb0abd17eee741a903c52baddda77498c864209/gymnasium_robotics/__init__.py)。

```bash
python -m pip install -r requirements/robotics.txt
```

Notebook 的安装单元格使用相对于 notebook 目录的依赖路径。请保留目录结构，从该 notebook 所在目录启动内核。不要混用独立安装的旧 `gym` 与 `gymnasium`。

模仿学习的专家文件已位于 `assignments/01-imitation-learning/assets/expert.pt`。该已有 checkpoint 同时包含 NumPy 归一化统计和权重，加载时显式指定 CPU 映射及其序列化模式；新生成的纯参数 checkpoint 使用 `weights_only=True`。

## MuJoCo 与渲染

Notebook 使用原生 `mujoco` 包，不再安装旧 `mujoco-py`，也不会修改 shell 配置或系统链接器配置。可选 Colab 启动步骤只在其托管虚拟机内为机器人主题安装渲染所需的系统包；本地运行会跳过该步骤。

- macOS：保留默认渲染后端；普通数值练习不需要显卡。
- Linux 无显示器机器：在导入 MuJoCo 前选择 `MUJOCO_GL=egl`，并安装主机对应的 EGL/OpenGL 驱动。Notebook 仅设置环境变量，不替主机安装驱动。
- 没有可用渲染后端时：模仿学习和策略梯度可关闭视频显示，视觉控制主题必须能够生成 RGB 图像。

本次整理不等于在所有平台上验证了完整 MuJoCo 训练。实际执行情况见 [验证记录](MAINTENANCE.md)。

## 两种环境接口

普通 Gymnasium 环境：`reset()` 返回 `(observation, info)`；`step()` 返回五个值，分别包含 `terminated` 和 `truncated`。两者任一为真时都应重置。

SB3 的 `VecEnv`：`reset()` 仅返回批量 observation，`step()` 返回四个值，其中 `done` 合并两种结束信号。它会自动重置；`infos[i]['terminal_observation']` 保存结束前的 observation。每个子环境必须拥有独立状态。实现依据见 [Gymnasium 接口](https://gymnasium.farama.org/api/env/) 与 [SB3 2.6.0 向量环境文档](https://stable-baselines3.readthedocs.io/en/v2.6.0/guide/vec_envs.html)。

重放缓冲区的 bootstrap mask 应符合任务定义：真正的终止不再 bootstrap；作为外部采样限制的超时仍可 bootstrap。有限时域任务则应明确把剩余时间与终止规则纳入状态和目标。参考 [Farama 的终止与截断说明](https://farama.org/Gymnasium-Terminated-Truncated-Step-API)。

## 结果比较

模仿学习使用稀疏奖励；后续主题对目标与进度奖励做了简化。视觉控制还有目标扰动。比较结果时同时记录奖励定义、终止规则、环境版本、训练预算、评估输入和随机种子。历史图表只提供学习案例，不构成当前环境的复现承诺。
