
'''
outline of PDE approximation using SBP projection:

L = [L_l,L_r].T boundrary condition vector
P = I-H^-1@L.T@(L@H^-1@L.T)^-1@L (projection matrix), P^2=P,H@P=P.T@H, LPv = 0. (P is idempotent, HP is symmetric,
the projected solution vector satisfies BCs), H is the quadrature matrix.

ex: 

u_t = a@u_x+b@u_xx,  -1<=x<=1, t>=0
u = 0, x=-1
a*u+2b*u_x, x=1
u=f(x), t=0

SBP =>

dv/dt = a*D_1@v+b*D_2@v -1<=x<=1, t>=0
v=0, x=-1
a*v+2b*d_r^T@v, x= 1, d_r = e^T_r@D1

Projection =>

v_t=P@(a*D_1+b*D_2)@P@v
v=f(x), t=0

For proving stability of the SBP-Projection approximation, use Energy method with multiplying by
v.T@H from the left.
'''

import operators as ops

import numpy as np
# Domain boundaries
xl = -2
xr = 2
mx = 101
# Space discretization
hx = (xr - xl)/(mx-1)
x = np.linspace(xl,xr,mx)
a = 1
b = 0.1

def f(x):
    return np.exp(-(6*x)**2)
#generate initial data:
v_0 = []
for _ in range(len(x)):
    v_0.append(f(x[_]))
v_0 = np.array(v_0)
print(v_0)


from scipy.sparse.linalg import inv
from scipy.sparse import kron, csc_matrix, eye, vstack
def SBP_sol(mx,hx,v):
    H,HI,D1,D2,e_l,e_r,d1_l,d1_r = ops.sbp_cent_4th(mx,hx)
    L = vstack((e_l,
                   a*e_r+2*b*d1_r))    
    P = np.eye(H.shape[0])-HI@L.T@inv(L@HI@L.T)@L
    D = P@(a*D1+b*D2)@P
    print(D.shape)
    rhs = D@v
    return rhs


print(SBP_sol(mx,hx,v_0))