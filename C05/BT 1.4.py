from math import*
#Bai 1.4:
a = float(input('Canh a = '))
b = float(input('Canh b = '))
c = float(input('Canh c = '))
p = (a + b + c) / 2
dientich = sqrt(p*(p-a)*(p-b)*(p-c))
print(f'Diện tích của tam giác có số đo ba cạnh ({a}; {b}; {c}) là:', dientich)