#!/usr/bin/env python3
"""
Generate comprehensive visualizations for The Qubit article.

This script creates code-driven illustrations for:
1. Classical bit vs quantum bit comparison
2. Bloch sphere with annotations
3. State vector visualization
4. Qubit gate transformations
5. Superposition concept
6. Measurement collapse
7. Multi-qubit state space growth
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch
from mpl_toolkits.mplot3d import proj3d, Axes3D
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere
import warnings
warnings.filterwarnings('ignore')

# Set style for professional appearance
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

import os

# Get the absolute path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'docs', 'foundations', 'illustrations') + '/'

def generate_classical_vs_quantum_bit():
    """Generate side-by-side comparison of classical bit and quantum bit."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Classical Bit
    ax1.set_xlim(-1, 5)
    ax1.set_ylim(-1, 5)
    ax1.axis('off')
    ax1.set_title('Classical Bit: Definite State', fontsize=16, fontweight='bold', pad=20)

    # Two boxes for 0 and 1
    box_0 = FancyBboxPatch((0.5, 2.5), 1.5, 1.5, boxstyle="round,pad=0.1",
                           edgecolor='#2E86AB', facecolor='#A8DADC', linewidth=3)
    box_1 = FancyBboxPatch((3, 2.5), 1.5, 1.5, boxstyle="round,pad=0.1",
                           edgecolor='gray', facecolor='white', linewidth=2, linestyle='--')
    ax1.add_patch(box_0)
    ax1.add_patch(box_1)

    ax1.text(1.25, 3.25, '0', fontsize=40, ha='center', va='center', fontweight='bold', color='#1D3557')
    ax1.text(3.75, 3.25, '1', fontsize=40, ha='center', va='center', color='gray')

    ax1.text(1.25, 1.8, 'Active', fontsize=12, ha='center', fontweight='bold', color='#2E86AB')
    ax1.text(3.75, 1.8, 'Inactive', fontsize=12, ha='center', color='gray')

    ax1.text(2.5, 0.5, 'At any moment: Either 0 OR 1', fontsize=12, ha='center',
             style='italic', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Quantum Bit
    ax2.set_xlim(-1, 5)
    ax2.set_ylim(-1, 5)
    ax2.axis('off')
    ax2.set_title('Quantum Bit: Superposition', fontsize=16, fontweight='bold', pad=20)

    # Two overlapping boxes with transparency
    box_q0 = FancyBboxPatch((0.5, 2.5), 1.5, 1.5, boxstyle="round,pad=0.1",
                           edgecolor='#E63946', facecolor='#F4A6A3', linewidth=3, alpha=0.7)
    box_q1 = FancyBboxPatch((3, 2.5), 1.5, 1.5, boxstyle="round,pad=0.1",
                           edgecolor='#E63946', facecolor='#F4A6A3', linewidth=3, alpha=0.7)
    ax2.add_patch(box_q0)
    ax2.add_patch(box_q1)

    ax2.text(1.25, 3.25, '0', fontsize=40, ha='center', va='center', fontweight='bold', color='#E63946')
    ax2.text(3.75, 3.25, '1', fontsize=40, ha='center', va='center', fontweight='bold', color='#E63946')

    # Plus sign between them
    ax2.text(2.5, 3.25, '+', fontsize=30, ha='center', va='center', fontweight='bold', color='#E63946')

    ax2.text(1.25, 1.8, 'Active', fontsize=12, ha='center', fontweight='bold', color='#E63946')
    ax2.text(3.75, 1.8, 'Active', fontsize=12, ha='center', fontweight='bold', color='#E63946')

    ax2.text(2.5, 0.5, 'Before measurement: Both 0 AND 1\n|ψ⟩ = α|0⟩ + β|1⟩',
             fontsize=12, ha='center', style='italic',
             bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.8))

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}classical-vs-quantum-bit.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated classical-vs-quantum-bit.png")


