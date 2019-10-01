x = float(input('Введіть x: '))
f = 0

if x > 3:
    f = 1.2*(x**2)-3*x-9
else:
    f = 12.1/(2*(x**2)+1)

print('F(x) = ', str(round(f,2)))
exit = input('Натисніть Enter для завершення')
