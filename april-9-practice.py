# Create a document that explains what this practice is. Document your struggles, what the goal of the practice was, what you learned along the way, etc. Also, learn how to link the file to the document in here, 
# and convert the practice into an html web page. In this file, we are practicing functions & list. 


# create a list with 8 numbers
nums = ["3",'2',"5","7",'8','9','6','4','1','22','16']


# create a math game that doesn't end until the total is 100. You can only 
# use the numbers in the list, and only have the option of using multiplication one time. 


#Create a function to implement this small project into a bigger one eventually so you can practice functions and working with multiple functions.
def get_user_numbers():


    #Create a loop
    while True:
        
        print()
        print()
        print()


        #Prompt the user to play the game
        print('''Welcome!    Can you get to over 100 using only the numbers below? To throw a curve ball, we're only allowing
            you to use multiplication one time. *HINT* You will use all of the numbers but one of them.
            Type 'y' to play
            Type 'n' to exit''')

        #We convert their input into a lowercase
        access = input("> ").lower()

        # They can only play the game if they enter y, after doing so, we enter into a loop
        if access == 'y':
            print()
            print()
            print()
            
            print(nums)
            print()
            print('Use the above integers to fill in the equation below & win the game. ')
            print('_ x _ + _ + _ + _ + _+  _ + _')
            while True:
                
                filled = input('Type the numbers here with no spacing >> ')


                # Make sure they entered valid whole numbers. If not, repeat the number entry.                 
                if filled.isdigit():
                    
                    #convert the filled data into a list and then print out the list for user to see
                    list(filled)
                    #print out the list seperated by commas
                    print(f"Your entry >>> {', '.join(filled)}")

                    #convert every value in the list into an integer
                    filled = [ int(num) for num in filled]
                    #multiply the first two indexes of the list
                    multi_1 = (filled[0]) * (filled[1])
                    #add the last 4 indexes of the list
                    add_1 = (filled[2]) + (filled[3]) + (filled[4]) + (filled[5]) + (filled[6]) + (filled[7]) + (filled[8])
                    #add both together
                    answer = (multi_1 + add_1)
                    if answer != 100:
                        print(f'You got {answer}. Try again. ')
                        continue
                    else:
                        print(f"You got {answer}. Good job! ")
                        break
                    

                    
                else:
                     print()
                     print("** Please enter 8 valid numbers. **")
                     print()
                     continue
                         
                    
        else:
            break



get_user_numbers()


    

            

