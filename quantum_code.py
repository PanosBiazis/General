from qiskit import QuantumCircuit 

# from qiskit.algorithms import AmplificationProblem 

# from qiskit.algorithms import Grover 

from qiskit.primitives import Sampler 

from qiskit.quantum_info import Statevector 

from qiskit.circuit.library.phase_oracle import Phaseoracle 

from qiskit.exceptions import MissingoptionallibraryError 

good_state = ['11'] 

oracle = QuantumCircuit(2) 

oracle.cz(0, 1) 

problem = AmplificationProblem(oracle, is_good_state=good_state)
 
problem.grover_operator.decompose().draw(output='mpl') 

grover = Grover(sampler=Sampler()) 

result = grover.amplify(problem) 

oracle = Statevector.from_label('11') 

problem = AmplificationProblem(oracle, is_good_state=['11']) 

grover = Grover(sampler=Sampler()) 

result = grover.amplify(problem) 

expression = '(a & b)'
try: 
    oracle = PhaseOracle(expression) 
    problem = AmplificationProblem(oracle) 
    display(problem.grover_operator.oracle.decompose().draw(output='mpl')) 
except MissingOptionalLibraryError as ex: 
    print(ex) 
