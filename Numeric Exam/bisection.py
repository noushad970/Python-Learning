# Bisection method for f(x) = e^x (3.2 sin x - 0.5 cos x)
# Stopping criteria: stop when half-interval < eps_step OR abs(f(c)) < eps_abs
# eps_step = 0.001, eps_abs = 0.001, interval [3,4]

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return math.exp(x) * (3.2*math.sin(x) - 0.5*math.cos(x))

def bisection(a, b, eps_step=0.001, eps_abs=0.001, max_iter=1000):
    if f(a) == 0:
        return a, [{'iter':0,'a':a,'b':b,'c':a,'f(c)':f(a),'interval_half':(b-a)/2}]
    if f(b) == 0:
        return b, [{'iter':0,'a':a,'b':b,'c':b,'f(c)':f(b),'interval_half':(b-a)/2}]
    if f(a)*f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs for bisection.")
    rows = []
    for i in range(1, max_iter+1):
        c = (a + b) / 2.0
        fc = f(c)
        interval_half = (b - a) / 2.0
        rows.append({'iter': i, 'a': a, 'b': b, 'c': c, 'f(c)': fc, 'interval_half': interval_half})
        # stopping conditions
        if abs(fc) < eps_abs or interval_half < eps_step:
            return c, rows
        # choose subinterval
        if f(a)*fc < 0:
            b = c
        else:
            a = c
    # if not converged
    return c, rows

# Run bisection
eps_step = 0.001
eps_abs = 0.001
a0, b0 = 3.0, 4.0
root, history = bisection(a0, b0, eps_step=eps_step, eps_abs=eps_abs)

# Create table (DataFrame) and show
df = pd.DataFrame(history)
# Round numbers for display clarity
df_display = df.copy()
df_display[['a','b','c','f(c)','interval_half']] = df_display[['a','b','c','f(c)','interval_half']].round(6)

import caas_jupyter_tools as cjt
cjt.display_dataframe_to_user("Bisection Iterations", df_display)

# Print result info
print(f"Found root (approx): {root:.6f}")
print(f"f(root) = {f(root):.6e}")
print(f"Number of iterations: {len(history)}")

# Plot function on [3,4] and mark root
xs = np.linspace(3.0, 4.0, 400)
ys = [math.exp(x)*(3.2*math.sin(x)-0.5*math.cos(x)) for x in xs]

plt.figure(figsize=(8,4))
plt.plot(xs, ys)
plt.axhline(0)
plt.scatter([root], [f(root)])
plt.title("f(x) = e^x (3.2 sin x - 0.5 cos x) on [3,4] — bisection root")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
