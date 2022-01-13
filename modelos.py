import numpy as np
# Modelo SIR

def dS(N, S, I, b):
    return S-((b*S*I)/N)

def dI(N, S, I, b, y):
    return I+((b*S*I)/N)-(y*I)

def dR(I, R, y):
    return R+(y*I)

def SIR(N, S, I, R, t, b=0.199, y=0.0714):
      vS = [S]
      vI = [I]
      vR = [R]
      vt = [1]
      for m in range(0,t-1):
          vS.append(dS(N,vS[m],vI[m],b))
          vI.append(dI(N,vS[m],vI[m],b,y))
          vR.append(dR(vI[m],vR[m],y))
          vt.append(m+2)
      return [vt,vS,vI,vR]

# Modelo Logistico
def Logistica(t: int, P: list):
    def p0(P0,t,a=0.1982,b=0.0000006):
        return (P0*a*np.exp(a*t))/((a-b*P0)+(P0*b*np.exp(a*t)))
    vt = []
    vP = []
    for i in range(0,t):
        vt.append(i+1)
        vP.append(p0(P[i],i+1))
    return [vt,vP]    

# Modelo Gompertz
def P(a,b,c,t):
    return a*np.exp(-b*np.exp(-c*t))

def dP(a, b, c, t):
    return a*b*c*np.exp(-c*t)*np.exp(-b*np.exp(-c*t))

def gompertz(t, const: list):
    vP = []
    vdP = []
    vt = []
    for m in range(0,t):
        vP.append(P(const[0],const[1],const[2],m))
        vdP.append(dP(const[0],const[1],const[2],m))
        vt.append(m)
    return [vt,vP,vdP]

def cal_constante(p: list):
    y = []
    a = p[len(p)-1]+1
    for i in p:
        y.append(np.log(np.log(a/i)))
    B = ((y[len(y)-1]-y[0])/(len(y)-1))*(-1)+y[0]
    m = (y[len(y)-1]-y[0])/(len(y)-1)
    b = np.exp(B)
    c = -m
    return [a,b,c]