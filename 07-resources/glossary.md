# Quantum Computing Glossary

A comprehensive A-Z guide to quantum computing terminology.

---

## A

### Algorithm
A step-by-step procedure for solving a problem. In quantum computing, algorithms exploit quantum phenomena like superposition and entanglement.

### Amplitude
The complex number coefficient in a quantum state's superposition. The square of the amplitude's magnitude gives the probability of measuring that state.

### Ancilla Qubit
An auxiliary qubit used temporarily during computation, then returned to its initial state. Often used in error correction and complex gate operations.

---

## B

### Bell State
One of four maximally entangled two-qubit states:
- |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
- |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
- |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2  
- |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2

Named after physicist John Stewart Bell.

### Bit
Classical unit of information, either 0 or 1. Short for "binary digit."

### Bloch Sphere
A geometric representation of a single qubit state as a point on a unit sphere. The north pole represents |0⟩, south pole |1⟩, and other points represent superpositions.

### Born Rule
The fundamental postulate connecting quantum states to measurement probabilities: P(outcome) = |amplitude|²

### Bra-Ket Notation
Standard notation in quantum mechanics:
- |ψ⟩ (ket): A quantum state vector
- ⟨ψ| (bra): The conjugate transpose
- ⟨φ|ψ⟩ (bracket): Inner product

---

## C

### Circuit Depth
The number of time steps required to execute a quantum circuit, when gates can be parallelized. Important for NISQ devices with limited coherence time.

### Classical Bit
See: Bit

### CNOT Gate
Controlled-NOT gate. A two-qubit gate that flips the target qubit if the control qubit is |1⟩. Essential for creating entanglement.

### Coherence
The preservation of quantum superposition. Coherence time is how long a qubit maintains its quantum state before decoherence.

### Controlled Gate
A multi-qubit gate where one or more "control" qubits determine whether an operation is applied to "target" qubits.

---

## D

### Decoherence
The loss of quantum behavior due to interaction with the environment. The main challenge in building quantum computers.

### Density Matrix
A mathematical representation of a quantum state that can describe both pure and mixed states. Useful for noisy quantum systems.

### Deutsch-Jozsa Algorithm
A quantum algorithm that determines whether a function is constant or balanced with a single query, versus O(2^(n-1)) queries classically.

### Dirac Notation
See: Bra-Ket Notation

---

## E

### Eigenstate
A quantum state that remains unchanged (except for a phase factor) when a particular operator is applied.

### Eigenvalue
The factor by which an eigenstate is scaled when an operator is applied to it.

### Entanglement
A quantum phenomenon where qubits become correlated such that measuring one instantly affects the other, regardless of distance. Einstein called it "spooky action at a distance."

### EPR Paradox
Einstein-Podolsky-Rosen thought experiment questioning quantum mechanics' completeness, leading to understanding of entanglement.

### Error Correction
Techniques to protect quantum information from decoherence and other errors using multiple physical qubits to encode one logical qubit.

---

## F

### Fault-Tolerant Quantum Computing
Quantum computing with error correction, allowing computation even when individual components fail.

### Fidelity
A measure of how close a quantum state or operation is to the ideal. Gate fidelity above 99% is typically needed for error correction.

---

## G

### Gate
An operation applied to one or more qubits, analogous to logic gates in classical computing but reversible.

### Grover's Algorithm
Quantum algorithm providing quadratic speedup for unstructured search: O(√N) versus O(N) classically.

---

## H

### Hadamard Gate (H)
Single-qubit gate creating equal superposition:
- H|0⟩ = (|0⟩ + |1⟩)/√2
- H|1⟩ = (|0⟩ - |1⟩)/√2

Fundamental for many quantum algorithms.

### Hamiltonian
An operator representing the total energy of a quantum system. In quantum computing, used to describe system evolution and in algorithms like VQE.

### Hybrid Algorithm
Algorithm combining quantum and classical computing, typical of NISQ-era approaches.

---

## I

### Interference
Quantum phenomenon where probability amplitudes can add (constructive) or cancel (destructive). Key principle in quantum algorithms.

---

## K

### Ket
See: Bra-Ket Notation

---

## L

### Logical Qubit
An error-corrected qubit encoded using multiple physical qubits. Required for fault-tolerant quantum computing.

---

## M

### Measurement
The process of observing a quantum state, causing it to collapse to a definite classical value. Fundamentally probabilistic in quantum mechanics.

### Mixed State
A statistical ensemble of quantum states, described by a density matrix. Contrasts with pure states.

---

## N

### NISQ
Noisy Intermediate-Scale Quantum. Current era of quantum computing with 50-1000 noisy qubits, without full error correction.

### No-Cloning Theorem
Fundamental principle: it's impossible to create an exact copy of an arbitrary unknown quantum state.

---

## O

