try:
    import cirq
    # if isinstance(cirq, bool) and cirq == True:
    #     print("Cirq is installed")
    if 'cirq' in globals():
        print("Cirq is installed")
except ImportError:
    print("Cirq is not installed. Install it with 'pip install cirq'")
    raise

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit that applies a square root of NOT gate, then measures the qubit.
circuit = cirq.Circuit(cirq.X(qubit) ** 0.5, cirq.measure(qubit, key='m'))
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)
