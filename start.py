import time
import pandas as pd
import csv
from functions import print_welcome_txt, loop_and_print, sort_and_return_top_entries, print_to_txt
import time



def main():
    #Taking the correct input and writing to leaderboard.csv
    print_welcome_txt()
    corr_answer = str(212)
    loop_and_print(corr_answer)
    
    #Updating the leaderboard
    top_entries = sort_and_return_top_entries()
    print_to_txt(top_entries)

if __name__ == "__main__":
    main()
