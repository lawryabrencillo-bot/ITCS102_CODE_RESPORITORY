money = 3757

J = 1000 
O = 500 
H = 200
N = 100
L = 50
A = 20 
W = 10
R = 5 
Y = 1

print("Balance", money)

Jzero = money // J
money = money % J
print("1000=", Jzero)

Ozero = money // O
money = money % O
print("500=", Ozero)

Hzero = money // H
money = money % H
print("200=", Hzero)

Nzero = money // N
money = money % N
print("100=", Nzero)

Lzero = money // L
money = money % L
print("50=", Lzero)

Azero = money // A
money = money % A
print("20=", Azero)

Wzero = money // W
money = money % W
print("10=", Wzero)

Rzero = money // R
money = money % R
print("5=", Rzero)

Yzero = money // Y
money = money % Y
print("1=", Yzero)
