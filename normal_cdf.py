import random
import math
import tkinter
_cp = tkinter.Tk()
_cp.withdraw()

normal = []
for x in range(100000):
    normal.append(random.normalvariate(0, 1))
_cp.clipboard_clear()
_cp.clipboard_append(normal)
print("done")