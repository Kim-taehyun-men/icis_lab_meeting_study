import random


count_s, count_r, count_p, count_no = 0, 0, 0, 0  # 반복 시 총 승리값
print("사람 수를 입력하시오.")
player_number = input()
print("몇번 반복하시겠습니까??")
play_time = input()

for i in range(0, int(play_time)):
  print("//////////////", i + 1, "번쨰 가위 바위 보//////////////")
  player_rpc = []
  for j in range(0, int(player_number)):
    player_rpc.append(random.randrange(1, 4))  #가위=1, 바위=2, 보=3

  if player_rpc.count(1) == 1:
    print(player_rpc.index(1) + 1, "번쨰 사람이 가위로 승리")
    count_s += 1

  if player_rpc.count(2) == 1:
    print(player_rpc.index(2) + 1, "번쨰 사람이 바위로 승리")
    count_r += 1

  if player_rpc.count(3) == 1:
    print(player_rpc.index(3) + 1, "번쨰 사람이 보로 승리")
    count_p += 1

  if (player_rpc.count(1) != 1 and player_rpc.count(2) != 1
      and player_rpc.count(3) != 1):
    print("승자는 없습니다.")
    count_no += 1

  # for k in range(len(player_rpc)):
  #   print("결과 검사",player_rpc[k])
print("총 인원:", player_number, ", 총 횟수", play_time)
print("가위 승: ", count_s, ", 바위 승: ", count_r, ", 보 승: ", count_p, ", 무승부: ",
      count_no)  ## 한판에 두명 이상 승리하는 경우가 생겨 총 횟수보다 승리의 수가 많다.
