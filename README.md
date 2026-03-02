# Exact Time Evolution of a Two-Qubit Transverse Field Ising Model

This project simulates the real-time dynamics of a two-qubit transverse-field Ising model using exact matrix exponentiation.

The time evolution operator is computed as:

U(t) = exp(-i H t)

Expectation values of local observables and correlations are calculated and visualized in three-dimensional observable space.

---

## Model

The Hamiltonian is:

H = -J Z₀Z₁ - h (X₀ + X₁)

where:

- `J` is the interaction strength  
- `h` is the transverse field  
- `X` and `Z` are Pauli operators  

Parameters used:

- J = 1.0  
- h = 0.8  
- Initial state: |00⟩  

---

## Computation

The full 4×4 Hamiltonian is constructed using Kronecker products.  
Time evolution is computed exactly using matrix exponentiation.

For each time step, the following expectation values are evaluated:

- ⟨Z₀⟩  
- ⟨Z₁⟩  
- ⟨Z₀Z₁⟩  

Their trajectory is plotted in 3D to visualize the system’s dynamics.

---

## Requirements

- Python 3.x  
- numpy  
- scipy  
- matplotlib  

---

## Notes

- The simulation is exact (no approximations).  
- The method scales exponentially with system size (dimension = 2^N).  
- Suitable for small systems and benchmarking purposes.
```
