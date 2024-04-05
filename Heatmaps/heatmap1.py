import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Your data
data = np.array([[0.66172336, 0.73891156, 0.65988662, 0.6255102, 0.72643991, 0.6921542, 0.64820862, 0.68376417, 0.71213152, 0.76206349, 0.79276644, 0.74657596, 0.72528345, 0.69505669, 0.6678458, 0.66870748, 0.69390023], 
                 [0.66315193, 0.65077098, 0.66444444, 0.66068027, 0.66217687, 0.67106576, 0.70668934, 0.70283447, 0.72172336, 0.69396825, 0.72580499, 0.68544218, 0.72748299, 0.66988662, 0.69628118, 0.72705215, 0.65285714],
                 [0.71328798, 0.75462585, 0.69269841, 0.77163265, 0.69380952, 0.69632653, 0.75258503, 0.73043084, 0.72657596, 0.72015873, 0.7139229, 0.75657596, 0.71873016, 0.68344671, 0.76190476, 0.66172336, 0.84235828],
                 [0.69362812, 0.67666667, 0.78705215, 0.7106576,  0.78782313, 0.77290249, 0.69433107, 0.77376417, 0.79281179, 0.73732426, 0.73056689, 0.84321995, 0.73569161, 0.7162585,  0.73650794, 0.75092971, 0.67117914],
                 [0.73650794, 0.71480726, 0.76027211, 0.75122449, 0.74886621, 0.78310658, 0.65047619, 0.73852608, 0.78349206, 0.76598639, 0.75804989, 0.65777778, 0.77839002, 0.74970522, 0.7476644, 0.7052381, 0.72056689],
                 [0.6855102, 0.72129252, 0.71442177, 0.73356009, 0.75131519, 0.74741497, 0.73641723, 0.77442177, 0.7306576, 0.76022676, 0.70689342, 0.76918367, 0.73786848, 0.75335601, 0.70494331, 0.72988662, 0.65893424],
                 [0.72163265, 0.7485034, 0.7723356, 0.80090703, 0.74027211, 0.72979592, 0.76877551, 0.8122449, 0.70278912, 0.76043084, 0.78419501, 0.75351474, 0.90482993, 0.80285714, 0.73306122, 0.6615873, 0.65698413],
                 [0.73918367, 0.71972789, 0.81553288, 0.7824263, 0.79015873, 0.74786848, 0.82349206, 0.76893424, 0.85331066, 0.82217687, 0.81870748, 0.77662132, 0.78739229, 0.84836735, 0.74253968, 0.77335601, 0.75045351]])

# Create meshgrid
x = np.arange(data.shape[1])+1
y = np.arange(data.shape[0])+1
x, y = np.meshgrid(x, y)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, data, cmap='viridis')

# Set labels
ax.set_xlabel('Stoel')
ax.set_ylabel('Rij')
ax.set_zlabel('Nagalmtijd(s)')

plt.show()
