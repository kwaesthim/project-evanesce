# Attempted Qubit simulation (non-functional)
import numpy as np

def broken_qubit_state():
    # Should create superposition but fails
    alpha = np.sqrt(0.5)
    beta = 1 - alpha  # Wrong: Should be sqrt(0.5)
    qubit = np.array([alpha, beta])  # Not normalized
    return np.dot(Hadamard(), qubit)

def Hadamard():
    return np.array([[1, 1], [1, -1]])  # Missing 1/sqrt(2) factor
