#!/usr/bin/env python3
"""
Generate Phase 1 Critical Illustrations for Part 1: Foundations

Creates 4 critical Qiskit-based visualizations:
1. Basic Bloch Sphere with Common States
2. Bell State Creation Circuit
3. Single Qubit Gates on Bloch Sphere
4. Superposition State Evolution

Requirements:
- qiskit
- matplotlib
- numpy

Usage:
    python scripts/generate_phase1_illustrations.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_vector, plot_histogram
from qiskit.quantum_info import Statevector
import warnings
warnings.filterwarnings('ignore')

# Output directory
OUTPUT_DIR = "01-foundations/illustrations"

# Standard figure settings
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.facecolor'] = 'white'

print("🎨 Generating Phase 1 Critical Illustrations...")
print("=" * 60)


# ============================================================================
# Illustration 1: Basic Bloch Sphere with Common States
# ============================================================================

def generate_bloch_sphere_basic():
    """Generate Bloch sphere showing 6 common qubit states."""
    print("\n1️⃣  Creating: Basic Bloch Sphere with Common States...")

    fig = plt.figure(figsize=(12, 10))

    # Define the 6 common states
    states = {
        '|0⟩': [0, 0, 1],      # North pole
        '|1⟩': [0, 0, -1],     # South pole
        '|+⟩': [1, 0, 0],      # +X axis
        '|-⟩': [-1, 0, 0],     # -X axis
        '|↻⟩': [0, 1, 0],      # +Y axis
        '|↺⟩': [0, -1, 0],     # -Y axis
    }

    # Create 2x3 subplot grid
    positions = [
        (0, 0, 1),  # |0⟩
        (0, 0, -1), # |1⟩
        (1, 0, 0),  # |+⟩
        (-1, 0, 0), # |-⟩
        (0, 1, 0),  # |↻⟩
        (0, -1, 0), # |↺⟩
    ]

    labels = ['|0⟩ (North)', '|1⟩ (South)', '|+⟩ (X+)', '|−⟩ (X−)',
              '|↻⟩ (Y+)', '|↺⟩ (Y−)']

    for idx, (label, vector) in enumerate(zip(labels, positions)):
        ax = fig.add_subplot(2, 3, idx + 1, projection='3d')

        # Plot Bloch sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, alpha=0.1, color='lightblue')

        # Plot axes
        ax.plot([0, 0], [0, 0], [-1.2, 1.2], 'k-', alpha=0.3, linewidth=1)
        ax.plot([-1.2, 1.2], [0, 0], [0, 0], 'k-', alpha=0.3, linewidth=1)
        ax.plot([0, 0], [-1.2, 1.2], [0, 0], 'k-', alpha=0.3, linewidth=1)

        # Label axes
        ax.text(0, 0, 1.3, 'Z', fontsize=10)
        ax.text(1.3, 0, 0, 'X', fontsize=10)
        ax.text(0, 1.3, 0, 'Y', fontsize=10)

        # Plot state vector
        ax.quiver(0, 0, 0, vector[0], vector[1], vector[2],
                 color='red', arrow_length_ratio=0.15, linewidth=3)

        # Plot equator
        theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(np.cos(theta), np.sin(theta), 0, 'b--', alpha=0.3, linewidth=1)

        ax.set_xlim([-1.2, 1.2])
        ax.set_ylim([-1.2, 1.2])
        ax.set_zlim([-1.2, 1.2])
        ax.set_box_aspect([1,1,1])
        ax.set_title(label, fontsize=12, fontweight='bold')
        ax.axis('off')

    plt.suptitle('Common Qubit States on the Bloch Sphere',
                 fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout()
    filename = f"{OUTPUT_DIR}/bloch-sphere-basic.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"   ✅ Saved: {filename}")


# ============================================================================
# Illustration 2: Bell State Creation Circuit
# ============================================================================

def generate_bell_state_circuit():
    """Generate circuit showing Bell state creation with H + CNOT."""
    print("\n2️⃣  Creating: Bell State Creation Circuit...")

    # Create circuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    # Draw circuit
    fig = qc.draw('mpl', style='iqp', fold=False)

    # Add title
    fig.suptitle('Bell State Creation: |Φ⁺⟩ = (|00⟩ + |11⟩)/√2',
                 fontsize=14, fontweight='bold', y=1.05)

    # Add annotations
    fig.text(0.5, 0.02,
             'Start: |00⟩  →  After H: (|00⟩ + |10⟩)/√2  →  After CNOT: (|00⟩ + |11⟩)/√2',
             ha='center', fontsize=10, style='italic')

    filename = f"{OUTPUT_DIR}/bell-state-circuit.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"   ✅ Saved: {filename}")


# ============================================================================
# Illustration 3: Single Qubit Gates on Bloch Sphere
# ============================================================================

def generate_gates_bloch_sphere():
    """Show X, Y, Z gate effects as rotations on Bloch sphere."""
    print("\n3️⃣  Creating: Single Qubit Gates on Bloch Sphere...")

    fig = plt.figure(figsize=(15, 5))

    gates = ['X', 'Y', 'Z']
    initial_state = [0, 0, 1]  # |0⟩ state

    # Define final states after each gate
    final_states = {
        'X': [0, 0, -1],   # X|0⟩ = |1⟩
        'Y': [0, 0, -1],   # Y|0⟩ = i|1⟩ (approximately |1⟩ on Bloch)
        'Z': [0, 0, 1],    # Z|0⟩ = |0⟩ (no change)
    }

    for idx, gate in enumerate(gates):
        ax = fig.add_subplot(1, 3, idx + 1, projection='3d')

        # Plot Bloch sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, alpha=0.1, color='lightblue')

        # Plot axes
        ax.plot([0, 0], [0, 0], [-1.2, 1.2], 'k-', alpha=0.3, linewidth=1)
        ax.plot([-1.2, 1.2], [0, 0], [0, 0], 'k-', alpha=0.3, linewidth=1)
        ax.plot([0, 0], [-1.2, 1.2], [0, 0], 'k-', alpha=0.3, linewidth=1)

        # Label axes
        ax.text(0, 0, 1.3, 'Z', fontsize=10)
        ax.text(1.3, 0, 0, 'X', fontsize=10)
        ax.text(0, 1.3, 0, 'Y', fontsize=10)

        # Plot initial state
        ax.quiver(0, 0, 0, initial_state[0], initial_state[1], initial_state[2],
                 color='blue', arrow_length_ratio=0.15, linewidth=2,
                 label='Initial |0⟩')

        # Plot final state
        final = final_states[gate]
        ax.quiver(0, 0, 0, final[0], final[1], final[2],
                 color='red', arrow_length_ratio=0.15, linewidth=3,
                 label=f'After {gate}')

        # Plot rotation axis
        if gate == 'X':
            ax.plot([0, 1.5], [0, 0], [0, 0], 'g--', linewidth=2, alpha=0.7, label='Rotation axis')
        elif gate == 'Y':
            ax.plot([0, 0], [0, 1.5], [0, 0], 'g--', linewidth=2, alpha=0.7, label='Rotation axis')
        elif gate == 'Z':
            ax.plot([0, 0], [0, 0], [0, 1.5], 'g--', linewidth=2, alpha=0.7, label='Rotation axis')

        ax.set_xlim([-1.2, 1.2])
        ax.set_ylim([-1.2, 1.2])
        ax.set_zlim([-1.2, 1.2])
        ax.set_box_aspect([1,1,1])
        ax.set_title(f'{gate} Gate (π rotation around {gate}-axis)',
                    fontsize=12, fontweight='bold')
        ax.legend(loc='upper left', fontsize=8)
        ax.axis('off')

    plt.suptitle('Pauli Gates as Rotations on the Bloch Sphere',
                 fontsize=16, fontweight='bold', y=0.95)

    filename = f"{OUTPUT_DIR}/gates-bloch-sphere.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"   ✅ Saved: {filename}")


# ============================================================================
# Illustration 4: Superposition State Evolution
# ============================================================================

def generate_superposition_evolution():
    """Show |0⟩ → H → |+⟩ with Bloch sphere and measurement histogram."""
    print("\n4️⃣  Creating: Superposition State Evolution...")

    fig = plt.figure(figsize=(15, 5))

    # Left: Initial state |0⟩
    ax1 = fig.add_subplot(1, 3, 1, projection='3d')
    state_0 = [0, 0, 1]

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax1.plot_surface(x, y, z, alpha=0.1, color='lightblue')
    ax1.plot([0, 0], [0, 0], [-1.2, 1.2], 'k-', alpha=0.3)
    ax1.plot([-1.2, 1.2], [0, 0], [0, 0], 'k-', alpha=0.3)
    ax1.plot([0, 0], [-1.2, 1.2], [0, 0], 'k-', alpha=0.3)
    ax1.quiver(0, 0, 0, state_0[0], state_0[1], state_0[2],
              color='blue', arrow_length_ratio=0.15, linewidth=3)
    ax1.text(0, 0, 1.3, 'Z', fontsize=10)
    ax1.text(1.3, 0, 0, 'X', fontsize=10)
    ax1.text(0, 1.3, 0, 'Y', fontsize=10)
    ax1.set_xlim([-1.2, 1.2])
    ax1.set_ylim([-1.2, 1.2])
    ax1.set_zlim([-1.2, 1.2])
    ax1.set_box_aspect([1,1,1])
    ax1.set_title('Initial State: |0⟩', fontsize=12, fontweight='bold')
    ax1.axis('off')

    # Middle: After H gate |+⟩
    ax2 = fig.add_subplot(1, 3, 2, projection='3d')
    state_plus = [1, 0, 0]  # |+⟩ on equator, X-axis

    ax2.plot_surface(x, y, z, alpha=0.1, color='lightblue')
    ax2.plot([0, 0], [0, 0], [-1.2, 1.2], 'k-', alpha=0.3)
    ax2.plot([-1.2, 1.2], [0, 0], [0, 0], 'k-', alpha=0.3)
    ax2.plot([0, 0], [-1.2, 1.2], [0, 0], 'k-', alpha=0.3)
    ax2.quiver(0, 0, 0, state_plus[0], state_plus[1], state_plus[2],
              color='red', arrow_length_ratio=0.15, linewidth=3)

    # Highlight equator
    theta = np.linspace(0, 2*np.pi, 100)
    ax2.plot(np.cos(theta), np.sin(theta), 0, 'r--', alpha=0.5, linewidth=2)

    ax2.text(0, 0, 1.3, 'Z', fontsize=10)
    ax2.text(1.3, 0, 0, 'X', fontsize=10)
    ax2.text(0, 1.3, 0, 'Y', fontsize=10)
    ax2.set_xlim([-1.2, 1.2])
    ax2.set_ylim([-1.2, 1.2])
    ax2.set_zlim([-1.2, 1.2])
    ax2.set_box_aspect([1,1,1])
    ax2.set_title('After H Gate: |+⟩ = (|0⟩+|1⟩)/√2', fontsize=12, fontweight='bold')
    ax2.axis('off')

    # Right: Measurement histogram
    ax3 = fig.add_subplot(1, 3, 3)

    # Create and run circuit
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    backend = AerSimulator()
    job = backend.run(qc, shots=1000)
    counts = job.result().get_counts()

    # Plot histogram
    states = ['0', '1']
    values = [counts.get('0', 0), counts.get('1', 0)]
    colors = ['steelblue', 'coral']

    bars = ax3.bar(states, values, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax3.set_xlabel('Measurement Outcome', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Counts (out of 1000 shots)', fontsize=11, fontweight='bold')
    ax3.set_title('Measurement Results', fontsize=12, fontweight='bold')
    ax3.set_ylim([0, 600])
    ax3.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}\n(~50%)',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.suptitle('Creating Superposition with Hadamard Gate',
                 fontsize=16, fontweight='bold', y=0.98)

    filename = f"{OUTPUT_DIR}/superposition-evolution.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"   ✅ Saved: {filename}")


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    try:
        # Generate all Phase 1 illustrations
        generate_bloch_sphere_basic()
        generate_bell_state_circuit()
        generate_gates_bloch_sphere()
        generate_superposition_evolution()

        print("\n" + "=" * 60)
        print("✅ Phase 1 Critical Illustrations Complete!")
        print(f"📁 All files saved to: {OUTPUT_DIR}/")
        print("\nFiles created:")
        print("  1. bloch-sphere-basic.png")
        print("  2. bell-state-circuit.png")
        print("  3. gates-bloch-sphere.png")
        print("  4. superposition-evolution.png")
        print("\n🎯 Ready to integrate into markdown files!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
