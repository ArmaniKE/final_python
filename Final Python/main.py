import tkinter as tk
from tkinter import messagebox
from laplace import laplace_eq, print_grid, visual
from wave_eq import wave_solver
from heat import plot_heat_solution

def run_laplace(grid):
    try:
        res = laplace_eq(grid)
        print_grid(res, title="Laplace Equation Solution")
        visual(res)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_wave_eq(length, duration, a, nx, nt):
    try:
        wave_solver(length, duration, a, nx, nt)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_heat_eq(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt):
    try:
        plot_heat_solution(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_function_select(*args):
    selected_func = func_var.get()
    
    for widget in inp_frame.winfo_children():
        widget.destroy()

    label_font = ("Arial", 14, "bold")
    entry_font = ("Arial", 12)

    if selected_func == "Laplace Equation":

        tk.Label(inp_frame, text="Rows:", font=label_font, fg="blue").grid(row=0, column=0, pady=5)
        row_entry = tk.Entry(inp_frame, font=entry_font)
        row_entry.grid(row=0, column=1)

        tk.Label(inp_frame, text="Columns:", font=label_font, fg="blue").grid(row=1, column=0, pady=5)
        col_entry = tk.Entry(inp_frame, font=entry_font)
        col_entry.grid(row=1, column=1)

        tk.Label(inp_frame, text="Top Boundary:", font=label_font, fg="blue").grid(row=2, column=0, pady=5)
        top_entry = tk.Entry(inp_frame, font=entry_font)
        top_entry.grid(row=2, column=1)

        tk.Label(inp_frame, text="Bottom Boundary:", font=label_font, fg="blue").grid(row=3, column=0, pady=5)
        bottom_entry = tk.Entry(inp_frame, font=entry_font)
        bottom_entry.grid(row=3, column=1)

        tk.Label(inp_frame, text="Left Boundary:", font=label_font, fg="blue").grid(row=4, column=0, pady=5)
        left_entry = tk.Entry(inp_frame, font=entry_font)
        left_entry.grid(row=4, column=1)

        tk.Label(inp_frame, text="Right Boundary:", font=label_font, fg="blue").grid(row=5, column=0, pady=5)
        right_entry = tk.Entry(inp_frame, font=entry_font)
        right_entry.grid(row=5, column=1)

        def on_laplace_submit():
            try:
                rows = int(row_entry.get())
                cols = int(col_entry.get())
                top = int(top_entry.get())
                bottom = int(bottom_entry.get())
                left = int(left_entry.get())
                right = int(right_entry.get())
                grid = [[0.0] * cols for _ in range(rows)]
                for j in range(cols):
                    grid[0][j] = top
                    grid[-1][j] = bottom
                for i in range(rows):
                    grid[i][0] = left
                    grid[i][-1] = right
                res = laplace_eq(grid)
        
                disp_window = tk.Toplevel()
                disp_window.title("Laplace Equation Results")
                
                tk.Label(disp_window, text="Initial Grid", font=("Arial", 14, "bold"), fg="blue").pack(pady=5)
                initial_grid = tk.Text(disp_window, width=60, height=15, font=("Courier", 12))
                initial_grid.pack(pady=5)
                initial_grid.insert("1.0", "\n".join(["\t".join(f"{val:.2f}" for val in row) for row in grid]))
                initial_grid.config(state="disabled")

                tk.Label(disp_window, text="Solved Grid", font=("Arial", 14, "bold"), fg="green").pack(pady=5)
                solved_grid = tk.Text(disp_window, width=60, height=15, font=("Courier", 12))
                solved_grid.pack(pady=5)
                solved_grid.insert("1.0", "\n".join(["\t".join(f"{val:.2f}" for val in row) for row in res]))
                solved_grid.config(state="disabled")
                
                visual(res)
                
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        tk.Button(inp_frame, text="Run Laplace", command=on_laplace_submit, font=("Arial", 14), bg="green", fg="white").grid(row=6, columnspan=2, pady=10)
    
    elif selected_func == "Wave Equation":
        tk.Label(inp_frame, text="Length:", font=label_font, fg="purple").grid(row=0, column=0, pady=5)
        length_entry = tk.Entry(inp_frame, font=entry_font)
        length_entry.grid(row=0, column=1)

        tk.Label(inp_frame, text="Duration:", font=label_font, fg="purple").grid(row=1, column=0, pady=5)
        duration_entry = tk.Entry(inp_frame, font=entry_font)
        duration_entry.grid(row=1, column=1)

        tk.Label(inp_frame, text="Coefficient (a):", font=label_font, fg="purple").grid(row=2, column=0, pady=5)
        a_entry = tk.Entry(inp_frame, font=entry_font)
        a_entry.grid(row=2, column=1)

        tk.Label(inp_frame, text="Number of spatial points (nx):", font=label_font, fg="purple").grid(row=3, column=0, pady=5)
        nx_entry = tk.Entry(inp_frame, font=entry_font)
        nx_entry.grid(row=3, column=1)

        tk.Label(inp_frame, text="Number of time steps (nt):", font=label_font, fg="purple").grid(row=4, column=0, pady=5)
        nt_entry = tk.Entry(inp_frame, font=entry_font)
        nt_entry.grid(row=4, column=1)

        def on_wave_submit():
            try:
                length = float(length_entry.get())
                duration = float(duration_entry.get())
                a = float(a_entry.get())
                nx = int(nx_entry.get())
                nt = int(nt_entry.get())
                run_wave_eq(length, duration, a, nx, nt)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

        tk.Button(inp_frame, text="Run Wave Equation", command=on_wave_submit, font=("Arial", 14), bg="green", fg="white").grid(row=5, columnspan=2, pady=10)
    
    elif selected_func == "Heat Equation":

        tk.Label(inp_frame, text="Length (L):", font=label_font, fg="orange").grid(row=0, column=0, pady=5)
        L_entry = tk.Entry(inp_frame, font=entry_font)
        L_entry.grid(row=0, column=1)

        tk.Label(inp_frame, text="Left End Temp (T0):", font=label_font, fg="orange").grid(row=1, column=0, pady=5)
        T0_entry = tk.Entry(inp_frame, font=entry_font)
        T0_entry.grid(row=1, column=1)

        tk.Label(inp_frame, text="Right End Temp (TL):", font=label_font, fg="orange").grid(row=2, column=0, pady=5)
        TL_entry = tk.Entry(inp_frame, font=entry_font)
        TL_entry.grid(row=2, column=1)

        tk.Label(inp_frame, text="Thermal Diffusivity (alpha):", font=label_font, fg="orange").grid(row=3, column=0, pady=5)
        alpha_entry = tk.Entry(inp_frame, font=entry_font)
        alpha_entry.grid(row=3, column=1)

        tk.Label(inp_frame, text="Initial Temp Value:", font=label_font, fg="orange").grid(row=4, column=0, pady=5)
        T_initial_entry = tk.Entry(inp_frame, font=entry_font)
        T_initial_entry.grid(row=4, column=1)

        tk.Label(inp_frame, text="Number of Spatial Points (Nx):", font=label_font, fg="orange").grid(row=5, column=0, pady=5)
        Nx_entry = tk.Entry(inp_frame, font=entry_font)
        Nx_entry.grid(row=5, column=1)

        tk.Label(inp_frame, text="Number of Time Steps (Nt):", font=label_font, fg="orange").grid(row=6, column=0, pady=5)
        Nt_entry = tk.Entry(inp_frame, font=entry_font)
        Nt_entry.grid(row=6, column=1)

        tk.Label(inp_frame, text="Time Step (dt):", font=label_font, fg="orange").grid(row=7, column=0, pady=5)
        dt_entry = tk.Entry(inp_frame, font=entry_font)
        dt_entry.grid(row=7, column=1)
        
        def on_heat_submit():
            try:
                L = float(L_entry.get())
                T0 = float(T0_entry.get())
                TL = float(TL_entry.get())
                alpha = float(alpha_entry.get())
                T_initial_value = float(T_initial_entry.get())
                Nx = int(Nx_entry.get())
                Nt = int(Nt_entry.get())
                dt = float(dt_entry.get())
                run_heat_eq(L, T0, TL, alpha, T_initial_value, Nx, Nt, dt)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

        tk.Button(inp_frame, text="Run Heat Equation", command=on_heat_submit, font=("Arial", 14), bg="green", fg="white").grid(row=8, columnspan=2, pady=10)

root = tk.Tk()
root.title("Differential Equation Solvers")
width, height = 1080, 720
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x_pos = int((screen_w / 2) - (width / 2))
y_pos = int((screen_h / 2) - (height / 2))
root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
label = tk.Label(root, text="Choose a function to test:", font=("Arial", 16, "bold"))
label.pack(pady=10)
func_var = tk.StringVar()
func_var.set("Select Function")
func_menu = tk.OptionMenu(root, func_var, "Laplace Equation", "Wave Equation", "Heat Equation")
func_menu.config(font=("Arial", 14))
func_menu.pack(pady=10)
func_var.trace("w", on_function_select)
inp_frame = tk.Frame(root)
inp_frame.pack(pady=10)
root.mainloop()