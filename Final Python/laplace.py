import matplotlib.pyplot as plt
import tkinter as tk

def laplace_eq(grid, tol=1e-6, max_iter=1000):
    row = len(grid)
    col = len(grid[0])
    grid2 = [i[:] for i in grid]
    for iter in range(max_iter):
        max_diff = 0
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                new_val = 0.25 * (grid[i+1][j] + grid[i-1][j] + grid[i][j+1] + grid[i][j-1])
                max_diff = max(max_diff, abs(new_val - grid2[i][j]))
                grid2[i][j] = new_val
        if max_diff < tol:
            print(f"Converged in {iter + 1} iterations")
            return grid2
        grid = [i[:] for i in grid2]
    print("Reached maximum iterations")
    return grid2

def user_inp():
    print("\nEnter the grid dimensions:")
    row = int(input("Rows: "))
    col = int(input("Columns: "))
    print("\nEnter the boundary values:")
    top = int(input("Top boundary: "))
    bottom = int(input("Bottom boundary: "))
    left = int(input("Left boundary: "))
    right = int(input("Right boundary: "))
    grid = [[0.0] * col for _ in range(row)]
    for j in range(col):
        grid[0][j] = top
        grid[-1][j] = bottom
    for i in range(row):
        grid[i][0] = left
        grid[i][-1] = right
    return grid

def print_grid(grid, title="Grid", outp=None):
    if outp:
        outp.insert(tk.END, f"\n{title}:\n")
        for i in grid:
            outp.insert(tk.END, " ".join([f"{val:6.2f}" for val in i]) + '\n')
    else:
        print(f"\n{title}:")
        for i in grid:
            print(" ".join([f"{val:6.2f}" for val in i]))

def visual(grid):
    plt.figure(figsize=(8, 6))
    cont = plt.contourf(grid, cmap='viridis', levels=1000, origin='upper')
    cbar = plt.colorbar(cont)
    cbar.set_label('Potential (phi)', rotation=270, labelpad=20)
    plt.title('Solution of the Laplace Equation', fontsize=16)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, linestyle='--', color='black', alpha=0.6)
    # plt.tight_layout()
    plt.show()