import pulp as pl

TotalDemand = 600

model = pl.LpProblem("Textile_Cost_Minimization", pl.LpMinimize)

x1 = pl.LpVariable('Cotton', lowBound=0)
x2 = pl.LpVariable('Polyester', lowBound=0)
x3 = pl.LpVariable('Mixed', lowBound=0)

model += 40*x1 + 35*x2 + 45*x3

model += 0.5*x1 + 0.4*x2 + 0.6*x3 <= 1000
model += 1.2*x1 + 0.6*x3 <= 500
model += 1.0*x2 + 0.8*x3 <= 400
model += 0.3*x1 + 0.25*x2 + 0.4*x3 <= 600

model += x1 + x2 + x3 >= TotalDemand

model.solve(pl.PULP_CBC_CMD(msg=False))

print("Status:", pl.LpStatus[model.status])
print("Cotton =", pl.value(x1))
print("Polyester =", pl.value(x2))
print("Mixed =", pl.value(x3))
print("Total Cost =", pl.value(model.objective))