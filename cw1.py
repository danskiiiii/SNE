# Wilczewski Daniel 
# Cw 1
# python 3

def print_logic_gate(weights):
    vec3_list = (0.0, 0.0, 1.0), (0.0, 1.0, 1.0), (1.0, 0.0, 1.0), (1.0, 1.0, 1.0) 
    vec2_list = (0.0, 1.0), (1.0, 1.0)

    if len(weights) == 3:
        for i in range(4):
            print(vec3_list[i][0], vec3_list[i][1], end = ' ')
            if weights[0] * vec3_list[i][0] + weights[1] * vec3_list[i][1] + weights[2] * vec3_list[i][2] >= 0.0:
                print(1)
            else:
                print(0)
    elif len(weights) == 2:
        for i in range(2):
            print(vec2_list[i][0], end = ' ')
            if weights[0] * vec2_list[i][0] +  weights[1] * vec2_list[i][1] >= 0.0:
                print(1)
            else:
                print(0)

    print()     

not_val = (-0.6, 0.4)
and_val = (0.25, 0.25, -0.5)
nand_val = (-0.33, -0.33, 0.33)
or_val = (0.33, 0.33, -0.33)

print("NOT")
print_logic_gate(not_val)
print("AND")
print_logic_gate(and_val)
print("NAND")
print_logic_gate(nand_val)
print("OR")
print_logic_gate(or_val)

