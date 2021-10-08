from openpiv import tools, pyprocess, validation, filters, scaling

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# The above line is a python "magic function". In this case, it sets the backend of matplotlib to 'inline' which makes graphs appear where the generating code does within a notebook. Since we're not running in Jupyter, comment out.



import imageio

frame_a = tools.imread('./openpiv/data/test1/exp1_001_a.bmp')
frame_b = tools.imread('./openpiv/data/test1/exp1_001_b.bmp')

fig, ax = plt.subplots(1,2, figsize(12, 10))
ax[0].imshow(frame_a, cmap = plt.cm.gray);
ax[1].imshow(frame_b, cmap = plt.cm.gray);
