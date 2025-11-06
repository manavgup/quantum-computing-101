# Setup Guide: Getting Started with Quantum Programming

This guide will help you set up your development environment for quantum computing.

## 🎯 Quick Start (5 minutes)

### Option 1: Cloud-Based (No Installation!)

**Best for:** Beginners, trying things out quickly

#### IBM Quantum Lab (Recommended)
1. Go to [quantum.ibm.com](https://quantum.ibm.com)
2. Create a free account
3. Access Jupyter notebooks in the cloud
4. Run on real quantum hardware!

**Pros:** 
- No installation
- Access to real quantum computers
- Free tier available
- Pre-installed libraries

#### Google Colab
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Install Qiskit in first cell: `!pip install qiskit`
3. Start coding

**Pros:**
- Familiar environment
- Free GPU access
- Easy sharing

---

## 💻 Local Installation (15 minutes)

### Option 2: Full Local Setup

**Best for:** Developers, those doing serious work

### Prerequisites

- **Python 3.8 or higher**
  ```bash
  python --version  # Check your version
  ```

- **pip** (Python package manager)
  ```bash
  pip --version
  ```

### Step-by-Step Installation

#### 1. Create a Virtual Environment (Recommended)

**Why?** Keeps quantum packages separate from other Python projects.

```bash
# Create virtual environment
python -m venv quantum-env

# Activate it
# On macOS/Linux:
source quantum-env/bin/activate

# On Windows:
quantum-env\Scripts\activate
```

#### 2. Install Core Quantum Frameworks

```bash
# Install all at once from requirements.txt
pip install -r requirements.txt

# Or install individually:
pip install qiskit              # IBM's framework
pip install qiskit-aer          # Simulators
pip install cirq                # Google's framework
pip install pennylane           # Xanadu's framework
pip install amazon-braket-sdk   # AWS framework
```

#### 3. Install Visualization Tools

```bash
pip install matplotlib plotly jupyter
```

#### 4. Verify Installation

```python
# test_install.py
import qiskit
import cirq
import pennylane as qml

print(f"Qiskit version: {qiskit.__version__}")
print(f"Cirq version: {cirq.__version__}")
print(f"PennyLane version: {qml.__version__}")
print("✅ All frameworks installed successfully!")
```

Run it:
```bash
python test_install.py
```

---

## 🚀 Framework-Specific Setup

### Qiskit (IBM)

#### Get IBM Quantum Access

1. **Create Account**: [quantum.ibm.com](https://quantum.ibm.com)
2. **Get API Token**: From your account settings
3. **Save Token**:

```python
from qiskit_ibm_runtime import QiskitRuntimeService

# One-time setup
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="YOUR_TOKEN_HERE"
)
```

#### First Qiskit Circuit

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

# Simulate
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print(counts)  # Should see ~500 '00' and ~500 '11'
```

### Cirq (Google)

#### First Cirq Circuit

```python
import cirq

# Create qubits
q0, q1 = cirq.LineQubit.range(2)

# Create circuit
circuit = cirq.Circuit(
    cirq.H(q0),
    cirq.CNOT(q0, q1),
    cirq.measure(q0, q1, key='result')
)

# Simulate
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)
print(result.histogram(key='result'))
```

### PennyLane (Xanadu)

#### First PennyLane Circuit

```python
import pennylane as qml

# Create device
dev = qml.device('default.qubit', wires=2)

# Define quantum function
@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

# Run
print(circuit())  # [0.5, 0, 0, 0.5]
```

---

## 🔧 IDE Setup

### VS Code (Recommended)

1. **Install VS Code**: [code.visualstudio.com](https://code.visualstudio.com)

2. **Install Extensions**:
   - Python (Microsoft)
   - Jupyter (Microsoft)
   - Qiskit Snippet (Optional)

3. **Configure**:
   ```json
   // settings.json
   {
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "jupyter.askForKernelRestart": false
   }
   ```

### Jupyter Notebook

```bash
# Install Jupyter
pip install jupyter notebook

# Launch
jupyter notebook

# Or use JupyterLab (modern interface)
pip install jupyterlab
jupyter lab
```

### PyCharm

1. Install PyCharm (Community or Professional)
2. Create new project with quantum-env interpreter
3. Install Jupyter plugin for notebook support

---

## 📊 Visualization Setup

### Qiskit Visualizations

```python
# Circuit drawing
qc.draw('mpl')  # Matplotlib style
qc.draw('text') # ASCII art (works everywhere)

# Statevector
from qiskit.quantum_info import Statevector
state = Statevector.from_instruction(qc)
state.draw('bloch')  # Bloch sphere

# Histogram
from qiskit.visualization import plot_histogram
plot_histogram(counts)
```

### Interactive Tools

```bash
# Install interactive widgets
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension

# Install Qiskit visualization tools
pip install pylatexenc  # For LaTeX rendering
```

---

## 🧪 Testing Your Setup

### Complete Test Script

Save as `test_quantum_setup.py`:

```python
#!/usr/bin/env python3
"""Test quantum computing setup"""

def test_imports():
    """Test that all packages import correctly"""
    print("Testing imports...")
    try:
        import qiskit
        import cirq
        import pennylane
        import numpy
        import matplotlib
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_qiskit():
    """Test Qiskit functionality"""
    print("\nTesting Qiskit...")
    try:
        from qiskit import QuantumCircuit
        from qiskit_aer import AerSimulator
        
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        
        simulator = AerSimulator()
        job = simulator.run(qc, shots=100)
        result = job.result()
        counts = result.get_counts()
        
        print(f"   Results: {counts}")
        print("✅ Qiskit working")
        return True
    except Exception as e:
        print(f"❌ Qiskit failed: {e}")
        return False

def test_cirq():
    """Test Cirq functionality"""
    print("\nTesting Cirq...")
    try:
        import cirq
        
        q = cirq.LineQubit(0)
        circuit = cirq.Circuit(
            cirq.H(q),
            cirq.measure(q, key='m')
        )
        
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=100)
        
        print(f"   Results: {result.histogram(key='m')}")
        print("✅ Cirq working")
        return True
    except Exception as e:
        print(f"❌ Cirq failed: {e}")
        return False

