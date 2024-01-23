s = input("Введите число: ")
n = float(s)
nz = int(n)
sign = 1 if s[0] != "-" else -1
nz = abs(nz)
nqs = "0." + s.split('.')[1]
nq = float(nqs)
#print(bin(nz)[2::], nq)
m = '.'
k = 0
while k < 32:
    nq *= 2
    m += str(int(nq))
    if int(nq) > 0:
        nq -= int(nq)
    k += 1
#print(bin(nz)[2::], m, sep = '')
if nz > 1:
    nzs = bin(nz)[2::]
    p = len(nzs) - 1
    r = nzs.index('1')
    m2 = nzs[r + 1::] + m[1::]
elif nz == 1:
    p = 0
    m2 = m[1::]
else: #if nz == 0:
    p = m.index('1') * (-1)
    m2 = m[-p + 1::]
ans = '0' if sign == 1 else '1'
ans += bin(p + 127)[2::].zfill(8)
ans += m2[:23]
print(ans)
ans2=''
for i in range(0,29,4):
    match ans[i:i+4]:
        case '0000': ans2 += '0'
        case '0001': ans2 += '1'
        case '0010': ans2 += '2'
        case '0011': ans2 += '3'
        case '0100': ans2 += '4'
        case '0101': ans2 += '5'
        case '0110': ans2 += '6'
        case '0111': ans2 += '7'
        case '1000': ans2 += '8'
        case '1001': ans2 += '9'
        case '1010': ans2 += 'A'
        case '1011': ans2 += 'B'
        case '1100': ans2 += 'C'
        case '1101': ans2 += 'D'
        case '1110': ans2 += 'E'
        case '1111': ans2 += 'F'
print(ans2)