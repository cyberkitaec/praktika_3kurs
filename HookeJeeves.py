

def HJ(b1, h, e, f):
    z = 0.1
    runOuterLoop = True
    while (runOuterLoop):
        runOuterLoop = False
        runInnerLoop = True
        xk = b1 
        b2 = utilSearch(b1, h, f) 
        Path1.append(b1)
        Path2.append(b2)
        Path3.append(xk)
        while (runInnerLoop):
            Path1.append(b1)
            Path2.append(b2)
            runInnerLoop = False
            for i in range(len(b1)):
                xk[i] = b1[i] + 2*(b2[i]-b1[i])
            Path3.append(xk)
            x = utilSearch(xk, h, f) 
            Path4.append(x)
            b1 = b2 
            fx = f(x)
            fb1 = f(b1)
            if (fx+machineAcc<fb1):
                b2 = x
                runInnerLoop = True 
            elif (fx-machineAcc>fb1): 
                runOuterLoop = True 
                break
            else:
                s = 0 
                for i in range(len(h)):
                    s+=h[i]*h[i]
                if (e*e + machineAcc > s): 
                    break 
                else:
                    for i in range(len(h)): 
                        h[i] = h[i]* z 
                    runOuterLoop = True 
    return b1 