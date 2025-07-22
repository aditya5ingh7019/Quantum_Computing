from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import numpy as np
import matplotlib.pyplot as plt

# Define the complex imbalanced state: (1/√10)|0⟩ + (3i/√10)|1⟩
alpha = 1 / np.sqrt(10)             # real part for |0⟩
beta = 3j / np.sqrt(10)             # imaginary part for |1⟩

# Create the statevector
state = Statevector([alpha, beta])

# Plot the Bloch sphere
fig = plot_bloch_multivector(state, title="Bloch Sphere: Complex Imbalanced State")
plt.tight_layout()
plt.show()

# save to image folder
fig.savefig("images/bloch_complex.png", dpi=300)