### Observable
A physical quantity that can be measured, represented by a Hermitian operator in quantum mechanics.

### Oracle
In quantum algorithms, a "black box" function that performs a specific query. Key component of Grover's and Deutsch-Jozsa algorithms.

---

## P

### Pauli Gates
Three fundamental single-qubit gates:
- **X (NOT)**: Bit flip |0⟩↔|1⟩
- **Y**: Bit and phase flip
- **Z**: Phase flip |1⟩→-|1⟩

### Phase
The complex angle of a quantum amplitude. Two states differing only by a global phase are physically equivalent.

### Phase Kickback
Technique where the phase of a controlled operation transfers to the control qubit. Used in many algorithms including Shor's.

### Physical Qubit
An actual qubit implementation (superconducting, ion trap, etc.), subject to errors. Multiple physical qubits encode one logical qubit.

### Pure State
A quantum state that can be described by a single state vector. Contrasts with mixed states.

---

## Q

### QAOA
Quantum Approximate Optimization Algorithm. Hybrid quantum-classical algorithm for combinatorial optimization problems.

### QFT
See: Quantum Fourier Transform

### Quantum Advantage
Demonstration that a quantum computer can solve a specific problem faster than any known classical algorithm on existing hardware.

### Quantum Circuit
A sequence of quantum gates applied to qubits, analogous to classical circuits.

### Quantum Fourier Transform
Quantum analogue of the discrete Fourier transform. Key component of Shor's algorithm. Can be implemented exponentially faster than classical FFT.

### Quantum Gate
See: Gate

### Quantum Parallelism
The ability of quantum computers to evaluate a function on multiple inputs simultaneously through superposition.

### Quantum Supremacy
See: Quantum Advantage (preferred term)

### Quantum Volume
Metric combining qubit count, gate fidelity, connectivity, and other factors to benchmark quantum computer capability.

### Qubit
Quantum bit. The fundamental unit of quantum information, can exist in superposition of |0⟩ and |1⟩.

---

## R

### Register
A collection of qubits, analogous to classical registers.

### Reversible Computing
Computing where operations can be undone. All quantum gates are reversible (unitary).

### Rotation Gate
Single-qubit gate that rotates the state around an axis of the Bloch sphere. Includes Rx, Ry, Rz gates.

---

## S

### Shor's Algorithm
Quantum algorithm for factoring integers in polynomial time, exponentially faster than best known classical algorithms. Threatens current cryptography.

### Superposition
A quantum state existing in multiple classical states simultaneously, until measured.

### SWAP Gate
Two-qubit gate that exchanges the states of two qubits.

---

## T

### T Gate
Single-qubit gate applying π/4 phase rotation. With Hadamard and CNOT, forms a universal gate set.

### Tensor Product
Mathematical operation combining quantum states. n qubits form a 2^n-dimensional Hilbert space via tensor products.

### Toffoli Gate
Three-qubit controlled-controlled-NOT gate. Classical reversible gate that's also a quantum gate.

### Transpilation
Process of converting a high-level quantum circuit into the low-level gates actually available on specific hardware.

---

## U

### Unitary Operation
A reversible transformation preserving probabilities (norm). All quantum gate operations are unitary.

### Universal Gate Set
A set of gates that can approximate any quantum operation to arbitrary precision. Example: {H, T, CNOT}.

---

## V

### Variational Algorithm
Hybrid quantum-classical algorithm using parameterized quantum circuits optimized by a classical computer. Examples: VQE, QAOA.

### VQE
Variational Quantum Eigensolver. Hybrid algorithm for finding ground state energies of molecules and materials.

---

## W

### Wave Function
Mathematical description of a quantum state as a function in Hilbert space.

### Wave Function Collapse
See: Measurement

---

## Additional Resources

- [IBM Quantum Composer Glossary](https://quantum.ibm.com/composer)
- [Qiskit Textbook](https://qiskit.org/textbook/)
- [Quantum Open Source Foundation](https://qosf.org/)

---

## Notation Guide

### Common Mathematical Notation

| Symbol | Meaning |
|--------|---------|
| \|ψ⟩ | Quantum state (ket) |
| ⟨ψ\| | Conjugate transpose (bra) |
| ⟨φ\|ψ⟩ | Inner product |
| ⊗ | Tensor product |
| † | Hermitian conjugate |
| Î | Identity operator |
| Û | Unitary operator |

### Common States

| Notation | Description |
|----------|-------------|
| \|0⟩ | Computational basis state zero |
| \|1⟩ | Computational basis state one |
| \|+⟩ | (|0⟩ + |1⟩)/√2 |
| \|-⟩ | (|0⟩ - |1⟩)/√2 |
| \|Φ⁺⟩ | Bell state |

---

*This glossary is continuously updated. Suggest additions via [GitHub Issues](https://github.com/manavgup/quantum-computing-101/issues).*
