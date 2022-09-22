import time

def print_to_terminal():
    """
    Prints the leaderboard to the terminal every 60 seconds
    """
    while True:
        with open("show_leaderboard.txt", "r") as file:
            print('')
            print('')
            print('')
            print('')
            print(file.read())
            time.sleep(60)
        file.close()
        
print_to_terminal()