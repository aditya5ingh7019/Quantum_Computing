




# Quantum Circuit Simulation using Qiskit

This project demonstrates a simple 1-qubit quantum circuit using Qiskit.
It applies an X gate followed by a Hadamard gate and then simulates the resulting state using different backends:
- Statevector simulator
- BasicSimulator
- AerSimulator
- IBM Runtime SamplerV2

The output shows:
- Statevector of the qubit
- Probability distributions
- Measurement results
- Histogram of outcomes

## Requirements

- Python 3.x
- qiskit
- matplotlib
- qiskit-aer
- qiskit-ibm-runtime

## How to Run

```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime matplotlib
python quantum_circuit_simulation.py
