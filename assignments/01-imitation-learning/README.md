[← Learning path](../../README.md)

# 01 · Imitation Learning: BC & DAgger

[简体中文](README.zh-CN.md) · **English**

Learn continuous-action policies from expert demonstrations, then use interactive data aggregation to study behavior beyond the demonstration distribution.

## Learning goals

- Derive exact discounted costs for BC and DAgger in a recovery problem.
- Implement supervised behavior cloning and validation-based checkpoint selection.
- Execute learner actions, query expert labels, and aggregate training data.

## Resources

| Material | Purpose |
| :--- | :--- |
| [Exercise notebook](exercises/notebook.ipynb) | Work through the implementation tasks |
| [Theory questions](exercises/questions.md) | Derive the results before reading the solution |
| [Reference notebook](solutions/notebook.ipynb) | Compare implementations and training procedures |
| [Solution PDF](solutions/solutions.pdf) | Read derivations, assumptions, and experiment analysis |
| [LaTeX source](solutions/solutions.tex) | Edit or rebuild the worked solutions |

## Running this topic

MuJoCo is required. The shared expert checkpoint is included at `assets/expert.pt`; both notebooks load it through `../assets/expert.pt` without another download.

**Colab:** Open the notebook, run its optional startup cell, upload the complete bundle, and install dependencies. See the [Colab guide · 中文](../../docs/COLAB.md).

**Local:** Start the kernel in the selected notebook's directory. Dependencies and rendering are described in the [environment guide · 中文](../../docs/ENVIRONMENT.md).

## Results and interpretation

Historical returns for random actions, the expert, BC, and DAgger are retained alongside a BC validation curve. The reference selects checkpoints by validation loss; the historical results have not been regenerated with the revised code.

Historical plots are in [figures/](solutions/figures/). Rerun the relevant experiments to evaluate the current implementation.

[← Previous topic](../00-numpy-pytorch/README.md) · [← Learning path](../../README.md) · [Next topic →](../02-policy-gradients/README.md)
