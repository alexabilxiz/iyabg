import matplotlib.pyplot as plt

x_axis = [1, 2, -3, 4, -5, 6, 7, -8, 9, 10]
y_axis = [2, 4, 9, -16, 25, -36, 49, 64,  -81, 100]

plt.title('Diagram Kartesius')
plt.scatter(x_axis, y_axis, color="blue", marker='*', label= 'legend 1')


plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.grid(True)
plt.legend()

plt.show()