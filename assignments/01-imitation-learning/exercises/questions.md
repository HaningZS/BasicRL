# Imitation Learning and Discounted Costs

## 1. Recovery under distribution shift

Consider a discounted infinite-horizon cost-minimization problem with $0<\gamma<1$. The initial state is safe. All safe states have identical continuation costs: a correct action costs 0 and stays safe; an incorrect action costs 1 and moves to a ditch. At each safe state, both learners make a mistake with probability $\epsilon$.

- The expert remains safe and has cost 0.
- A behavior-cloning (BC) learner in the ditch stays there forever, paying cost 1 per step.
- A dataset-aggregation (DAgger) learner in the ditch pays cost 1 for the current action, then returns to a safe state with probability $1-\epsilon$, or stays in the ditch with probability $\epsilon$.

Let $C$ and $D$ denote the expected discounted costs when starting safe or in the ditch. Derive exact formulas for the initial cost of BC and DAgger. Then discuss the approximations for small $\epsilon$ and large discount factor, including any additional relation between $\epsilon$ and $1-\gamma$ that the approximation requires.

## 2. A cost-minimization MDP

All transitions below are deterministic. Set $\gamma=0.9$ and minimize the infinite discounted sum of costs. States 3, 4, and 5 have mandatory self-loops; they are not terminal states.

| State | Action | Next state | Immediate cost |
| --- | --- | --- | --- |
| 1 | a1 | 2 | 0 |
| 1 | a2 | 3 | 2 |
| 2 | a1 | 4 | 18 |
| 2 | a2 | 5 | 0 |
| 3 | a1 | 3 | 1 |
| 4 | a1 | 4 | 0 |
| 5 | a1 | 5 | 1.5 |

Compute $V^*(s)$ and an optimal action for every state. Explain why minimizing immediate cost alone does not solve the problem.
