import numpy as np
import matplotlib.pyplot as plt
import os
n = 100
A = 10
x = np.linspace(0, np.pi, 100) # задаём отрезок
fx = (-np.sin(x)*((np.sin((x**2)/np.pi))**(2*A)))
# создание папки для текстовика
try:
 os.mkdir('results')
except OSError:
 pass
complete_file = os.path.join('results', 'task_01_307B_Pogudin_16.txt')
f = open(complete_file, 'w')
# создаём текстовик
f.write('   x    f(x)\n')
for i in range(n):
 f.write(str("%.4f" % x[i])+'    '+str("%.4f" % fx[i])+"\n")
f.close()
# график
fig, ax = plt.subplots()
ax.plot(x, fx, linewidth = 2)
ax.set_xlim(0, 3);
ax.set_ylim(-1, 0.25);
ax.grid(linewidth = 1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, fx, color = 'red')
plt.show()