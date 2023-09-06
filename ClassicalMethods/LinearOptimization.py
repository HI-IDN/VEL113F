from gurobipy import Model, GRB


def add_constraints(model, P, V, B, M):
    # Constraints
    model.addConstr(P + V + B + M == 1, name="Total_Liter")
    model.addConstr(M >= 0.03, name="Min_Malt")
    model.addConstr(M <= 0.05, name="Max_Malt")
    model.addConstr(B >= 0.02, name="Min_Brandy")
    model.addConstr(V <= 0.07, name="Max_Vodka")
    model.addConstr(V + B <= 0.10, name="Max_HardLiquor")


def solve_first_model():
    model = Model("Beer Substitute Optimization - Strongest Blend")

    # Decision Variables
    P = model.addVar(name="Pilsner")
    V = model.addVar(name="Vodka")
    B = model.addVar(name="Brandy")
    M = model.addVar(name="Malt_Extract")

    # Objective Function: Maximizing the strength
    model.setObjective(2.25 * P + 40 * V + 40 * B + 1.5 * M, GRB.MAXIMIZE)

    # Adding constraints
    add_constraints(model, P, V, B, M)

    # Solve the model
    model.optimize()

    if model.Status == GRB.OPTIMAL:
        return float(P.x), float(V.x), float(B.x), float(M.x), float(model.objVal)
    else:
        return None, None, None, None, None


def solve_second_model():
    model = Model("Beer Substitute Optimization - Cheapest Blend")

    # Decision Variables
    P = model.addVar(name="Pilsner")
    V = model.addVar(name="Vodka")
    B = model.addVar(name="Brandy")
    M = model.addVar(name="Malt_Extract")

    # Objective Function: Minimizing the cost
    model.setObjective(100 * P + 2000 * V + 3000 * B + 120 * M, GRB.MINIMIZE)

    # Adding constraints
    add_constraints(model, P, V, B, M)

    # Additional constraint for the 4% strength
    model.addConstr(2.25 * P + 40 * V + 40 * B + 1.5 * M == 4, name="4%_Strength")

    # Solve the model
    model.optimize()

    if model.Status == GRB.OPTIMAL:
        return float(P.x), float(V.x), float(B.x), float(M.x), float(model.objVal)
    else:
        return None, None, None, None, None


def print_solution(P, V, B, M, objVal):
    print(
        f"Optimal Solution: Pilsner={P:.2f}, Vodka={V:.2f}, Brandy={B:.2f}, Malt Extract={M:.2f}, Objective Value={objVal:.2f}")


# Solve the first model
P1, V1, B1, M1, objVal1 = solve_first_model()

# Solve the second model
P2, V2, B2, M2, objVal2 = solve_second_model()

# Print results
print_solution(P1, V1, B1, M1, objVal1)
print("-" * 50)
print_solution(P2, V2, B2, M1, objVal2)
