import matplotlib.pyplot as plt
import numpy as np



fileName = '.\\user_data\\19-file-time.txt'
diagramFile = '.\\user_diagrams\\new-diagram.png'
# Чтение значений из файла
with open(fileName, 'r') as file:
    data = file.readlines()
    data = [float(value) for value in data]

# Построение графика

x = np.arange(len(data))
x_new = np.linspace(0, len(data), 100)  # 100 точек для интерполяции
y_new = np.interp(x_new, x, data)


plt.plot(data)
plt.title('График EAR по времени')
plt.xlabel('Время')
plt.ylabel('EAR')
plt.savefig(diagramFile)


plt.show()