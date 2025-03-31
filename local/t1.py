# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit #, execute, Aer
# import randrange for random choices
from random import randrange
import pylatexenc
import matplotlib.pyplot as plt


q = QuantumRegister(5)
c = ClassicalRegister(5)
qc = QuantumCircuit(q, c)

qrand = q[randrange(5)]

for i in range(5):
    qc.z(q[i])

qc.h(qrand)

qc.measure(q,c)
qc.draw(output='mpl')
