N = int(input())

tiles = [0, 1, 3]

def tiling(n):

    if n <= 2:
        return tiles[n]
    
    else:
        k = len(tiles)

        if k < n + 1:

            while k < n + 1:
                tiles.append(tiles[k - 1] + tiles[k - 2] * 2)
                k += 1

        return tiles[n]
    
print(tiling(N) % 10007)