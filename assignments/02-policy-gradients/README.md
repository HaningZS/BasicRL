[← Learning path](../../README.md)

# 02 · Policy Gradients & Reward Shaping

[简体中文](README.zh-CN.md) · **English**

Derive policy gradients from the score-function identity, understand causality, baselines, and discount conventions, then implement two REINFORCE variants.

## Learning goals

- Use conditional expectation to derive reward-to-go and baseline identities.
- Understand terminal conditions for reward shaping and support conditions for importance sampling.
- Implement REINFORCE with the outer `gamma**t` factor for the start-state discounted objective.

## Resources

| Material | Purpose |
| :--- | :--- |
| [Exercise notebook](exercises/notebook.ipynb) | Work through the implementation tasks |
| [Theory questions](exercises/questions.md) | Derive the results before reading the solution |
| [Reference notebook](solutions/notebook.ipynb) | Compare implementations and training procedures |
| [Solution PDF](solutions/solutions.pdf) | Read derivations, assumptions, and experiment analysis |
| [LaTeX source](solutions/solutions.tex) | Edit or rebuild the worked solutions |

## Running this topic

MuJoCo is required. Match the objective defined in the PDF, checking both the relative discount inside reward-to-go and the outer `gamma**t` factor.

**Colab:** Open the notebook, run its optional startup cell, upload the complete bundle, and install dependencies. See the [Colab guide · 中文](../../docs/COLAB.md).

**Local:** Start the kernel in the selected notebook's directory. Dependencies and rendering are described in the [environment guide · 中文](../../docs/ENVIRONMENT.md).

## Results and interpretation

Historical loss curves for both REINFORCE variants are retained. Their signs and trends do not replace return evaluation, and the curves predate the discounting correction.

Historical plots are in [figures/](solutions/figures/). Rerun the relevant experiments to evaluate the current implementation.

[← Previous topic](../01-imitation-learning/README.md) · [← Learning path](../../README.md) · [Next topic →](../03-actor-critic/README.md)
