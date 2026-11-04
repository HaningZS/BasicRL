# Policy Gradients, Shaping, and Off-Policy Data

## 1. Score functions and reward-to-go

Let $p_\theta(\tau)=\mu_0(s_0)\prod_{t=0}^{H-1}\pi_\theta(a_t\mid s_t)P(s_{t+1}\mid s_t,a_t)$ and $R(\tau)=\sum_{t=0}^{H-1}r_t$. Initial states, dynamics, and rewards do not depend on $\theta$.

1. Derive $\nabla_\theta J=\mathbb E_{p_\theta}[\nabla_\theta\log p_\theta(\tau)R(\tau)]$. State conditions that justify differentiation under the integral.
2. Show, using conditional expectation, that rewards preceding $a_t$ can be removed from the term multiplying $\nabla_\theta\log\pi_\theta(a_t\mid s_t)$.
3. Prove that an action-independent state baseline does not bias the policy gradient, and obtain the advantage form with the true value baseline.

Now consider an undiscounted two-state problem. Start at $s_1$. Action $a_1$ receives reward 1 and stays at $s_1$; action $a_2$ receives reward 0 and terminates at $s_2$. The policy chooses $a_1$ with probability $\theta\in(0,1)$.

4. Compute $J'(\theta)$ by the trajectory score-function estimator. Use $K\geq0$ for the number of rewarded self-loops before exit.
5. Compute $J(\theta)$ directly and differentiate it to check the result.
6. Compute the reward-to-go estimator on a trajectory with $K=k$ and verify its expectation equals the same derivative.

## 2. Potential-based reward shaping

In a discounted infinite-horizon MDP, assume bounded rewards, $0<\gamma<1$, and a bounded potential $\Phi=\widehat V$. A reference value estimate satisfies $\|V^\pi-\widehat V\|_\infty\leq\epsilon$. Define

$$\widetilde r_t=r_t+\gamma\Phi(s_{t+1})-\Phi(s_t).$$

1. Express the shaped discounted return in terms of the original return. Show the finite partial sum before taking a limit.
2. Explain why exact optimization preserves the optimal value under the original reward, even when the potential is approximate. Distinguish equality of optimal values from uniqueness of an optimal policy.
3. State the terminal-potential condition needed when an episodic return is stopped instead of continued indefinitely.

## 3. Importance-weighted off-policy gradients

For a fixed behavior policy $\beta$, suppose target trajectories are supported by behavior trajectories, and that the initial-state distribution and dynamics are the same.

1. Rewrite the policy gradient as an expectation over $p_\beta$ using the full trajectory likelihood ratio.
2. Simplify that ratio to a product of action-probability ratios.
3. Expand $\nabla_\theta\log p_\theta(\tau)$ into per-step terms.
4. Discuss data reuse, support, variance, and the effect of clipping or self-normalizing weights.

## Programming discussion

Compare vanilla REINFORCE and reward-to-go for the same start-state discounted objective $J_\gamma=\mathbb E[\sum_t\gamma^t r_t]$. Explain both the relative discount inside reward-to-go and the outer $\gamma^t$ factor. Explain why a Gaussian policy's log density need not be nonpositive and why policy-loss curves alone do not measure control quality.
