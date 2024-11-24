
import operators as ops

'''
outline of SBP_SAT approximation:


ex: 

u_t = a@u_x+b@u_xx,  -1<=x<=1, t>=0
u = 0, x=-1
a*u+2b*u_x, x=1
u=f(x), t=0

SBP =>

dv/dt = a*D_1@v+b*D_2@v -1<=x<=1, t>=0
v=0, x=-1
a*v+2b*d_r^T@v, x= 1, d_r = e^T_r@D1

SBP-SAT Discretization of IBVP ex:





'''