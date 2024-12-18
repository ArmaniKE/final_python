# Differential Equation Solvers

This project provides implementations of numerical methods to solve various differential equations, including the Heat Equation, Laplace Equation, and Wave Equation. A graphical user interface (GUI) built using Tkinter enables users to select and run the desired solver.

## Features

### 1. Heat Equation Solver (`heat.py`)
Solves the one-dimensional heat equation using:
- Explicit Method
- Richardson Method (improved accuracy based on the Explicit Method)

Generates and displays plots of the temperature distribution.

### 2. Laplace Equation Solver (`laplace.py`)
Solves the Laplace equation numerically for a grid with boundary conditions.
- Iterative solver with user-specified tolerance and maximum iterations.
- Displays the grid solution as a contour plot.

### 3. Wave Equation Solver (`wave_eq.py`)
Solves the one-dimensional wave equation using:
- Jacobi Method
- Euler Method

Compares solutions and visualizes results at specific time steps.

### 4. Graphical User Interface (`main.py`)
- GUI allows users to select and configure inputs for the desired equation solver.
- Displays results interactively.

## Requirements

- Python 3.x
- Required libraries: `matplotlib`, `tkinter`

Install required libraries:
```bash
pip install matplotlib
```

## Usage

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

### GUI Overview

- **Laplace Equation**: Specify grid dimensions and boundary conditions. Click "Run Laplace" to solve and visualize the result.
- **Wave Equation**: Provide length, duration, wave speed, and grid resolution parameters. Click "Run Wave Equation" to see comparisons of different methods.
- **Heat Equation**: Input thermal properties and grid configuration. Click "Run Heat Equation" to analyze the solution.

### Example Scripts (CLI)

#### Heat Equation:
```python
from heat import plot_heat_solution

plot_heat_solution(L=10, T0=100, TL=0, alpha=0.01, T_initial_value=20, Nx=50, Nt=500, dt=0.1)
```

#### Laplace Equation:
```python
from laplace import laplace_eq, visual

grid = [[100 if j == 0 else 0 for j in range(5)] for i in range(5)]
solution = laplace_eq(grid, tol=1e-5)
visual(solution)
```

#### Wave Equation:
```python
from wave_eq import wave_solver

wave_solver(length=10, duration=5, a=0.5, nx=50, nt=500)
```

## Notes
- Ensure that numerical stability conditions (e.g., CFL condition for wave and heat equations) are satisfied.
- GUI input validation checks are in place but ensure meaningful input values.

## License
This project is open-source and distributed under the MIT License.
