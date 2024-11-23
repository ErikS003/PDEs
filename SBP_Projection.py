
import operators as ops
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

