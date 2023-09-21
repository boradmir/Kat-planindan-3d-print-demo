import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Kat planı verilerini tanımlayın
kat_planı = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])

# 3D grafiği oluşturun
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Kat planını 3D modelde çizin
ax.plot(kat_planı[:,0], kat_planı[:,1], zs=0, zdir='z', label='Kat Planı')

# Eksenleri etiketleyin
ax.set_xlabel('X ekseni')
ax.set_ylabel('Y ekseni')
ax.set_zlabel('Z ekseni')

# Grafiği gösterin
plt.show()
