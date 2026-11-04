[← Learning path](../../README.md)

# 00 · NumPy & PyTorch Foundations

[简体中文](README.zh-CN.md) · **English**

Start with arrays and tensors, reason about shapes, and train a regressor with checkpoint saving and loading.

## Learning goals

- Explain reduction axes and broadcasting in row-wise distances.
- Assemble squares and video frames with vectorized operations that preserve pixel order.
- Implement regression training, checkpoint selection, and loading for evaluation.

## Resources

| Material | Purpose |
| :--- | :--- |
| [Exercise notebook](exercises/notebook.ipynb) | Work through the implementation tasks |
| [Reference notebook](solutions/notebook.ipynb) | Compare implementations and training procedures |
| [Solution PDF](solutions/solutions.pdf) | Read derivations, assumptions, and experiment analysis |
| [LaTeX source](solutions/solutions.tex) | Edit or rebuild the worked solutions |
| [Shapes and assembly](solutions/q1.py) · [Regression and checkpoints](solutions/q2.py) | Reference Python modules |

## Running this topic

A CPU is sufficient. Exercise and solution notebooks each have their own `q1.py` and `q2.py`; check that imports resolve to the version you selected.

**Colab:** Open the notebook, run its optional startup cell, upload the complete bundle, and install dependencies. See the [Colab guide · 中文](../../docs/COLAB.md).

**Local:** Start the kernel in the selected notebook's directory. Dependencies and rendering are described in the [environment guide · 中文](../../docs/ENVIRONMENT.md).

## Results and interpretation

No historical regression training curves are provided. Check your implementation using its training loss and predictions from a reloaded checkpoint.

[← Learning path](../../README.md) · [Next topic →](../01-imitation-learning/README.md)