def test_visualization():
    """Test visualization capabilities"""
    print("\nTesting visualization...")
    try:
        import matplotlib.pyplot as plt
        from qiskit import QuantumCircuit
        
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        
        # This should not raise an error
        qc.draw('text')
        
        print("✅ Visualization working")
        return True
    except Exception as e:
        print(f"❌ Visualization failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Quantum Computing Setup Test")
    print("=" * 50)
    
    results = [
        test_imports(),
        test_qiskit(),
        test_cirq(),
        test_visualization()
    ]
    
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 All tests passed! You're ready to go!")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    print("=" * 50)
```

Run it:
```bash
python test_quantum_setup.py
```

---

## 🐛 Troubleshooting

### Common Issues

#### "No module named 'qiskit'"
```bash
# Make sure virtual environment is activated
source quantum-env/bin/activate  # macOS/Linux
quantum-env\Scripts\activate     # Windows

# Reinstall
pip install --upgrade qiskit
```

#### "Microsoft Visual C++ required" (Windows)
- Install: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

#### "Command 'python' not found"
```bash
# Try python3 instead
python3 --version
python3 -m pip install qiskit
```

#### Jupyter Kernel Issues
```bash
# Register kernel
python -m ipykernel install --user --name=quantum-env

# Then select "quantum-env" kernel in Jupyter
```

#### Import Errors After Installation
```bash
# Upgrade pip first
pip install --upgrade pip

# Clear cache and reinstall
pip cache purge
pip install --force-reinstall qiskit
```

---

## 📦 Optional Tools

### Advanced Visualization
```bash
pip install qiskit[visualization]
pip install plotly  # Interactive plots
```

### Performance
```bash
pip install qiskit-aer-gpu  # GPU-accelerated simulators
```

### Development Tools
```bash
pip install pytest          # Testing
pip install black           # Code formatting
pip install jupyter-book    # Documentation
```

---

## 🎓 Next Steps

Now that you're set up:

1. **Try the notebooks**: Go to [`06-hands-on/notebooks/`](../notebooks/)
2. **Start simple**: [Your First Quantum Circuit](../notebooks/01-first-quantum-circuit.ipynb)
3. **Explore**: Try different frameworks
4. **Build**: Create your own circuits

---

## 📚 Quick Reference

### Useful Commands

```bash
# Activate environment
source quantum-env/bin/activate

# Update packages
pip install --upgrade qiskit cirq pennylane

# List installed packages
pip list | grep -i quantum

# Save environment
pip freeze > requirements.txt

# Recreate environment
pip install -r requirements.txt

# Deactivate environment
deactivate
```

### Useful Links

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Cirq Documentation](https://quantumai.google/cirq)
- [PennyLane Documentation](https://pennylane.ai/)
- [IBM Quantum](https://quantum.ibm.com)

---

## 💬 Getting Help

- **Qiskit Slack**: [qiskit.slack.com](https://qiskit.slack.com)
- **Stack Overflow**: Tag with `qiskit`, `cirq`, or `quantum-computing`
- **This Repo**: [Open an issue](https://github.com/manavgup/quantum-computing-101/issues)

---

**Ready to start coding?** Head to [Your First Quantum Circuit](../notebooks/01-first-quantum-circuit.ipynb)! 🚀
