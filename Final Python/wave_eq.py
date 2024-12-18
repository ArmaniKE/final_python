import math
import matplotlib.pyplot as plt

def wave_jacobi(a, nx, nt, dx, dt):
    """Метод Эйлера"""
    cfl = a * (dt**2) / (dx**2)
    if cfl > 1:
        raise ValueError("Схема неустойчива. Уменьшите dt или увеличьте nx.")
    U = [[0.0 for _ in range(nx)] for _ in range(nt)]
    for i in range(nx):
        x = i * dx
        U[0][i] = math.sin(math.pi * x)
    U[1] = U[0][:]
    for n in range(1, nt - 1):
        for i in range(1, nx - 1):
            U[n + 1][i] = 2 * U[n][i] - U[n - 1][i] + dt * (U[n][i + 1] - 2 * U[n][i] + U[n][i - 1])
    return U

def wave_euler(a, nx, nt, dx, dt):
    """Метод Эйлера"""
    cfl = a * (dt**2) / (dx**2)
    if cfl > 1:
        raise ValueError("Схема неустойчива. Уменьшите dt или увеличьте nx.")
    U = [[0.0 for _ in range(nx)] for _ in range(nt)]
    for i in range(nx):
        x = i * dx
        U[0][i] = math.sin(math.pi * x)
    U[1] = U[0][:]
    for n in range(1, nt - 1):
        for i in range(1, nx - 1):
            U[n + 1][i] = U[n][i] + dt * (U[n][i + 1] - 2 * U[n][i] + U[n][i - 1])
    return U

def plot_wave_methods(U_methods, labels, nx, nt, dx, dt):
    """Построение графиков для аналитического решения и метода Эйлера"""
    x = [i * dx for i in range(nx)]
    times_to_plot = [0, nt // 2]
    plt.figure(figsize=(12, 8))
    for idx, U in enumerate(U_methods):
        plt.plot(x, U[times_to_plot[1]], label=labels[idx])
    plt.xlabel("x")
    plt.ylabel("U(x, t)")
    plt.title("Сравнение аналитического решения и метода Эйлера")
    plt.legend()
    plt.grid()
    plt.show()
    
def wave_solver(length, duration, a, nx, nt):
    dx = length / (nx - 1)
    dt = duration / (nt - 1)
    U_jacobi = wave_jacobi(a, nx, nt, dx, dt)
    U_euler = wave_euler(a, nx, nt, dx, dt)
    plot_wave_methods(
        [U_jacobi, U_euler],
        ["Метод Якоби", "Метод Эйлера"],
        nx, nt, dx, dt)