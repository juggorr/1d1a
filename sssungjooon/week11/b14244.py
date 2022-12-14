# n과 m이 주어졌을 때, n개의 노드로 이루어져 있고, 
# m개의 리프로 이루어져 있는 트리를 만드는 프로그램을 작성하시오.
# (3 ≤ n ≤ 50, 2 ≤ m ≤ n-1)

# 첫째 줄에 n과 m이 주어진다.
n, m = map(int,input().split())

# 리프는 차수가 1인 노드이다.
# 리프가 2개라면 n개 개수에 상관없이 일직선으로만 된 트리이다.
# 따라서 트리의 간선 정보는 0부터 n-m까지 i, i+1 식으로 출력
if m == 2 :
    for i in range(0,n-m+1):
        print(f'{i} {i+1}')

else :
    # 그 외의 경우에는 여러 가지 방법이 있지만
    # 우선 일직선 양 끝 2개 리프를 제외한, 나머지 리프들은 하나의 노드에 다 붙여줘도 된다.
    # 따라서 리프이자 일직선으로 마지막에 있는 노드를 last_node로 지정하고
    # 나머지들은 노드 1에 다 붙여준다.
    last_node = n-m+1
    # 트리의 정점은 0번부터 n-1번까지 있다.
    for i in range(0,n):
        # 일직선으로 만들 노드들의 간선 정보 출력
        if i <= n - m :
            print(f'{i} {i+1}')
        # 리프이자 일직선 마지막 노드의 번호보다 큰 거는 다 한 노드에 다 붙여줘도 된다.
        # 나는 1번 선정 (1번이 일직선 시작번인 0번이나 일직선 끝번이 아니기 때문)
        elif i > last_node :
            print(f'1 {i}')