import numpy as np

# Define iteration matrix B and vector c: x^(k+1) = B * x^k + c
B = np.array([[0, 1/4, 0],
              [1/4, 0, 1/4],
              [0, 1/3, 0]])

c = np.array([7/4, 5/4, 4/3])

# Initial approximation
x = np.array([0.0, 0.0, 0.0])

max_iter = 100
tol = 1e-6

print(f"{'k':>3} {'x[0]':>12} {'x[1]':>12} {'x[2]':>12} {'error':>12}")
print("-" * 55)

for k in range(1, max_iter + 1):
    x_old = x.copy()

    # x^(k+1) = B * x^k + c
    x = B @ x_old + c

    error = np.linalg.norm(x - x_old, ord=np.inf)

    print(
        f"{k:3d}"
        f"{x[0]:12.6f}"
        f"{x[1]:12.6f}"
        f"{x[2]:12.6f}"
        f"{error:12.6e}"
    )

    # Stopping criteria
    if error < tol:
        print(f"\nConverged in {k} iterations.")
        break
