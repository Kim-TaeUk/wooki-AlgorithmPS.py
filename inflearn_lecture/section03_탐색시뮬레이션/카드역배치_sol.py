list = list(range(21))

for _ in range(10):  # 해당 반복문에서는 굳이 i를 할당하지 않아도 된다, _로 처리
    a, b = map(int, input().split())
    for i in range((b - a + 1) // 2):
        list[a + i], list[b - i] = list[b - i], list[a + i]
        # 값을 swap해주는 방식으로

list.pop(0)  # 0은 제외하고 출력해야 하니 pop(0)해서 맨 앞 원소 없에기
print(list)

# 범위가 2부터 7라고 하면 -> 2-7, 3-6, 4-5 이렇게 3번 swap해야 함
# (7-2) // 2 = 2이다 따라서 7-2+1의 몫으로 루프를 돌게 한다
# 범위가 3부터 7라고 하면 -> 3-7, 4-5 이렇게 2번 swap해야 함
# (7-3) // 2 = 2이다 어차피 2번 돈다
# +1한 것의 몫을 구해도 (7-3+1) // 2 = 2가 똑같이 나오기 때문에 일반성을 확보함

# 굳이 변수 안쓰고 _로 처리하는 idea
# 몫을 이용해서 반복횟수의 일반성 확보하는 idea
# python에서의 값 편리하게 swap
# 출력할 때 필요없는 부분 pop하는 idea
