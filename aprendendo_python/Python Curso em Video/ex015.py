#Tabuada de um número qualquer
x = int(input('Digite um número para ver sua tabuada: '))

print('---------------')
for i in range(1, 11):
    print(f'{x} x {i} = {x*i}')
print('---------------')
