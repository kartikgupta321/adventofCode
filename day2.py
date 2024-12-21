with open('day2.txt','r') as file:
  result = [list(map(int, line.split())) for line in file]

# print(result[0])
 
count = 0
for i in range(0, len(result)):
  data = result[i]
  # print(data)
  isSafe = True
  notSafe = 0
  if len(data) > 1:
    change = 1 if data[1] - data[0] > 0 else 0

  if change == 1:
    for j in range(1, len(data)):
        if data[j] - data[j-1] > 0 and abs(data[j - 1] - data[j]) >= 1 and abs(data[j-1] - data[j]) <= 3:
          isSafe = True
          
        else:
          if j + 1 == len(data):
            if notSafe == 0:
              notSafe += 1
              continue
            else:
              isSafe = False
            break
          if notSafe < 2 and data[j + 1] - data[j-1] > 0 and abs(data[j - 1] - data[j + 1]) >= 1 and abs(data[j-1] - data[j + 1]) <= 3:
            notSafe += 1
            continue
          else:
            isSafe = False
            break
  else:
    for j in range(1, len(data)):
      if data[j] - data[j-1] < 0 and abs(data[j - 1] - data[j]) >= 1 and abs(data[j-1] - data[j]) <= 3:
        isSafe = True
      else:
        if j + 1 == len(data):
          if notSafe == 0:
              notSafe += 1
              continue
          else:
            isSafe = False
          break
        if notSafe < 2 and data[j+1] - data[j-1] < 0 and abs(data[j - 1] - data[j+1]) >= 1 and abs(data[j-1] - data[j+1]) <= 3:
          notSafe += 1
          continue
        else:
          isSafe = False
          break
          

  
  if isSafe == True:
    # print(data, notSafe)
    count += 1

print(count)