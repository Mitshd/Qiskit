import numpy as np

# initialization
# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, assemble, transpile

# import basic plot tools
from qiskit.visualization import plot_histogram
from qiskit import *
n = input("number of qbits")
m = int(n)
circuit = QuantumCircuit(m,m-1)
for i in range(m-1):
    circuit.h(i)
circuit.x(m-1)
circuit.barrier()
circuit.h(m-1)
circuit.draw()
#attempt at a balanced circuit
bit_string = "101010"

for i in range(len(bit_string)):
    if bit_string[i] == "1":
        circuit.x(i)
circuit.barrier()
circuit.draw()
for i in range(m-1):
    circuit.cx(i,m-1)
circuit.draw()
circuit.barrier()

for i in range(len(bit_string)):
    if bit_string[i] == "1":
        circuit.x(i)
circuit.barrier()
#attempt at a balanced circuit end
for i in range(m-1):
    circuit.h(i)
circuit.barrier()
circuit.draw()
for i in range(m-1):
    circuit.measure(i,i)
circuit.draw()
# use local simulator
aer_sim = Aer.get_backend('aer_simulator')
qobj = assemble(circuit, aer_sim)
results = aer_sim.run(qobj).result()
answer = results.get_counts()

plot_histogram(answer)
