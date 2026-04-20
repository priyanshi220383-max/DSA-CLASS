def secant(x0, x1, tol=1e-6, max_iter=20):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1 - fx0) < 1e-10:
            print("Function values too close; stop.")
            break
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        print(f"Iter {i+1}: x = {x2:.6f}")
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    return x2

# Start from x0 = 1.0, x1 = 2.0
root_secant = secant(1.0, 2.0)
print("Secant root ≈", root_secant)