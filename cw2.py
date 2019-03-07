# Wilczewski Daniel
# Cw 2
# python3

u_1 = [0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1]
u_2 = [0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
u_3 = [0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1]
u_4 = [0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1]
u_5 = [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1]
u_vectors = [ u_1, u_2, u_3, u_4, u_5 ]

def get_scalar_sum(w,u):
    output = 0.0

    for i in range(26):
        output += w[i] * u[i]

    if output >= 0 :
        return 1.0
    else:
        return 0.0

def train(c):
    zt = 0.0
    time = 1
    counter = 0
    w_vector = [ 1 + 1/(i+0.05) for i in range(26) ]

    while counter != 5:
        if 1 + (time-1) % 5  <= 3:
            zt = 1.0
        else:
            zt = 0.0

        y = get_scalar_sum(w_vector, u_vectors[time%5])

        for i in range(26):
            w_vector[i] = w_vector[i] + c * (zt - y) * u_vectors[ (time-1) % 5][i]
        time +=1

        if y == zt:
            counter += 1
        else:
            counter = 0

    print(f"c = {c}, time = {time}")
    w_vector = [ round(x, 2) for x in w_vector ]
    for idx, val in enumerate(w_vector):
        print(val, end='\t')
        print() if idx < 24 and (idx+1) % 5 == 0  else None
    print('\n')

train(1.0)
train(0.1)
train(0.01)