def generate_bloch_sphere_annotated():
    """Generate detailed annotated Bloch sphere showing geometry."""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Draw sphere
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.2, edgecolor='none')

    # Draw axes
    ax.plot([-1.3, 1.3], [0, 0], [0, 0], 'k-', linewidth=2, alpha=0.6)
    ax.plot([0, 0], [-1.3, 1.3], [0, 0], 'k-', linewidth=2, alpha=0.6)
    ax.plot([0, 0], [0, 0], [-1.3, 1.3], 'k-', linewidth=2, alpha=0.6)

    # Label axes
    ax.text(1.5, 0, 0, 'X', fontsize=16, fontweight='bold', color='red')
    ax.text(0, 1.5, 0, 'Y', fontsize=16, fontweight='bold', color='green')
    ax.text(0, 0, 1.5, 'Z', fontsize=16, fontweight='bold', color='blue')

    # Mark poles
    ax.scatter([0], [0], [1], color='blue', s=200, marker='o', edgecolors='darkblue', linewidths=2)
    ax.scatter([0], [0], [-1], color='red', s=200, marker='o', edgecolors='darkred', linewidths=2)

    ax.text(0, 0, 1.3, '|0⟩', fontsize=18, ha='center', fontweight='bold', color='blue')
    ax.text(0, 0, -1.3, '|1⟩', fontsize=18, ha='center', fontweight='bold', color='red')

    # Mark equator points
    ax.scatter([1], [0], [0], color='purple', s=150, marker='o', alpha=0.8)
    ax.scatter([-1], [0], [0], color='purple', s=150, marker='o', alpha=0.8)
    ax.scatter([0], [1], [0], color='orange', s=150, marker='o', alpha=0.8)
    ax.scatter([0], [-1], [0], color='orange', s=150, marker='o', alpha=0.8)

    ax.text(1.2, 0, 0, '|+⟩', fontsize=14, color='purple', fontweight='bold')
    ax.text(-1.2, 0, 0, '|−⟩', fontsize=14, color='purple', fontweight='bold')
    ax.text(0, 1.2, 0, '|↻⟩', fontsize=14, color='orange', fontweight='bold')
    ax.text(0, -1.2, 0, '|↺⟩', fontsize=14, color='orange', fontweight='bold')

    # Draw an arbitrary state vector
    theta, phi = np.pi/4, np.pi/3
    state_x = np.sin(theta) * np.cos(phi)
    state_y = np.sin(theta) * np.sin(phi)
    state_z = np.cos(theta)

    ax.quiver(0, 0, 0, state_x, state_y, state_z,
              arrow_length_ratio=0.15, color='darkgreen', linewidth=3, alpha=0.9)
    ax.text(state_x*1.2, state_y*1.2, state_z*1.2, '|ψ⟩',
            fontsize=14, fontweight='bold', color='darkgreen')

    # Add angles
    arc_theta = np.linspace(0, theta, 20)
    arc_x = 0.3 * np.sin(arc_theta) * np.cos(phi)
    arc_y = 0.3 * np.sin(arc_theta) * np.sin(phi)
    arc_z = 0.3 * np.cos(arc_theta)
    ax.plot(arc_x, arc_y, arc_z, 'g--', linewidth=2, alpha=0.7)
    ax.text(0.15, 0.1, 0.35, 'θ', fontsize=12, color='darkgreen', fontweight='bold')

    # Projection on XY plane
    ax.plot([state_x, state_x], [state_y, state_y], [0, state_z],
            'g--', linewidth=1, alpha=0.5)
    ax.plot([0, state_x], [0, state_y], [0, 0], 'g--', linewidth=2, alpha=0.7)

    # Phi angle
    arc_phi = np.linspace(0, phi, 20)
    arc_phi_x = 0.3 * np.cos(arc_phi)
    arc_phi_y = 0.3 * np.sin(arc_phi)
    arc_phi_z = np.zeros_like(arc_phi)
    ax.plot(arc_phi_x, arc_phi_y, arc_phi_z, 'm--', linewidth=2, alpha=0.7)
    ax.text(0.2, 0.15, 0, 'φ', fontsize=12, color='magenta', fontweight='bold')

    ax.set_xlabel('X', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y', fontsize=12, fontweight='bold')
    ax.set_zlabel('Z', fontsize=12, fontweight='bold')
    ax.set_title('The Bloch Sphere: Complete Geometry\n|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩',
                 fontsize=14, fontweight='bold', pad=20)

    ax.set_box_aspect([1,1,1])
    ax.view_init(elev=20, azim=45)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}bloch-sphere-annotated.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated bloch-sphere-annotated.png")


