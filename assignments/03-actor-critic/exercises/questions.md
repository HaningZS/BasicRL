# Approximate Policy Improvement

Consider an infinite-horizon discounted MDP with bounded rewards and $0<\gamma<1$. A reference policy $\pi$ has value $V^\pi$, and an estimate satisfies

$$\|V^\pi-\widehat V\|_\infty\leq\epsilon.$$

Let $\widehat\pi$ be greedy with respect to $\widehat V$:

$$\widehat\pi(s)\in\arg\max_a\left[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\widehat V(s')\right].$$

1. Prove the pointwise, one-sided bound

   $$V^\pi(s)-V^{\widehat\pi}(s)\leq\frac{2\gamma\epsilon}{1-\gamma}\quad\text{for every }s.$$

   First derive a one-step inequality using greediness, then close the discounted recurrence. Explain why this is not a bound on the absolute value of the difference and why it does not compare directly with an arbitrary optimal policy.
2. Explain the factor $1/(1-\gamma)$ and why the performance loss is not generally bounded by just $\epsilon$.
3. Derive the finite-horizon version. Use time-indexed values $V_t^\pi$, estimates $\widehat V_t$, and greedy policies $\widehat\pi_t$ with the same terminal condition. State precisely which per-time approximation errors are assumed bounded.

## Programming discussion

Implement the actor and critic losses for a Monte Carlo advantage actor-critic, DDPG, and SAC. Explain the role of detached actor weights, replay buffers, target networks, entropy, true termination versus time-limit truncation, and the change of variables for a squashed Gaussian action.
