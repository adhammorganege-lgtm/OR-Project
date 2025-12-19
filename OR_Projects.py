import pulp as pl
import tkinter as tk
from tkinter import messagebox

# -------------------------
# Optimization Function
# -------------------------
def solve_model():
    try:
        demand = float(entry_demand.get())

        model = pl.LpProblem("Textile_Cost_Minimization", pl.LpMinimize)

        x1 = pl.LpVariable('Cotton', lowBound=0)
        x2 = pl.LpVariable('Polyester', lowBound=0)
        x3 = pl.LpVariable('Mixed', lowBound=0)

        # Objective Function
        model += 40*x1 + 35*x2 + 45*x3

        # Constraints
        model += 0.5*x1 + 0.4*x2 + 0.6*x3 <= 1000
        model += 1.2*x1 + 0.6*x3 <= 500
        model += x2 + 0.8*x3 <= 400
        model += 0.3*x1 + 0.25*x2 + 0.4*x3 <= 600
        model += x1 + x2 + x3 >= demand

        model.solve(pl.PULP_CBC_CMD(msg=False))

        if pl.LpStatus[model.status] != "Optimal":
            messagebox.showerror("Error", "No optimal solution found")
            return

        result_text.set(
            f"Optimal Production Plan\n"
            f"------------------------\n"
            f"Cotton Shirts     : {pl.value(x1):.2f}\n"
            f"Polyester Shirts  : {pl.value(x2):.2f}\n"
            f"Mixed Shirts      : {pl.value(x3):.2f}\n\n"
            f"Minimum Cost = {pl.value(model.objective):.2f} EGP"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")

# -------------------------
# GUI Design — Dark Theme
# -------------------------
root = tk.Tk()
root.title("Textile Production Optimization")
root.geometry("480x440")
root.configure(bg="#1e1e1e")

# Title
tk.Label(
    root,
    text="Textile Cost Minimization Model",
    font=("Segoe UI", 16, "bold"),
    bg="#1e1e1e",
    fg="#d4d4d4"
).pack(pady=15)

# Input Panel
input_frame = tk.Frame(root, bg="#252526", bd=1, relief="solid")
input_frame.pack(padx=20, pady=10, fill="x")

tk.Label(
    input_frame,
    text="Total Production Demand (Units)",
    font=("Segoe UI", 11),
    bg="#252526",
    fg="#d4d4d4"
).pack(pady=10)

entry_demand = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    justify="center",
    bg="#1e1e1e",
    fg="#d4d4d4",
    insertbackground="#d4d4d4",
    relief="flat"
)
entry_demand.pack(pady=5)
entry_demand.insert(0, "600")

# Solve Button
tk.Button(
    root,
    text="Solve Optimization Model",
    command=solve_model,
    bg="#0e639c",
    fg="white",
    activebackground="#1177bb",
    activeforeground="white",
    font=("Segoe UI", 11, "bold"),
    padx=15,
    pady=6,
    relief="flat"
).pack(pady=15)

# Result Panel
result_frame = tk.Frame(root, bg="#252526", bd=1, relief="solid")
result_frame.pack(padx=20, pady=10, fill="both", expand=True)

result_text = tk.StringVar()
tk.Label(
    result_frame,
    textvariable=result_text,
    font=("Consolas", 11),
    bg="#252526",
    fg="#d4d4d4",
    justify="left"
).pack(padx=10, pady=10)

root.mainloop()