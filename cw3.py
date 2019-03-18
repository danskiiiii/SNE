# Wilczewski Daniel
# Cw 3
# python3
def show_output_matrix(vector):
    matrix = []
    for element in vector:
        if (element == -1):
            matrix.append('-')
        elif (element == 1):
            matrix.append('*')
    for i in range(1,len(matrix)+1):
        if i %5 == 0:
            print (matrix[i-1],'')
        else:
            print(matrix[i-1] ,end ='')
    print()

def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1

def SGN( vector):
    sgn_vector=[]
    for i in range(25):
        sgn_vector.append(sgn(vector[i]))
    return sgn_vector

def Hebb_function(matrix, vector):
    u = [ 0 for i in range(25)]
    for i in range(25):
        for j in range(25):
            u[i] += matrix[i][j] * vector[j]
    return SGN(u)

z0  = [ -1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1,  1, -1,  1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1 ]
z1  = [ -1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1 ]
z0_ = [ -1,  1,  1,  1, -1, -1,  1, -1, 1,  -1, -1,  1, -1,  1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1 ]
z1_ = [ -1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1, -1 ]
w = [ [ 0 for x in range(25) ]  for y in range(25) ]
for i in range(25):
    for j in range(25):
        w[i][j] = 0.04 * (z0[i] * z0[j] + z1[i] * z1[j] )
print ('F(z0):')
show_output_matrix(Hebb_function(w, z0))
print ('F(z1):')
show_output_matrix(Hebb_function(w, z1))
print ("Zaburzone F(z0'):")
show_output_matrix(Hebb_function(w, z0_))
print ("Zaburzone F(z1'):")
show_output_matrix(Hebb_function(w, z1_))