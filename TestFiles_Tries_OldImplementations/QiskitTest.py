from qiskit import QuantumCircuit, Aer, assemble
from math import pi
import numpy as np
from qiskit.visualization import plot_bloch_multivector, plot_histogram, array_to_latex

qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
qc.cx(0,1)
print(qc.draw())

svsim = Aer.get_backend('aer_simulator')
qc.save_statevector()
qobj = assemble(qc)
final_state = svsim.run(qobj).result().get_statevector()
print(array_to_latex(final_state, prefix="\\text{Statevector} = "))

x = '0123'
print(x[0:2])
n = 2
txt = '1010'
print(txt.split())
z=np.fromstring('1010',dtype='u1')-ord('0')
z.reshape(1,4)
z = -1*z
z[z==0]=1
print(z)