import numpy as np
import matplotlib.pyplot as plt
from label_maps import * 
import cgi
## pick a random class 0-99
fc_i = np.random.randint(0, 100)
fc_st = finelabel_from_idx(fc_i)
print(fc_i)
print(fc_st)

## pick a random img, 0-99
img_i = np.random.randint(0, 100)
