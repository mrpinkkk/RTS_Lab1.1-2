import matplotlib.pyplot as plt
from alg import signal, get_m, get_D, get_R, get_R_by_gen, r_tau


n = 10
omega = 1200
N = 64

range_min = 0
range_max = 1

x_gen = signal(n, omega, N, range_min, range_max)
y_gen = signal(n, omega, N, range_min, range_max)

x = [x_gen(i) for i in range(N)]
y = [y_gen(i) for i in range(N)]

x1 = [i+N//2 for i in x]

plt.plot(range(N), x, label='x')
plt.plot(range(N), y, label='y')
plt.legend()
plt.show()
m = get_m(x)
D = get_D(x, m)

Rxx1 = get_R(x, x1)
Rxx = get_R(s_gen, int(N/2), m)
print(f'm: {m}\nD: {D}')

Rxx = get_R(x[:N//2], x[N//2:])
plt.plot(range(N//2), Rxx, label='Rxx')

Rxy = get_R(x, y)
plt.plot(range(N), Rxy, label='Rxy')

Rxx_gen = get_R_by_gen(x_gen, y_gen, N)
plt.plot(range(N), Rxx_gen, label='Rxx_gen')

r_tau_X = [r_tau(x_gen, y_gen, N, tau) for tau in range(N//2)]
r_tau_Y = [r_tau(x_gen, x_gen, N, tau) for tau in range(N//2)]
plt.plot(range(N//2), r_tau_X, label='Rxx_tauX')
plt.plot(range(N//2), r_tau_Y, label='Rxx_tauY')

print(sum(Rxx))
print(sum(Rxy))
plt.legend()
plt.show()

