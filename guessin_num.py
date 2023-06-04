import random

max_num = 1000          # Maximum value of picked number
min_num = 0             # Minimum value of piecked number
guess_counter = 0               # Value of PCs' guess

# List which contains all possile to pick numbers
num_list = list(        
           range(
           min_num, max_num))    

# Index of the number in the middle of the num_list
centre_list_index = int (len  #
                  (num_list)/2) 

# Loop which checks the answer:
while True:
    pc_guess =  num_list[centre_list_index]
    answer = input (f"Mój strzał to: \n {pc_guess} \n Trafiłem? odp: dużo/mało/dycha \n >>>")
    
# When the number is correctly picked  
    if answer == "dycha":
        print("Strzał w dziesiątkę")
        guess_counter += 1
        break

# When guessed number is to low
    elif answer == "mało":
       num_list = num_list[centre_list_index:max_num]
       centre_list_index = int(len(num_list)/2)
       guess_counter += 1

# When answer say its too low but only 1 number in a list position left
       if len(num_list) == 1:
            print(f"{num_list[0]} musi być właściwym numerem")
            break

# When guessed number is too high
    elif answer == "dużo":
        num_list = num_list[ min_num: centre_list_index]
        centre_list_index=int(len(num_list)/2)
        guess_counter+=1

# When answer say its too high but only 1 number in a list position left 
        if len(num_list)==1:
            print(f"{num_list[0]} musi być właściwym numerem")
            break

# If answer contains chars not specified in input quotation
    else:
        print("Zły format")
        continue

# Print the summary after the game.    
print(f" Twój numer to {pc_guess}. \n Udało Mi się w {guess_counter} próbach")

   