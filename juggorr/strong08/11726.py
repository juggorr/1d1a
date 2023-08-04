N = int(input())

# 0일때는 0으로?
# 1일 때는 1가지
# 2일 때는 가로두개, 세로두개
# 3일 때는
# 1칸 채우고 + 2
# 2칸 채우고 + 1

# 메모이제이션 활용?
tiles = [0, 1, 2]

def tiling(N):

    if N  <= 2:
        
        return tiles[N]

    else:
        n = len(tiles)

        # 구하고자 하는 숫자가 기록되어있지 않다면
        if n < N + 1:
            # 구하고자 하는 숫자를 기록할 때 까지
            while n <= N:
                tiles.append(tiles[n - 1] + tiles[n - 2])
                n += 1        

        # print(tiles)
        return tiles[N]

print(tiling(N) % 10007)
