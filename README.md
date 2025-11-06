# Quantum Computing 101: From Fundamentals to Applications

<div align="center">

![Quantum Computing](https://img.shields.io/badge/Quantum-Computing-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A comprehensive, beginner-friendly guide to quantum computing**  
*From quantum mechanics basics through the complete quantum stack, algorithms, and real-world applications*

[Getting Started](#-getting-started) • [Learning Paths](#-learning-paths) • [Contents](#-contents) • [Contributing](#-contributing)

</div>

---

## 🌟 **About This Repository**

Welcome to **Quantum Computing 101**! This repository is designed to take you from zero to hero in quantum computing, whether you're a:

- 🎓 **Complete beginner** curious about quantum computing
- 💻 **Software developer** wanting to build quantum applications
- 🔬 **Researcher/Scientist** exploring quantum algorithms
- 💼 **Business leader** understanding quantum's potential
- 🧑‍🎓 **Student** learning quantum computing fundamentals

### **What Makes This Different?**

- ✅ **Progressive learning**: Start from basics, build up systematically
- ✅ **Visual first**: Every concept explained with clear illustrations
- ✅ **Hands-on**: Interactive Jupyter notebooks and real code examples
- ✅ **Framework agnostic**: Examples in Qiskit, Cirq, Q#, and more
- ✅ **Practical focus**: Real use cases and industry applications
- ✅ **Complete stack**: From hardware to high-level algorithms

---

## 🚀 **Getting Started**

### **Prerequisites**

- Basic understanding of programming (Python recommended)
- High school level mathematics (algebra, basic trigonometry)
- Curiosity and willingness to learn! 🧠

### **Quick Start**

1. **Choose your learning path** (see below)
2. **Start with [Foundations](./01-foundations/)** if you're new
3. **Run the notebooks** in [Hands-On](./06-hands-on/) to experiment
4. **Explore algorithms** in [Part 4](./04-algorithms/) when ready

### **Installation** (for hands-on coding)

```bash
# Clone this repository
git clone https://github.com/manavgup/quantum-computing-101.git
cd quantum-computing-101

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

---

## 🎯 **Learning Paths**

Choose the path that fits your background and goals:

### 🟢 **Path 1: Complete Beginner**
*"I'm new to quantum computing and want to start from scratch"*

1. [Why Quantum Computing?](./01-foundations/01-why-quantum.md)
2. [The Qubit](./01-foundations/04-the-qubit.md)
3. [Quantum Gates](./02-gates-and-circuits/01-single-qubit-gates.md)
4. [Your First Circuit](./06-hands-on/notebooks/01-first-quantum-circuit.ipynb) 🔬
5. [Quantum Algorithms Overview](./04-algorithms/README.md)

### 🟡 **Path 2: Software Developer**
*"I code daily and want to build quantum applications"*

1. [Classical Computing Recap](./01-foundations/02-classical-recap.md) ⚡
2. [Quantum Stack Overview](./03-quantum-stack/README.md)
3. [Frameworks Comparison](./03-quantum-stack/04-frameworks.md)
4. [Algorithm Implementations](./04-algorithms/implementations/)
5. [Hands-On Projects](./06-hands-on/) 💻

### 🔴 **Path 3: Researcher/Scientist**
*"I want deep understanding of quantum algorithms"*

1. [Quantum Mechanics Essentials](./01-foundations/03-quantum-mechanics-basics.md)
2. [Mathematical Foundations](./02-gates-and-circuits/04-circuit-identities.md)
3. [Algorithm Deep-Dives](./04-algorithms/)
4. [Research Papers](./07-resources/research-papers.md)
5. [Advanced Implementations](./06-hands-on/exercises/advanced/)

### 💼 **Path 4: Business/Executive**
*"I need to understand quantum's business impact"*

1. [Why Quantum? The Business Case](./01-foundations/01-why-quantum.md)
2. [The Quantum Stack](./03-quantum-stack/06-complete-stack.md)
3. [Industry Use Cases](./05-use-cases/)
4. [Maturity Matrix](./05-use-cases/08-maturity-matrix.md)
5. [Current Limitations](./05-use-cases/09-limitations.md)

---

## 📚 **Contents**

### **Part 1: Quantum Foundations** 🎯
*Start here if you're new to quantum computing*

- [Why Quantum Computing?](./01-foundations/01-why-quantum.md) - The motivation and quantum advantage
- [Classical Computing Recap](./01-foundations/02-classical-recap.md) - Bits, gates, and circuits
- [Quantum Mechanics Essentials](./01-foundations/03-quantum-mechanics-basics.md) - Wave-particle duality, superposition
- [The Qubit](./01-foundations/04-the-qubit.md) - Bloch sphere, quantum states
- [Quantum Entanglement](./01-foundations/05-entanglement.md) - Bell states, correlations
- [Quantum Measurement](./01-foundations/06-measurement.md) - Wave function collapse, Born rule

### **Part 2: Quantum Gates & Circuits** ⚡
*Learn the building blocks of quantum programs*

- [Single-Qubit Gates](./02-gates-and-circuits/01-single-qubit-gates.md) - Pauli, Hadamard, rotation gates
- [Multi-Qubit Gates](./02-gates-and-circuits/02-multi-qubit-gates.md) - CNOT, Toffoli, SWAP
- [Quantum Circuits](./02-gates-and-circuits/03-quantum-circuits.md) - Circuit notation and composition
- [Circuit Identities](./02-gates-and-circuits/04-circuit-identities.md) - Optimization patterns

### **Part 3: The Quantum Computing Stack** 🏗️
*Understand the complete technology stack*

- [Hardware Layer](./03-quantum-stack/01-hardware-layer.md) - Superconducting, trapped ions, photonic
- [Control & Calibration](./03-quantum-stack/02-control-calibration.md) - Pulse control, error mitigation
- [Quantum Assembly](./03-quantum-stack/03-quantum-assembly.md) - QASM, Quil, Blackbird
- [Software Frameworks](./03-quantum-stack/04-frameworks.md) - Qiskit, Cirq, Q#, PennyLane
- [Cloud Platforms](./03-quantum-stack/05-cloud-platforms.md) - IBM, AWS, Azure, Google
- [Complete Stack Diagram](./03-quantum-stack/06-complete-stack.md) - The full picture

### **Part 4: Quantum Algorithms** 🧮
*Master the algorithms that demonstrate quantum advantage*

- [Gate-Level Primitives](./04-algorithms/01-gate-primitives.md) - QFT, phase kickback
- [Deutsch-Jozsa Algorithm](./04-algorithms/02-deutsch-jozsa.md) - First quantum advantage
- [Grover's Search](./04-algorithms/03-grovers-algorithm.md) - Quadratic speedup for search
- [Shor's Factoring](./04-algorithms/04-shors-algorithm.md) - Breaking RSA encryption
- [Quantum Phase Estimation](./04-algorithms/05-quantum-phase-estimation.md) - Eigenvalue finding
- [VQE](./04-algorithms/06-vqe.md) - Variational quantum eigensolver
- [QAOA](./04-algorithms/07-qaoa.md) - Quantum approximate optimization
- [Quantum ML](./04-algorithms/08-quantum-ml.md) - Neural networks and kernels
- [Algorithm Comparison](./04-algorithms/09-algorithm-comparison.md) - Which algorithm for what?

### **Part 5: Use Cases & Applications** 💼
*Discover how quantum computing solves real-world problems*

- [Drug Discovery & Chemistry](./05-use-cases/01-drug-discovery.md)
- [Finance](./05-use-cases/02-finance.md) - Portfolio optimization, risk analysis
- [Cryptography](./05-use-cases/03-cryptography.md) - Post-quantum cryptography
- [Optimization & Logistics](./05-use-cases/04-optimization.md)
- [Machine Learning](./05-use-cases/05-machine-learning.md)
- [Materials Science](./05-use-cases/06-materials-science.md)
- [Climate & Energy](./05-use-cases/07-climate-energy.md)
- [Maturity Matrix](./05-use-cases/08-maturity-matrix.md) - When will quantum deliver?
- [Current Limitations](./05-use-cases/09-limitations.md) - Honest assessment

### **Part 6: Hands-On Learning** 🔬
*Build and experiment with quantum circuits*

- [Setup Guide](./06-hands-on/setup-guide.md) - Get your environment ready
- **Interactive Notebooks:**
  - [Your First Quantum Circuit](./06-hands-on/notebooks/01-first-quantum-circuit.ipynb)
  - [Quantum Teleportation](./06-hands-on/notebooks/02-quantum-teleportation.ipynb)
  - [Building Grover's Algorithm](./06-hands-on/notebooks/03-grovers-step-by-step.ipynb)
  - [VQE for Hydrogen](./06-hands-on/notebooks/04-vqe-hydrogen.ipynb)
  - [Quantum Game](./06-hands-on/notebooks/05-quantum-game.ipynb)
- **Exercises:** [Beginner](./06-hands-on/exercises/beginner/) | [Intermediate](./06-hands-on/exercises/intermediate/) | [Advanced](./06-hands-on/exercises/advanced/)

### **Part 7: Resources & Community** 📖
*Curated resources for continued learning*

- [Learning Resources](./07-resources/learning-resources.md) - Courses, books, videos
- [Research Papers](./07-resources/research-papers.md) - Key papers by topic
- [Tools & Platforms](./07-resources/tools-and-platforms.md) - Access to quantum computers
- [Communities](./07-resources/communities.md) - Discord, Slack, forums
- [Glossary](./07-resources/glossary.md) - A-Z quantum terms
- [FAQ](./07-resources/faq.md) - Common questions answered

---

## 🎨 **Visual Learning**

This repository emphasizes visual explanations:

- 🎯 **Bloch Sphere** visualizations for qubit states
- 📊 **Circuit diagrams** for every algorithm
- 📈 **Infographics** for technology comparisons
- 🎬 **Animations** for quantum phenomena
- 🗺️ **Architecture diagrams** for the quantum stack

*All illustrations are SVG format for crisp rendering and included in respective folders.*

---

## 🛠️ **Technology Stack**

This repository uses:

- **Python 3.8+** for code examples
- **Qiskit** (IBM)
- **Cirq** (Google)
- **Q#** (Microsoft)
- **PennyLane** (Xanadu)
- **Jupyter Notebooks** for interactive learning
- **Matplotlib/Plotly** for visualizations

---

## 📈 **Progress Tracker**

Track your learning progress:

- [ ] Part 1: Foundations (6 topics)
- [ ] Part 2: Gates & Circuits (4 topics)
- [ ] Part 3: Quantum Stack (6 topics)
- [ ] Part 4: Algorithms (9 topics)
- [ ] Part 5: Use Cases (9 topics)
- [ ] Part 6: Complete all notebooks (5 notebooks)
- [ ] Part 7: Explore resources

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

- 🐛 **Report bugs** or broken links
- 💡 **Suggest improvements** to explanations
- ✍️ **Add content** (new algorithms, use cases, examples)
- 🎨 **Create illustrations** or improve existing ones
- 🧪 **Share your projects** built using this guide

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

### **Contributors**

Thanks to all contributors who help improve this resource! ⭐

---

## 📜 **License**

This project is licensed under the MIT License - see [LICENSE](./LICENSE) file for details.

---

## 🌐 **Connect & Learn More**

- 💬 **Discussions**: [GitHub Discussions](https://github.com/manavgup/quantum-computing-101/discussions)
- 🐛 **Issues**: [Report bugs or request features](https://github.com/manavgup/quantum-computing-101/issues)
- ⭐ **Star this repo** to bookmark and support the project
- 🔔 **Watch** for updates

---

## 📊 **Repository Stats**

![Stars](https://img.shields.io/github/stars/manavgup/quantum-computing-101?style=social)
![Forks](https://img.shields.io/github/forks/manavgup/quantum-computing-101?style=social)
![Issues](https://img.shields.io/github/issues/manavgup/quantum-computing-101)
![Last Commit](https://img.shields.io/github/last-commit/manavgup/quantum-computing-101)

---

## 🎓 **Learning Outcomes**

After completing this guide, you will be able to:

✅ Explain fundamental quantum mechanics concepts  
✅ Understand qubits, superposition, and entanglement  
✅ Read and write quantum circuits  
✅ Implement quantum algorithms in multiple frameworks  
✅ Understand the complete quantum computing stack  
✅ Evaluate quantum use cases for business problems  
✅ Run quantum programs on real quantum computers  
✅ Stay current with quantum computing developments  

---

## 🙏 **Acknowledgments**

Inspired by and built upon the excellent work of:
- IBM Quantum Learning
- Qiskit textbook
- Microsoft Quantum Katas
- Quantum computing research community

---

<div align="center">

**⭐ If you find this helpful, please star the repository! ⭐**

*Happy quantum computing!* 🚀

</div>
