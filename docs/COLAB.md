# 在 Google Colab 上学习

本教程使用完整的 `basicrl-study.zip` 资料包。每份 notebook 顶部都有一个可选的 Colab 启动单元格，用来上传资料、恢复目录结构和准备机器人渲染环境；本地 Jupyter 会跳过这个单元格的 Colab 操作。

## 1. 选择主题和运行时

| 主题 | 建议起步方式 | 需要准备什么 |
| --- | --- | --- |
| 00 NumPy / PyTorch | CPU | 同目录的 `q1.py`、`q2.py` |
| 01 BC / DAgger | CPU 即可起步，GPU 可选 | 共享专家权重、MuJoCo |
| 02 策略梯度 | CPU 起步 | MuJoCo，先完成练习或使用参考版 |
| 03 Actor-Critic / DDPG / SAC | CPU 起步，较长实验可选 GPU | MuJoCo，先用较小训练步数检查流程 |
| 04 世界模型 | CPU 起步 | MuJoCo、PPO 与转移数据 |
| 05 视觉控制 | 先用少量图像在 CPU 检查流程，CNN 训练可选 GPU | 120×120 RGB 渲染及图像数据 |

打开 [Google Colab](https://colab.research.google.com/)，通过“运行时 → 更改运行时类型”（Runtime → Change runtime type）选择 CPU 或可用的 GPU。先选好硬件再上传资料。免费 GPU 的型号与可用性会变化，运行时也可能断开，具体以 [Colab 官方 FAQ](https://research.google.com/colaboratory/faq.html) 为准。

选择 GPU 不会自动把所有代码移到 GPU：本项目部分 PPO 示例明确使用 `device="cpu"`。先按默认配置完成流程；只有打算使用 CUDA 时才调整模型设备。

例如视觉主题的状态估计器需要使用 GPU 时，把原初始化行改成 `state_estimator = StateEstimator().to("cuda" if torch.cuda.is_available() else "cpu")`，再创建优化器；参考版的训练函数会将 batch 移到模型所在设备。PPO 的计算设备由各自构造函数的 `device` 参数决定，和 MuJoCo 的渲染后端分别设置。

## 2. 打开 notebook 并上传完整资料

1. 在本地下载并解压 `basicrl-study.zip`。维护者可在仓库根目录运行 `python3 scripts/export_release.py` 生成最新包。
2. 在 Colab 选择“文件 → 上传笔记本”（File → Upload notebook），打开某个主题的 `exercises/notebook.ipynb`；希望先看完整示例时，打开对应的 `solutions/notebook.ipynb`。
3. 连接运行时，执行标题下的 **Optional: Google Colab setup** 代码单元格。
4. 出现上传按钮时，选择完整的 **`basicrl-study.zip`**。这里只需上传 ZIP，无须逐个上传 Python 文件或专家权重。

Colab 打开 notebook 和向运行时上传文件是两步操作。启动单元格会将资料解压到 `/content/basicrl-study/`，并切换到当前主题、当前练习版或参考版的目录。例如，模仿学习参考版应显示：

```text
Working directory: /content/basicrl-study/assignments/01-imitation-learning/solutions
```

这样 `../../../requirements/robotics.txt`、`../assets/expert.pt` 和基础练习的本地模块都能按原目录解析。上传和下载使用 [Colab 官方文件接口](https://github.com/googlecolab/colabtools/blob/main/google/colab/files.py)。

在同一个运行时重跑启动单元格时，会复用已解压的资料。切换主题或练习/参考版时，运行新 notebook 自己的启动单元格；不要手动把参考版的 `q1.py` 覆盖到练习目录。

## 3. 安装依赖并做一次小检查

继续执行 notebook 的依赖安装单元格：基础主题安装 `basics.txt`，机器人主题安装 `robotics.txt`。不要跳过安装单元格，也不要另外克隆旧练习仓库来获取权重。

如果 Colab 在安装后提示重启会话，按提示重启，再从启动单元格开始执行。重启后确认工作目录，随后从上到下运行定义、数据收集、训练和评估部分。Python 包安装策略与固定的机器人版本见 [环境指南](ENVIRONMENT.md)；Colab 的 Python 版本由服务提供，不必在 notebook 中创建本地 `.venv`。

基础主题可在导入后检查模块来源：

```python
from pathlib import Path
import q1
import q2

print(Path.cwd())
print(q1.__file__)
print(q2.__file__)
```

路径应指向你正在学习的 `exercises/` 或 `solutions/`。做练习时，可在左侧文件面板打开并编辑该目录中的 `q1.py`、`q2.py`，保存后重新执行对应单元格；notebook 已提供自动重载设置。

机器人主题在完成安装和渲染设置后，可插入下面的短检查，再开始长训练：

```python
import os
import torch
import gymnasium as gym
import gymnasium_robotics

gym.register_envs(gymnasium_robotics)
print("CUDA available:", torch.cuda.is_available())
print("MuJoCo renderer:", os.environ.get("MUJOCO_GL"))

check_env = gym.make("FetchReach-v4", render_mode="rgb_array",
                     width=120, height=120)
try:
    observation, info = check_env.reset(seed=0)
    observation, reward, terminated, truncated, info = check_env.step(
        check_env.action_space.sample()
    )
    frame = check_env.render()
    assert frame.shape == (120, 120, 3), frame.shape
    print("Environment step and RGB render succeeded:", frame.shape)
finally:
    check_env.close()
```

启动单元格为机器人主题安装 Colab 虚拟机所需的系统渲染库，并默认选择 `osmesa` 软件离屏渲染；有无 GPU 都可以先用这一配置。该设置必须先于 MuJoCo / OpenGL 导入。OSMesa 的含义和平台变量可核对 [MuJoCo 官方实现](https://github.com/google-deepmind/mujoco/blob/main/python/mujoco/osmesa/__init__.py)。已有 EGL 配置的用户可以保留 `MUJOCO_GL=egl`，但需要运行时驱动支持。

先缩小训练轮数、交互步数或图像采集量，确认各环节能连接起来，再恢复 notebook 中的实验配置。练习版中的 `NotImplementedError` 表示该部分仍待实现；参考版用于对照。少量数据下得到的回报不应直接与解答中的历史数字比较。

## 4. 保存 notebook、代码与训练结果

Colab 中的 notebook 编辑记录与 `/content` 虚拟机中的文件分别保存。使用“文件 → 在云端硬盘中保存副本”或下载 `.ipynb` 保存 notebook；另外备份修改过的 `.py`、训练权重和图表。Notebook 保存成功不代表这些文件也已保存。运行时的存储与回收规则见 [官方 FAQ](https://research.google.com/colaboratory/faq.html)。

训练或编辑结束后，可在当前 notebook 最后添加一个代码单元格，打包代码和结果并下载：

```python
from pathlib import Path
import zipfile
from google.colab import files

output = Path("/content/basicrl-results.zip")
suffixes = {".py", ".pth", ".pt", ".zip", ".png", ".mp4"}
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(Path.cwd().rglob("*")):
        relative = path.relative_to(Path.cwd())
        if (path.is_file() and path.suffix in suffixes
                and "figures" not in relative.parts
                and not any(part.startswith(".") for part in relative.parts)):
            archive.write(path, relative)
files.download(str(output))
```

这个结果包包含当前目录下修改的 Python 文件与生成的模型、图片、视频，跳过随资料提供的历史 `figures/`。正在编辑的 notebook 仍通过 Colab 的文件菜单单独保存。

如需将结果包存到自己的 Google Drive，可以在下载前执行：

```python
from google.colab import drive
from pathlib import Path
import shutil

drive.mount("/content/drive")
destination = Path("/content/drive/MyDrive/BasicRL")
destination.mkdir(parents=True, exist_ok=True)
shutil.copy2("/content/basicrl-results.zip", destination / "basicrl-results.zip")
```

按 Colab 提示授权后再复制文件。Drive 挂载接口见 [Colab 官方实现](https://github.com/googlecolab/colabtools/blob/main/google/colab/drive.py)。重新分配到新运行时后，先恢复完整资料包和依赖，再恢复自己保存的 checkpoint；能否继续训练还取决于该 checkpoint 是否包含所需的优化器等状态。

## 5. 常见问题

| 现象 | 处理方式 |
| --- | --- |
| 找不到 `requirements`、`q1` 或 `expert.pt` | 重新运行当前 notebook 的 Colab 启动单元格，检查输出的工作目录。 |
| 上传按钮没有出现或取消了选择 | 重新执行启动单元格，并选择完整资料 ZIP。 |
| 安装后仍有旧版本导入错误 | 按 Colab 提示重启会话，再从顶部执行；检查当前 Python 和包版本。 |
| `libOSMesa`、OpenGL 或 EGL 报错 | 确认机器人系统库安装成功；重启会话后先运行启动与渲染设置，避免先导入 MuJoCo。默认使用 `osmesa`。 |
| `torch.cuda.is_available()` 为 `False` | CPU 配置下属于正常情况；需要 CUDA 时检查运行时类型与当前 GPU 可用性。 |
| 碰到 `NotImplementedError` | 检查是否在练习版的待实现位置；先补全它，或切换到参考版阅读。 |
| 找不到训练 checkpoint | 按 notebook 顺序先执行相应训练阶段；新运行时需要恢复之前保存的模型。 |
| 断开后代码、图片或权重不见了 | 重新上传资料；从已下载的结果包或自己的 Drive 恢复修改与结果。 |

本次补充对启动代码做了本地路径与分支检查，未在真实 Colab 账号中执行完整训练；实际可用的 Python、GPU 和运行时资源以 Colab 当前服务为准。
