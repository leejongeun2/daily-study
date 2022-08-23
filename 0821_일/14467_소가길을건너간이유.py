# 소의 위치를 n번 관찰, 각 관찰은 <소의 번호와// 소의 위치> 하나씩으로 이루어져 있음
# 소의 번호는 1이상 10이하의 정수이고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1중의 하나
# 소가 길을 건너간 횟수 출력 

import sys
sys.stdin = open("14467_input.txt")

cow = [[-1]*10, [0]*10] # 각 소들의 숫자와 위치를 이차원배열 생성
# 소들의 숫자는 -1과 0으로 초기화
# 0의 자리 -1리스트생성, 1의 자리 0의 리스트 생성 
# -1로 생성한 이유는 새롭게 -1로 초기화해서 소의 이동숫자를 입력 받으려고, 예를 들어 같은 소가 한번 더 이동하기 위해 입력 받을 경우 
# 다음 if절로 넘어가고 거기서 이동을 한지, 안한지 체크 해줌
# 즉, 소가 처음이면 첫번쨰 조건절에서 확인, 소가 한번 입력 받은적 있는 소라면 두번째 조건절에서 확인

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())


    # 아래 n-1인 이유는 소의 번호를 인덱스 자리에 맞춰서 진행할려고.
    if cow[0][n-1] == -1: # 이차원배열 0,2(소의번호)의 자리가 -1일때, => 다음줄 입력 값인 경우 동일하므로, 해당 조건 성립 안됨
        #즉, 위의 조건절은 각 소 별로, 이동 시작을 했는지 확인하여 시작을 안했다면(-1) 그것을 소의위치로 바꿔줌
        cow[0][n-1] = m # 해당자리를 1(첫번째 예제)로 바꿈
        continue # 아래코드 실행안하고 for문으로 점프
    if cow[0][n-1] != m: # 0, 2(소의번호)가 0(소의위치)이 아닐 때 => 소의 위치가 이전 위치와 다를 때
        cow[0][n-1] = m # 입력 받은 소의위치로 변경해줌
        cow[1][n-1] += 1 # 이차원배열 1의 자리 리스트에는 소가 몇번 이동했는지 체크하기 위함임
        continue

print(sum(cow[1])) # 소가 몇번이동했는지 체크하는 cow의 1인덱스의 합을 구함


    

