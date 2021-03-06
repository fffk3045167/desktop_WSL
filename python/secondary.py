#二次方程 ax**2 + bx + c = 0
#导入cmath(复杂数学运算)模块
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

if (b**2 - 4*a*c) >= 0:
    
    d = (b**2) - (4*a*c)
    
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    
    sol3 = (-b - d**0.5) / (2*a)
    sol4 = (-b + d**0.5) / (2*a)
    
    sol5 = float(sol3)
    sol6 = float(sol4)
    
    print('一元二次方程的根为（使用cmath）: {0} ; {1}'.format(sol1,sol2))
    print('一元二次方程的根为（不使用cmath）: {0} ; {1}'.format(sol3,sol4))
    print('使用float类型转换: {0} ; {1}'.format(sol5,sol6))
else:
    print('该一元二次方程无解.')