def generate_state_vector_visualization():
    """Generate visualization of qubit state vector with amplitude bars."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Three different states
    states = [
        (np.array([1, 0]), '|0⟩: Definite State', '#2E86AB'),
        (np.array([1/np.sqrt(2), 1/np.sqrt(2)]), '|+⟩: Equal Superposition', '#E63946'),
        (np.array([0.6, 0.8]), 'Custom: α|0⟩ + β|1⟩', '#06A77D')
    ]

    for idx, (state, title, color) in enumerate(states):
        ax = axes[idx]

        # Amplitude bars
        amplitudes = state
        probabilities = np.abs(amplitudes)**2

        bars = ax.bar(['|0⟩', '|1⟩'], amplitudes, color=[color, color],
                      alpha=0.7, edgecolor='black', linewidth=2)

        # Add probability labels on bars
        for i, (amp, prob) in enumerate(zip(amplitudes, probabilities)):
            ax.text(i, amp + 0.05, f'α = {amp:.3f}\nP = {prob:.3f}',
                   ha='center', fontsize=10, fontweight='bold')

        ax.set_ylabel('Amplitude', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=13, fontweight='bold', pad=10)
        ax.set_ylim(0, 1.2)
        ax.grid(axis='y', alpha=0.3)

        # Add normalization check
        norm = np.sum(probabilities)
        ax.text(0.5, -0.15, f'|α|² + |β|² = {norm:.3f}',
               ha='center', transform=ax.transAxes, fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.suptitle('Qubit State Vector Representation', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}state-vector-visualization.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated state-vector-visualization.png")


def generate_measurement_collapse():
    """Generate visualization showing measurement collapse."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Before measurement
    ax1 = axes[0]
    ax1.set_xlim(-0.5, 1.5)
    ax1.set_ylim(0, 1.2)
    ax1.bar([0, 1], [0.6, 0.8], color=['#A8DADC', '#F4A6A3'],
            edgecolor='black', linewidth=2, alpha=0.8)
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(['|0⟩', '|1⟩'], fontsize=14, fontweight='bold')
    ax1.set_ylabel('Amplitude', fontsize=12, fontweight='bold')
    ax1.set_title('Before Measurement\nSuperposition State', fontsize=13, fontweight='bold')
    ax1.text(0, 0.65, 'α=0.6', ha='center', fontsize=11, fontweight='bold')
    ax1.text(1, 0.85, 'β=0.8', ha='center', fontsize=11, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)

    # Measurement arrow
    ax2 = axes[1]
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.annotate('', xy=(0.8, 0.5), xytext=(0.2, 0.5),
                arrowprops=dict(arrowstyle='->', lw=4, color='#E63946'))
    ax2.text(0.5, 0.65, 'MEASURE', ha='center', fontsize=14, fontweight='bold', color='#E63946')
    ax2.text(0.5, 0.35, 'P(0) = 36%\nP(1) = 64%', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # After measurement (collapsed to |1⟩)
    ax3 = axes[2]
    ax3.set_xlim(-0.5, 1.5)
    ax3.set_ylim(0, 1.2)
    bars = ax3.bar([0, 1], [0, 1], color=['lightgray', '#E63946'],
            edgecolor='black', linewidth=2)
    bars[0].set_alpha(0.3)
    bars[1].set_alpha(0.9)
    ax3.set_xticks([0, 1])
    ax3.set_xticklabels(['|0⟩', '|1⟩'], fontsize=14, fontweight='bold')
    ax3.set_ylabel('Amplitude', fontsize=12, fontweight='bold')
    ax3.set_title('After Measurement\nCollapsed to |1⟩', fontsize=13, fontweight='bold')
    ax3.text(1, 1.05, 'α=1', ha='center', fontsize=11, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    ax3.text(0.5, -0.15, 'Superposition destroyed!', ha='center',
            transform=ax3.transAxes, fontsize=11, style='italic', color='#E63946',
            bbox=dict(boxstyle='round', facecolor='#FFE5E5', alpha=0.8))

    plt.suptitle('Quantum Measurement: Collapse of Superposition',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}measurement-collapse.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated measurement-collapse.png")


def generate_multi_qubit_growth():
    """Generate visualization showing exponential growth of state space."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Bar chart showing state space growth
    n_qubits = np.arange(1, 11)
    classical_states = 2**n_qubits

    ax1.bar(n_qubits, classical_states, color='#457B9D', alpha=0.8,
            edgecolor='black', linewidth=2)
    ax1.set_xlabel('Number of Qubits', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Number of States\n(Simultaneously Accessible)', fontsize=13, fontweight='bold')
    ax1.set_title('Exponential Growth: 2ⁿ States', fontsize=14, fontweight='bold')
    ax1.set_xticks(n_qubits)
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_yscale('log')

    # Add value labels on bars
    for i, (n, states) in enumerate(zip(n_qubits, classical_states)):
        if n <= 7:
            ax1.text(n, states, f'{states}', ha='center', va='bottom',
                    fontsize=9, fontweight='bold')

    # Comparison table
    ax2.axis('off')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)

    table_data = [
        ['Qubits', 'Classical\nBits Needed', 'States', 'Quantum\nAdvantage'],
        ['1', '2', '2', '2×'],
        ['2', '4', '4', '2×'],
        ['3', '8', '8', '2.67×'],
        ['5', '32', '32', '6.4×'],
        ['10', '1,024', '1,024', '102×'],
        ['20', '1,048,576', '1,048,576', '52,429×'],
        ['50', '≈10¹⁵', '≈10¹⁵', '≈10¹³×'],
    ]

    table = ax2.table(cellText=table_data, cellLoc='center', loc='center',
                     bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)

    # Style header row
    for i in range(4):
        cell = table[(0, i)]
        cell.set_facecolor('#1D3557')
        cell.set_text_props(weight='bold', color='white')

    # Style data rows
    for i in range(1, 8):
        for j in range(4):
            cell = table[(i, j)]
            if i % 2 == 0:
                cell.set_facecolor('#F1FAEE')
            else:
                cell.set_facecolor('white')
            if j == 3:  # Highlight advantage column
                cell.set_facecolor('#E5F5E0')
                cell.set_text_props(weight='bold', color='#2D6A4F')

    ax2.set_title('Classical vs Quantum State Representation',
                 fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}multi-qubit-growth.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated multi-qubit-growth.png")


def generate_gate_transformation_sequence():
    """Generate step-by-step gate transformation visualization."""
    fig, axes = plt.subplots(1, 4, figsize=(18, 5))

    gates_sequence = [
        ('|0⟩\nInitial', [1, 0], '#2E86AB'),
        ('H gate\n|+⟩', [1/np.sqrt(2), 1/np.sqrt(2)], '#E63946'),
        ('Z gate\n|−⟩', [1/np.sqrt(2), -1/np.sqrt(2)], '#F77F00'),
        ('H gate\n|1⟩', [0, 1], '#06A77D'),
    ]

    for idx, (title, state, color) in enumerate(gates_sequence):
        ax = axes[idx]

        # Amplitude bars (handling negative values)
        amplitudes = np.array(state)
        bars = ax.bar(['|0⟩', '|1⟩'], amplitudes, color=[color, color],
                      alpha=0.8, edgecolor='black', linewidth=2)

        # Add labels
        for i, amp in enumerate(amplitudes):
            y_pos = amp + 0.05 if amp >= 0 else amp - 0.05
            va = 'bottom' if amp >= 0 else 'top'
            ax.text(i, y_pos, f'{amp:.3f}', ha='center', va=va,
                   fontsize=10, fontweight='bold')

        ax.set_ylabel('Amplitude', fontsize=11, fontweight='bold')
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_ylim(-1, 1)
        ax.axhline(y=0, color='black', linewidth=0.5)
        ax.grid(axis='y', alpha=0.3)

        # Add arrow to next state
        if idx < 3:
            ax.annotate('', xy=(1.15, 0.5), xytext=(1.05, 0.5),
                       xycoords=('axes fraction', 'axes fraction'),
                       arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

    plt.suptitle('Gate Transformation Sequence: |0⟩ → H → Z → H → |1⟩',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}gate-transformation-sequence.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated gate-transformation-sequence.png")


if __name__ == '__main__':
    print("Generating qubit visualizations...")
    print(f"Output directory: {OUTPUT_DIR}")

    generate_classical_vs_quantum_bit()
    generate_bloch_sphere_annotated()
    generate_state_vector_visualization()
    generate_measurement_collapse()
    generate_multi_qubit_growth()
    generate_gate_transformation_sequence()

    print("\n✓ All visualizations generated successfully!")
    print(f"Files saved to: {OUTPUT_DIR}")
