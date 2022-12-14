import pandas as pd
import time
import csv

def print_welcome_txt():
    """prints the welcome text
    """
    print('')
    print('')
    print('')
    print('')
    print('░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗')
    print('░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝')
    print('░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░')
    print('░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░')
    print('░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗')
    print('░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝')
    print('')
    print('')
    print('')
    print('')
    
        
def loop_and_print(corr_answer):
    """takes the answer input and if correct, appends a new line to the leaderboard.csv file with the contestant info

    Args:
        ans_int (int): the number of vowels in the text according to the contestant
    """
    start = time.time()
    var_session = True 

    while var_session:
        answer = str(input("Write your answer here: "))
        if answer != corr_answer:
            print("Try again please!")
            #answer = (input("Write your answer here: "))
            
        else: 
            end = time.time()
            print("Well done m8!!")
            email = input("Please write your email here, it will only be used to contact the winner:  ")
            name = input("Please write your name or preferred nickname here. It will only be used for leaderboard display: ")
            time_elapsed = end - start 
            
            myCsvRow = [email, name, time_elapsed]

            #Opening up the .csv file and writing the entry as a new row
            with open('leaderboard.csv','a') as fd:
                writer_object = csv.writer(fd)
                writer_object.writerow(myCsvRow)
                fd.close()
            var_session = False 


def sort_and_return_top_entries():
    """
        loads the leaderboard csv file and returns the "number" top entries as a pandas df
    Returns:
        df: the top "number" entries from the leaderboard csv
        
    """
    leaderboard_unsorted = pd.read_csv("leaderboard.csv")
    leaderboard_sorted = leaderboard_unsorted.sort_values(by=["Time"])
    top_entries = leaderboard_sorted.head(20)
    return top_entries
    

def print_to_txt(dataframe):
    """
    Writes over the current text file with the new results everytime it is called
    Args:
        df: a dataframe with the n fastest entries
    """
    str1 = str("██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗ ██╗██╗\n")
    str2 = str("██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██║██║\n")
    str3 = str("██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║██║██║\n")
    str4 = str("██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║╚═╝╚═╝\n")
    str5 = str("███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██╗██╗\n")
    str6 = str("╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝\n")
    dataframe_new = dataframe.drop("emails", axis = 1)
    with open("show_leaderboard.txt", "w") as file:
        file.write(str1)
        file.write(str2)
        file.write(str3)
        file.write(str4)
        file.write(str5)
        file.write(str6)
        file.write("\n")
        file.write("\n")
        file.write("\n")
        dfAsString = dataframe_new.to_string(header=True, index=False)
        file.write(dfAsString)
    file.close()       
                
