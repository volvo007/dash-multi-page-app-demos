import numpy as np
import pandas as pd
import datashader as ds
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis

from numba import jit
from math import sin, cos, sqrt

n = 10000000


@jit(nopython=True)
def Califf(x, y, a, b, c, d, *o):
    return sin(a * y) + c * cos(a * x),\
        sin(b * x) + d * cos(b * y)


@jit(nopython=True)
def get_coord(fn, x0, y0, a, b=0, c=0, d=0, e=0, f=0, n=n):
    x, y = np.zeros(n), np.zeros(n)
    x[0], y[0] = x0, y0
    for i in range(n-1):
        x[i+1], y[i+1] = fn(x[i], y[i], a, b, c, d, e, f)
    return x, y


def get_df(fn, x0, y0, a, b=0, c=0, d=0, e=0, f=0, n=n):
    x, y = get_coord(fn, x0, y0, a, b, c, d, e, f, n)
    return pd.DataFrame({'x': x, 'y': y})


df = get_df(Califf, 0, 0, -1.3, -1.3, -1.8, -1.9, 0, 0, n)

cvs = ds.Canvas(plot_width=800, plot_height=800)
agg = cvs.points(df, 'x', 'y')
# img = tf.shade(agg, cmap=viridis)
img = tf.shade(agg, cmap=viridis, how='log')
print(img)

img.to_pil().save('test1.png')
