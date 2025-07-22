




import qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.providers.basic_provider import BasicSimulator
from  qiskit_ibm_runtime import SamplerV2
from qiskit.visualization import plot_histogram

qc = qiskit.QuantumCircuit(1)

qc.x(0)
qc.h(0)

print(qc.draw())

q = Statevector(qc)
print(q)

print(q.probabilities())

print(q.sample_counts(100))


# Show matrix form of the circuit (unitary operator)
U = Operator(qc)
print("Matrix (unitary operator) of the circuit:\n", U.data)

qc = qiskit.QuantumCircuit(1,1)
qc.x(0)
qc.h(0)
qc.measure(0, 0)
print(qc.draw())

sim_basic = BasicSimulator()
sim_aer = AerSimulator()

count_basic = sim_basic.run(qc, shots=100).result().get_counts()
count_aer = sim_aer.run(qc, shots=100).result().get_counts()

print(count_basic)
print(count_aer)

sam_aer = SamplerV2(mode=sim_aer)
result = sam_aer.run([qc], shots=100).result()
count_sam = result[0].data.c.get_counts()
print(count_sam)




plot_histogram(count_sam)
plt.show()