import numpy as np
import matplotlib.pyplot as plt
from numpy import kron
from scipy.linalg import expm


I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])

J = 1.0
h = 0.8
t_max = 10
n_steps = 200


# Hamiltonian
H = (
    -J * kron(Z, Z)
    -h * (kron(X, I) + kron(I, X))
)

# Initial state |00>
psi0 = np.array([1, 0, 0, 0], dtype=complex)

times = np.linspace(0, t_max, n_steps)

# Operators for expectation values
Z0 = kron(Z, I)
Z1 = kron(I, Z)
ZZ = kron(Z, Z)

exp_Z0 = []
exp_Z1 = []
exp_ZZ = []

# Time evolution
for t in times:
    U = expm(-1j * H * t)
    psi_t = U @ psi0

    exp_Z0.append(np.real(np.conjugate(psi_t) @ (Z0 @ psi_t)))
    exp_Z1.append(np.real(np.conjugate(psi_t) @ (Z1 @ psi_t)))
    exp_ZZ.append(np.real(np.conjugate(psi_t) @ (ZZ @ psi_t)))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(exp_Z0, exp_Z1, exp_ZZ)
ax.set_xlabel("<Z0>")
ax.set_ylabel("<Z1>")
ax.set_zlabel("<Z0 Z1>")
ax.set_title("2-Qubit Quantum Many-Body Dynamics")
plt.show()


