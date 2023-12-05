with open('input_day_1.txt') as f:
  input_text = f.readlines()
def getCalibrationValue(input):
  input = input.replace("one", "on1e")
  input = input.replace("two", "tw2o")
  input = input.replace("three", "th3ree")
  input = input.replace("four", "f4our")
  input = input.replace("five", "fiv5e")
  input = input.replace("six", "s6ix")
  input = input.replace("seven", "se7ven")
  input = input.replace("eight", "eig8ht")
  input = input.replace("nine", "ni9ne")

  first = None
  second = None
  for i in input:
    if i.isdigit():
      if first == None:
        first = i
      second = i

  return int(first + second)

sum = 0
for i in input_text: 
  sum += getCalibrationValue(i)
print(sum)