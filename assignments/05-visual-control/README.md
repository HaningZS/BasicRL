[← Learning path](../../README.md)

# 05 · Visual State Estimation & Control

[简体中文](README.zh-CN.md) · **English**

Estimate states from RGB images, compare estimated-state and end-to-end image policies, and connect supervised prediction error with closed-loop control.

## Learning goals

- Collect temporally aligned RGB images and state labels.
- Build a CNN estimator and a consistent observation wrapper.
- Evaluate the deployed visual pipeline, true-state diagnostic, and end-to-end policy separately.

## Resources

| Material | Purpose |
| :--- | :--- |
| [Exercise notebook](exercises/notebook.ipynb) | Work through the implementation tasks |
| [Reference notebook](solutions/notebook.ipynb) | Compare implementations and training procedures |
| [Solution PDF](solutions/solutions.pdf) | Read derivations, assumptions, and experiment analysis |
| [LaTeX source](solutions/solutions.tex) | Edit or rebuild the worked solutions |

## Running this topic

MuJoCo and 120×120 RGB rendering are required. The reference returns unbatched observations, avoids repeated normalization of [0,1] images, and measures deployment success through the estimated-state pipeline.

**Colab:** Open the notebook, run its optional startup cell, upload the complete bundle, and install dependencies. See the [Colab guide · 中文](../../docs/COLAB.md).

**Local:** Start the kernel in the selected notebook's directory. Dependencies and rendering are described in the [environment guide · 中文](../../docs/ENVIRONMENT.md).

## Results and interpretation

Historical records distinguish estimated-state returns from success measured with true-state inputs. An unrecorded visual-pipeline success rate is left unreported.

Historical plots are in [figures/](solutions/figures/). Rerun the relevant experiments to evaluate the current implementation.

[← Previous topic](../04-model-based-rl/README.md) · [← Learning path](../../README.md)
