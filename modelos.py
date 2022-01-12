
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

