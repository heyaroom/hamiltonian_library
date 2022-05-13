def stark_z(od, wd, w0, a0):
    w0d = w0 + od**2*a0/(2*(w0-wd)*(w0+a0-wd))
    return w0d