import pandas as pd


def sort_and_return_top_five(number):
    """_summary_
        loads the leaderboard csv file and returns the "number" top entries as a pandas df
    Returns:
        df: the top "number" entries from the leaderboard csv
        
    """
    leaderboard_unsorted = pd.read_csv("leaderboard.csv")
    leaderboard_sorted = leaderboard_unsorted.sort_values(by=["Time"])
    top_five = leaderboard_sorted.head(n=number)
    return top_five
    

def replace_lines(dataframe):
    """_summary_

    Args:
        filename (_type_): _description_
    """
    str1 = str("██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗ ██╗██╗\n")
    str2 = str("██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██║██║\n")
    str3 = str("██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║██║██║\n")
    str4 = str("██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║╚═╝╚═╝\n")
    str5 = str("███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██╗██╗\n")
    str6 = str("╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝\n")
    print(dataframe)
    dataframe_new = dataframe.drop("emails", axis = 1)
    with open("test.txt", "w") as file:
        file.write(str1)
        file.write(str2)
        file.write(str3)
        file.write(str4)
        file.write(str5)
        file.write(str6)
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        dfAsString = dataframe_new.to_string(header=True, index=False)
        file.write(dfAsString)
    file.close()       
                
scoreboard = sort_and_return_top_five(10)            
print(scoreboard)
replace_lines(scoreboard)