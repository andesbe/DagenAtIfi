import pandas as pd
import numpy as np

def sort_leaderboard():
    leaderboard_unsorted = pd.read_csv("leaderboard.csv")
    leaderboard_sorted = leaderboard_unsorted.sort_values(by=["time"])
    print(leaderboard_sorted)
    
    
def return_top_five(leaderboard_sorted):
    last_five = leaderboard_sorted.ix[5:]
    
sort_leaderboard()