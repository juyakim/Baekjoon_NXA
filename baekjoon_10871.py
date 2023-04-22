# 백준 10871:X보다 작은수
# A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.


# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
N, X = map(int, input().split())  # map함수를 이용하여 N는 10,X는 5를 정수(int)로 입력받기

# num 변수에 둘째줄 입력할 숫자들을 list에 int로 입력
A = list(map(int, input().split()))  # 예제입력 1 10 4 9 2 3 8 5 7 6

# for문을 이용해 range(N),
for i in range(N):  # N이 10이므로 i는 0부터 9까지 입력됨
    if A[i] < X:
        # list에 있는 숫자들이 X=5 보다 작을 때  출력됨
        print(A[i], end=" ")  # num[0~9]를 통해, end로 한칸씩 띄어주기
