N, M = map(int, input().split())

facs = [1, 1]

def fac(n):

    k = len(facs)
     
    if n > 1 and k <= n:
        while k < n + 1:
            facs.append(k * facs[k - 1])
            k += 1
          
    return facs[n]

up = 1

for i in range(M):
    up *= (N - i)

# print(up)

print(up // fac(M))
