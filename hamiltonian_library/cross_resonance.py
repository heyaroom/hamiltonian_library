def cr_ix(g,o,w0,w1,a0,a1):
    d = w0 - w1
    oix = - g*o/(d+a0) \
    + d*a0*g*o**3/((d+a0)**3*(2*d+a0)*(2*d+3*a0))
    return oix

def cr_iz(g,o,w0,w1,a0,a1):
    d = w0 - w1
    oiz = g**2*o**2/2*( \
        (a0**3-2*a0*d**2-2*d**3)/(a0*d**2*(a0+d)**2*(d-a1)) \
        + (a0**2+d**2)/(d**2*a1*(a0+d)**2) \
        + (6*a0**5+4*a0**4*d-6*a0**3*d**2+7*a0**2*d**3+12*a0*d**4+4*d**5) \
            / (d**2*(a0+d)**2*(2*a0+d)**2*(a0+2*d)*(3*a0+2*d)) \
        + 2/(a0*(a0+d)*(a0+d-a1)) \
        + 2/((a0+d)*(a0+d-a1)) \
        + 1/(d*(d-a1)**2))
    return oiz

def cr_zi(g,o,w0,w1,a0,a1):
    d = w0 - w1
    ozi = - a0*o**2/(2*d*(a0+d)) \
        + g**2*o**2/(2*(a0+d)**3) * ( \
            2*(a0**2+a0*d+d**2)*(a0+d)/(a0*d*(a1-d)) \
            + a0/2*( \
                4*a0**2/d**3 \
                + 11*a0/d**2 \
                + 3*a0/(2*a0+d)**2 \
                - 2/(a0+2*d) \
                - 6/(3*a0+2*d) \
                + 12/d \
            ) \
            + 2*(a0+d)**2/(a0*(a0+d-a1)) \
            + 2*(a0+d)**2/(a0+d-a1) \
            - 2*a0*(a0+d)/(d+a1) \
        )
    return ozi

def cr_zx(g,o,w0,w1,a0,a1):
    d = w0 - w1
    ozx = - g*o/d*(a0/(a0+d)) \
        + g*o**3*a0**2*(3*a0**3+11*a0**2*d+15*a0*d**2+9*d**3) \
        /(2*d**3*(a0+d)**3*(a0+2*d)*(3*a0+2*d))
    return ozx

def cr_zz(g,o,w0,w1,a0,a1):
    d = w0 - w1
    ozz = g**2/(2*(a0+d)**2) * ( \
        o**2*( \
            (a0**3-2*a0*d**2-2*d**3)/(a0*d**2*(a1-d)) \
            + 1/2*( \
                4*(3*a0+d)*(a0**2+a0*d+d**2)/(d**2*(2*a0+d)**2) \
                - 16*d/(3*a0**2+8*a0*d+4*d**2) \
            ) \
            + 2*a0/(d*a1) \
            - 2*(a0+d)/(a0+d-a1)**2 \
            - 2*(a0+d)/(a0*(a0+d-a1)) \
        ) \
        + 2*(a0+d)*(a0+a1)/(d-a1) \
    )
    return ozz