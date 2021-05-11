import time

l = 20
q = ['.']*l
i = 0
f = 1
while True:
    i+=1
    p = q[:]
    m = q[:]
    x = i%(l-2)
    p[x], p[x-1], p[x+1], p[x-2], p[x+2] = ["0", "O", "O", 'o', "o"]
    print ("".join(p), end="", flush=True)
    time.sleep(0.05*f)
    print ("\r", end="", flush=True)
    if i%l == 0: f += 1
    
