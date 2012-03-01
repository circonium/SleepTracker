# -*- coding: utf-8 -*-

import datetime

from matplotlib import pyplot as plt
import numpy as np

fname = "RUN2.TXT"

t, x, y, z = np.loadtxt(fname).T

fig = plt.figure(figsize=(10, 3))
sfig=fig.add_subplot(111)

sfig.plot(t, x, label='X')
sfig.plot(t, y, label='Y')
sfig.plot(t, z, label='Z')

sfig.set_xlim((-10000, 10000))

sfig.set_xlabel("Time")
sfig.set_ylabel("ADC value")

sfig.legend()

plt.savefig(fname[:-4] + '.png', dpi=150, bbox_inches='tight')
plt.show()
