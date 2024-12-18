import matplotlib.pyplot as plt

def explicit_method(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt):
    dx = L / (Nx - 1)
    x = [i * dx for i in range(Nx)]
    u = [0.0] * Nx
    u_new = [0.0] * Nx    
    T_initial = lambda x: T_initial_value
    for i in range(Nx):
        u[i] = T_initial(x[i])
    for n in range(Nt):
        for i in range(1, Nx-1):
            u_new[i] = u[i] + alpha * dt / dx**2 * (u[i-1] - 2*u[i] + u[i+1])
        u_new[0] = T0
        u_new[-1] = TL
        u[:] = u_new[:]
    return u, x

def richardson_method(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt):
    u = [0.0] * Nx
    u_richardson = u[:]
    u_explicit_1, x = explicit_method(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt)
    u_explicit_2, _ = explicit_method(L, T0, TL, alpha, T_initial_value, Nx, Nt // 2, dt / 2)
    for i in range(Nx):
        u_richardson[i] = u_explicit_1[i] + (u_explicit_1[i] - u_explicit_2[i]) / 3
    return u_richardson, x

def plot_heat_solution(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt):
    u_explicit, x = explicit_method(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt)
    u_richardson, _ = richardson_method(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt)

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(x, u_explicit, label="Explicit Method")
    plt.title("Explicit Method Solution")
    plt.xlabel("x")
    plt.ylabel("Temperature")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(x, u_richardson, label="Richardson Method", color='r')
    plt.title("Richardson Method Solution")
    plt.xlabel("x")
    plt.ylabel("Temperature")
    plt.grid(True)

    plt.tight_layout()
    plt.show()