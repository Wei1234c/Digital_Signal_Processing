# https://www.coursera.org/learn/dsp/resources/eBDIq
from waves.tools.dsp import *


l = 0.9
G0 = 1 / 6
w0 = np.pi/3
p = np.exp(1j * w0)

Filter.get_H_from_polynomials([[G0]], [[1, -l * p], [1, -l * np.conj(p)]], 360, plot = True)

plt.show()
