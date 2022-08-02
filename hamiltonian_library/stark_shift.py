import numpy as np

def stark_z(od, wd, w0, a0):
    w0d = w0 + od**2*a0/(2*(w0-wd)*(w0+a0-wd))
    return w0d

def numerical_stark_z(od, wd, w0, a0):
    hamiltonian = np.array([
        [0, od/2, 0],
        [od/2, w0-wd, 2**(-0.5)*od],
        [0, 2**(-0.5)*od, 2*(w0-wd)+a0]
    ])
    val, vec = np.linalg.eig(hamiltonian)
    
    eg = val[np.argmin(abs(val-0))]
    ee = val[np.argmin(abs(val-(w0-wd)))] + wd
    ef = val[np.argmin(abs(val-(2*(w0-wd)+a0)))] + 2*wd

    w0d = ee - eg
    a0d = ef - 2*ee + eg
    
    return w0d, a0d