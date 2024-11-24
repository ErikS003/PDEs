
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

v_t = aD_1@v + bD_2@v + sH^-1d_l(e_l^T@v)+tau_l*H^-1@e_l@(e_l^T)+tau_r*H^-1@e_r@((ae_r^T+2bd_r^T)@v)
v = f, if t = 0


'''