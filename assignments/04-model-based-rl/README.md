[← Learning path](../../README.md)

# 04 · Model-Based Reinforcement Learning

[简体中文](README.zh-CN.md) · **English**

Collect transitions with an expert policy, fit a world model, and study how a policy trained inside that model transfers to the real environment.

## Learning goals

- Train a PPO expert and collect aligned states, actions, and next states.
- Fit transition dynamics and train a policy inside the learned environment.
- Aggregate learner data and compare returns and success under a consistent evaluation protocol.

## Resources

| Material | Purpose |
| :--- | :--- |
| [Exercise notebook](exercises/notebook.ipynb) | Work through the implementation tasks |
| [Reference notebook](solutions/notebook.ipynb) | Compare implementations and training procedures |
| [Solution PDF](solutions/solutions.pdf) | Read derivations, assumptions, and experiment analysis |
| [LaTeX source](solutions/solutions.tex) | Edit or rebuild the worked solutions |

## Running this topic

MuJoCo is required. Each vectorized sub-environment owns an independent simulator. Real and learned environments use a 50-step limit, and the model keeps goal coordinates fixed within an episode.

**Colab:** Open the notebook, run its optional startup cell, upload the complete bundle, and install dependencies. See the [Colab guide · 中文](../../docs/COLAB.md).

**Local:** Start the kernel in the selected notebook's directory. Dependencies and rendering are described in the [environment guide · 中文](../../docs/ENVIRONMENT.md).

## Results and interpretation

Curves for both rounds of world-model learning and PPO are retained. The aggregated learner has higher recorded real-environment metrics than the expert in those evaluations; that comparison is not a general performance guarantee.

Historical plots are in [figures/](solutions/figures/). Rerun the relevant experiments to evaluate the current implementation.

[← Previous topic](../03-actor-critic/README.md) · [← Learning path](../../README.md) · [Next topic →](../05-visual-control/README.md)
