with open("input_day_1.txt", "r") as f:
    user_input = [line for line in f.readlines()]


def trebuchet(words_list):
    """Puts the first and last number that contains a word to
    make another number, then sums all the new values.

    Args:
        words_list (str): The input of the day put under a str format
    """

  # Creates a list that will be used to store the new values before making the sum of them
    list_values = []
  
    for selected_word in words_list: # Selects each word of the input at every iteration
        
        # print(selected_word) -- If you want to verify that your programs selects correctly the 
        #                         word
         
        # Creates a list to stock the numbers in the word, will be reset at every change of word
        list_numbers = []

        for caracter in selected_word: # Selects each caracter of the word
          try : 
            # Turns the caracter into an int
            int(caracter)
            # Adds the integer to the list 'list_numbers'
            list_numbers.append(caracter)

          # If a ValueError comes, this means the caracter is a str, so we won't do anything.
          except ValueError: 
            pass # Permits the program to skip a line
            
        # print(list_numbers) -- If you want to verify the list is well done for your tests

      # If the word only contains a single number
        if len(list_numbers) == 1: 

          # Adds the number two times to make a new number
          number_1 = str(list_numbers[0]) # Turns the integer to a str to concatenate them
          number_2 = str(list_numbers[0])
          
          # print("First number = " + number_1) -- If you want to verify you weren't wrong somewhere
          # print("Last number = " + number_2)  -- If you want to verify you weren't wrong somewhere

          value = number_1 + number_2 # Concatenates both values to maje a new value
          # print("Adding " + value) -- If you want to verify you weren't wrong somewhere


          list_values.append(int(value)) # Adds the new number to the list 'list_numbers'

        elif len(list_numbers) > 1: # If there's more than one number in the word
          
          number_1 = str(list_numbers[0]) # Turns the first number of the list into an str
          number_2 = str(list_numbers[len(list_numbers)-1]) # Turns the last number of the list into an str
          #print("First number = " + number_1)  -- If you want to verify you weren't wrong somewhere
          #print("Last number = " + number_2)   
          
          value = number_1 + number_2 #Concatenates the numbers to form a new one
          #print("Adding " + value)

          list_values.append(int(value)) # Adds the new number to the list 'list_numbers'
    
    return(sum(list_values))



print(trebuchet(user_input))
