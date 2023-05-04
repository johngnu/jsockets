import sys

# devielve a * b con sumas
def ms(a, b):
    s = 0    
    for i in range(1, b + 1):
        s = s + a
    return s    

# se ejecuta 
# python argv_program.py 5 7

print(sys.argv)  # muestra un array

a = sys.argv[1] # lle 5
b = sys.argv[2] # lee 7

print(a, b)

cad = "a b"
print(cad.split()[0])

print(ms(int(a), int(b))) 