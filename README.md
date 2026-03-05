# Exact Time Evolution of a Two-Qubit Transverse Field Ising Model

This project simulates the **real-time quantum dynamics of a two-qubit transverse-field Ising model** using **exact matrix exponentiation**.

The system is evolved using the unitary time evolution operator

$$
U(t) = e^{-iHt}
$$

and the expectation values of local observables are computed throughout the evolution.

The trajectory of these observables is visualized in a **three-dimensional observable space**, revealing the dynamical behavior of the system.

---

# Model

The system is described by the **two-qubit transverse-field Ising Hamiltonian**

$$
H = -J Z_0 Z_1 - h (X_0 + X_1)
$$

where

- $J$ is the **spin–spin interaction strength**
- $h$ is the **transverse magnetic field**
- $X$ and $Z$ are **Pauli operators**

The subscripts denote the qubit on which the operator acts.

---

# Parameters

Default parameters used in the simulation:

- $J = 1.0$
- $h = 0.8$
- Initial state

$$
|\psi(0)\rangle = |00\rangle
$$

The system is evolved for

$$
t \in [0,10]
$$

with **200 time steps**.

---

# Computation

The full **4 × 4 Hamiltonian matrix** is constructed using Kronecker products of Pauli operators.

For each time step:

1. The unitary operator is computed

$$
U(t) = e^{-iHt}
$$

2. The evolved state is obtained

$$
|\psi(t)\rangle = U(t)|\psi(0)\rangle
$$

3. Expectation values are computed

$$
\langle Z_0 \rangle = \langle \psi(t)| Z_0 |\psi(t) \rangle
$$

$$
\langle Z_1 \rangle = \langle \psi(t)| Z_1 |\psi(t) \rangle
$$

$$
\langle Z_0 Z_1 \rangle = \langle \psi(t)| Z_0 Z_1 |\psi(t) \rangle
$$

These observables define a **trajectory in a 3-dimensional observable space**

$$
(\langle Z_0 \rangle , \langle Z_1 \rangle , \langle Z_0 Z_1 \rangle)
$$

which captures the dynamical evolution of the system.

---

# Physical Regimes Explored

The dynamics of the transverse-field Ising model depends strongly on the ratio

$$
\frac{h}{J}
$$

Different regimes correspond to qualitatively different physics.

---

## 1. Interaction-Dominated Regime

Parameters:

$$
J = 1.0, \quad h = 0.2
$$

In this regime the **spin–spin interaction dominates** over the transverse field.

<img width="1280" height="800" alt="Screenshot 2026-03-05 at 11 38 53 AM" src="https://github.com/user-attachments/assets/96983080-035c-4aa0-9ff2-978e6eda995c" />

The system prefers aligned spin configurations, and the dynamics are relatively constrained.

---

## 2. Balanced Regime

Parameters:

$$
J = 1.0, \quad h = 1.0
$$

Here the **interaction and field compete strongly**, leading to richer dynamics and stronger oscillations in the observables.

<img width="1280" height="800" alt="Screenshot 2026-03-05 at 11 39 56 AM" src="https://github.com/user-attachments/assets/4d20e444-421c-4a94-b46d-8ecff9cce0b7" />

---

## 3. Field-Dominated Regime

Parameters:

$$
J = 0.2, \quad h = 1.0
$$

In this regime the **transverse field dominates**, causing spins to frequently flip between states.

<img width="1280" height="800" alt="Screenshot 2026-03-05 at 11 41 28 AM" src="https://github.com/user-attachments/assets/fac1d946-77d8-4fe3-ac49-570d50c8bc0c" />

The observable trajectories reflect strong field-induced dynamics.

## 4. Combined Plots of Interaction-dominated, Balanced and Field-Dominated Region

<img width="1280" height="800" alt="Screenshot 2026-03-05 at 11 42 35 AM" src="https://github.com/user-attachments/assets/e9dc753e-f05a-4ecc-80ec-5ff9283cf079" />


---

# Requirements

Python packages required:

- Python 3.x
- numpy
- scipy
- matplotlib

Install using:

```
pip install numpy scipy matplotlib
```

---

# Notes

- The simulation is **exact** and involves **no approximations**.
- The Hilbert space dimension scales as

$$
\dim = 2^N
$$

for an $N$-qubit system.

- As a result, exact simulations become computationally expensive for large systems.

This implementation therefore serves as a **small-system benchmark for studying quantum many-body dynamics**.


---
