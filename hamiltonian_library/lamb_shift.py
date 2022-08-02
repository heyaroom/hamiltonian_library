import numpy as np

def lamb_z(g01, w0, w1, a0, a1):
    w0d = w0 + g01**2/(w0-w1) + g01**2*(a0+a1)/(((w0+a0)-w1)*(w0-(w1+a1)))
    w1d = w1 + g01**2/(w1-w0) + g01**2*(a0+a1)/(((w0+a0)-w1)*(w0-(w1+a1)))
    return w0d, w1d

def lamb_zz(g01, w0, w1, a0, a1):
    zz = -2*g01**2*(a0+a1)/(((w0+a0)-w1)*(w0-(w1+a1)))
    return zz