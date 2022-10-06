import random
# import matplotlib.pyplot as plt


def win_count(n):
  if player_rpc.count(n) == 1:
    #print(player_rpc.index(n) + 1, "번째 사람 승리")
    count[n] += 1


print("사람 수, 반복 수를 입력하시오.")
player_number = input()
play_time = input()
print("경우의 수가 몇가지 입니까??(Ex: 가위,바위,보-3가지)")
case = input()
count = [0]  #1부터 입력값의 경우의수 입력

for i in range(0, int(case)):
  count.append(0)

for i in range(0, int(play_time)):
  player_rpc = []
  for j in range(0, int(player_number)):
    player_rpc.append(random.randrange(1, int(case) + 1))  #랜덤 경우의수 생성

  print("//////////////", i + 1, "번쨰 가위 바위 보//////////////")
  print("랜덤으로 생긴 경우의 수 ", player_rpc)

  for n in range(1, int(case) + 1):  # 누가 승리했는지 카운팅
    win_count(n)

#그래프 출력

# plt.xlim([0, 1000])      # X축의 범위: [xmin, xmax]
# plt.ylim([0, 1000])     # Y축의 범위: [ymin, ymax]
# plt.show()

#결과값 출력
print("총 인원:", player_number, ", 총 횟수", play_time)
for i in range(1, int(case) + 1):
  print(i, "경우의 수", count[i], "승리")
