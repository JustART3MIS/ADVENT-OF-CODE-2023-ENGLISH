with open("input_day_2.txt", "r") as f:
    user_input = f.readlines()

bag_cubes = {
  "red": 12,
  "green": 13,
  "blue": 14
}
answer = 0

def conundrum(input):
  # Adds the variable created before inside of the function without needing it as an argument
  global answer 
  
	for line in input: # Will set 'line' as the next line at every iteration
        
  possible = True # Initialising 'possible' as True
        
  # Splits the line in two using ':' as a mark. Stores what's before in 'id_' 
  # and what's after in 'line'
  id_, line = line.split(": ") 
        
  # Splits the line in two where there's a space, and stores what's after in 'id_number'
  id_number = id_.split(" ")[1]

	# At every iteration, 'part' will be a part of the sentence splitted where there is a ';'
  for part in line.split("; "): 
		for ball in part.split(", "):
			count, color = ball.split()
			if int(count) > bag_cubes[color]:
				possible = False
  	
			# print("Possible :", possible, id_number)
  
  	if possible == True:
			answer += int(id_number)
    
	return(answer) # Returns the sum of all the possible game numbers
    
print(conundrum(user_input))
