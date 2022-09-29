import random

count_scissors = 0 
count_rock = 0 
count_paper = 0

print("특별한 가위바위보 게임")
print("사람 수를 입력하시오.")
player_number = input()
print(player_number)
player_rpc = []
for i in range(0,int(player_number)):
  a = random.randrange(1,4) #가위=1, 바위=2, 보=3
  player_rpc.append(a)

  
for i in player_rpc:
  result = player_rpc[i]
  print(result)
  if result == 1:
    count_scissors += 1
  elif result == 2:
    count_rock += 1
  else:
    count_paper += 1
