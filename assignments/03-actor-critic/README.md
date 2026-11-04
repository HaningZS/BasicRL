[← Learning path](../../README.md)

# 03 · Actor-Critic & Approximate Policy Improvement

[简体中文](README.zh-CN.md) · **English**

Introduce a learned value baseline, compare DDPG and SAC, and analyze how value-approximation errors affect a greedy policy.

## Learning goals

- Prove a one-sided approximate-improvement bound and its finite-horizon version.
- Implement a full-return advantage baseline, DDPG, and SAC.
- Distinguish termination from truncation and inspect replay, target networks, and action distributions.

## Resources

| Material | Purpose |
| :--- | :--- |
| [Exercise notebook](exercises/notebook.ipynb) | Work through the implementation tasks |
| [Theory questions](exercises/questions.md) | Derive the results before reading the solution |
| [Reference notebook](solutions/notebook.ipynb) | Compare implementations and training procedures |
| [Solution PDF](solutions/solutions.pdf) | Read derivations, assumptions, and experiment analysis |
| [LaTeX source](solutions/solutions.tex) | Edit or rebuild the worked solutions |

## Running this topic

MuJoCo is required. The basic actor-critic uses full trajectory returns and a learned baseline. The reference corrects advantage shapes, discounts, replay interfaces, device buffers, and SAC episode resets.

**Colab:** Open the notebook, run its optional startup cell, upload the complete bundle, and install dependencies. See the [Colab guide · 中文](../../docs/COLAB.md).

**Local:** Start the kernel in the selected notebook's directory. Dependencies and rendering are described in the [environment guide · 中文](../../docs/ENVIRONMENT.md).

## Results and interpretation

Historical loss plots and evaluation outputs are retained. They predate the reference revisions and do not validate the training performance of the current code.

Historical plots are in [figures/](solutions/figures/). Rerun the relevant experiments to evaluate the current implementation.

[← Previous topic](../02-policy-gradients/README.md) · [← Learning path](../../README.md) · [Next topic →](../04-model-based-rl/README.md)
