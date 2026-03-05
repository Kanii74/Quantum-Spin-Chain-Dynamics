import numpy as np
import matplotlib.pyplot as plt
from numpy import kron
from scipy.linalg import expm


# ------------------------------------------------
# Pauli matrices
# ------------------------------------------------

I = np.array([[1,0],[0,1]])
X = np.array([[0,1],[1,0]])
Z = np.array([[1,0],[0,-1]])


# ------------------------------------------------
# Observables
# ------------------------------------------------

Z0 = kron(Z,I)
Z1 = kron(I,Z)
ZZ = kron(Z,Z)


# ------------------------------------------------
# Simulation parameters
# ------------------------------------------------

t_max = 10
n_steps = 200
times = np.linspace(0,t_max,n_steps)

psi0 = np.array([1,0,0,0],dtype=complex)  # |00>


# ------------------------------------------------
# Hamiltonian
# ------------------------------------------------

def build_hamiltonian(J,h):

    H = (
        -J * kron(Z,Z)
        -h * (kron(X,I) + kron(I,X))
    )

    return H


# ------------------------------------------------
# Time evolution simulation
# ------------------------------------------------

def simulate(J,h):

    H = build_hamiltonian(J,h)

    exp_Z0=[]
    exp_Z1=[]
    exp_ZZ=[]

    for t in times:

        U = expm(-1j*H*t)
        psi_t = U @ psi0

        exp_Z0.append(np.real(np.conjugate(psi_t) @ (Z0 @ psi_t)))
        exp_Z1.append(np.real(np.conjugate(psi_t) @ (Z1 @ psi_t)))
        exp_ZZ.append(np.real(np.conjugate(psi_t) @ (ZZ @ psi_t)))

    return np.array(exp_Z0), np.array(exp_Z1), np.array(exp_ZZ)



# ------------------------------------------------
# Plot single regime
# ------------------------------------------------

def plot_single(Z0_vals,Z1_vals,ZZ_vals,title,color,filename):

    fig = plt.figure(figsize=(9,7))
    ax = fig.add_subplot(111,projection='3d')

    ax.plot(
        Z0_vals,
        Z1_vals,
        ZZ_vals,
        color=color,
        linewidth=2.5
    )

    # mark initial state
    ax.scatter(
        Z0_vals[0],
        Z1_vals[0],
        ZZ_vals[0],
        color=color,
        s=70,
        label="Initial state"
    )

    ax.set_xlabel(r"$\langle Z_0 \rangle$")
    ax.set_ylabel(r"$\langle Z_1 \rangle$")
    ax.set_zlabel(r"$\langle Z_0 Z_1 \rangle$")

    ax.set_title(title)

    ax.view_init(elev=25,azim=35)

    ax.legend()

    plt.tight_layout()

    plt.savefig(filename,dpi=300)

    plt.show()



# ------------------------------------------------
# Parameter regimes
# ------------------------------------------------

cases = [

    (1.0,0.2,"Interaction Dominated (J=1.0, h=0.2)","blue","interaction_dominated.png"),

    (1.0,1.0,"Balanced Regime (J=1.0, h=1.0)","green","balanced_regime.png"),

    (0.2,1.0,"Field Dominated (J=0.2, h=1.0)","red","field_dominated.png")

]


# ------------------------------------------------
# Generate individual plots
# ------------------------------------------------

results=[]

for J,h,title,color,filename in cases:

    Z0_vals,Z1_vals,ZZ_vals = simulate(J,h)

    results.append((Z0_vals,Z1_vals,ZZ_vals,color,title,J,h))

    plot_single(Z0_vals,Z1_vals,ZZ_vals,title,color,filename)



# ------------------------------------------------
# Combined plot
# ------------------------------------------------

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111,projection='3d')

for Z0_vals,Z1_vals,ZZ_vals,color,title,J,h in results:

    ax.plot(
        Z0_vals,
        Z1_vals,
        ZZ_vals,
        color=color,
        linewidth=2.5,
        label=f"{title}"
    )

ax.set_xlabel(r"$\langle Z_0 \rangle$")
ax.set_ylabel(r"$\langle Z_1 \rangle$")
ax.set_zlabel(r"$\langle Z_0 Z_1 \rangle$")

ax.set_title("Quantum Dynamics for Different TFIM Regimes")

ax.legend()

ax.view_init(elev=25,azim=35)

plt.tight_layout()

plt.savefig("combined_dynamics.png",dpi=300)

plt.show()
