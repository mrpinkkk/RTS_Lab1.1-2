import matplotlib.pyplot as plt
from alg import signal, get_m, get_D

n = 10
omega = 1200
N = 64

range_min = 0
range_max = 1

s_gen = signal(n, omega, N, range_min, range_max)
s = [s_gen(i) for i in range(N)]
m = get_m(s)
D = get_D(s, m)
print(f'm: {m}\nD: {D}')

plt.plot(range(N), s)
plt.show()
