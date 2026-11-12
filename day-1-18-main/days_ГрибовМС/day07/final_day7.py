import numpy as np

data = np.array([[55, 40, 90, 75, 68], [60, 70, 80, 65, 90], [45, 85, 30, 95, 72]])

print(data)
print(data.shape)
print(data.ndim)
print(data.size)

avg = np.mean(data)
print(avg)

print(np.mean(data, axis=1))
print(np.mean(data, axis=0))
print(np.min(data))
print(np.max(data))
print(data[data >= 60])
print(data[data < avg])

print(data[0])
print(data[:, -1])
print(data[0:2, 0:2])

data[1, 1] = 95

new_data = data + 5
print(np.mean(new_data))
