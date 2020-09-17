def get_number(a,b,c,d):
    return 1000*a+100*b+10*c+d
a, b, c, d = 0, 0, 0, 0
for i in range(1,10):
    if a != 0:
        break
    for j in range(0,10):
        if a != 0:
            break
        for k in range(0,10):
            if a != 0:
                break
            for l in range(1,10):
                if get_number(i,j,k,l)*4 == get_number(l,k,j,i):
                    a,b,c,d = i,j,k,l
                    break

print(f'a = {a}\nb = {b}\nc = {c}\nd = {d}')
print(f'Test: {get_number(a, b, c, d)}*4 = {get_number(a, b, c, d)*4}')