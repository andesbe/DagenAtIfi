import pandas as pd

class leaderboard:
    
    def __init__():
        


    def sort_and_return_top_five():
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
                