def sizzle_zz(g01, o0, o1, wd, w0, w1, a0, a1):
    zz = 2*g01*abs(o0)*abs(o1)*a0*a1/((w0-wd)*(w1-wd)*(w0+a0-wd)*(w1+a1-wd))
    return zz

def sizzle_iz(g01, o0, o1, wd, w0, w1, a0, a1):
    iz = g01*(a0+a1)*abs(o0)*abs(o1)/((w1-wd)*(w0+a0-wd)*(w1+a1-wd))
    return iz

def sizzle_zi(g01, o0, o1, wd, w0, w1, a0, a1):
    zi = g01*(a0+a1)*abs(o0)*abs(o1)/((w0-wd)*(w0+a0-wd)*(w1+a1-wd))
    return zi