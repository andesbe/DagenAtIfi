import time
from csv import writer

start = time.time()

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




answer = int(input("Write your answer here: "))
corr_answer = int(212)
var_session = True 

while var_session:
        
    if answer != corr_answer:
        print("Try again ya cunt!")
        answer = int(input("Write your answer here: "))
        
    else: 
        end = time.time()
        print("Well done m8!!")
        email = input("Please write your email here, it will only be used to contact the winner. ")
        name = input("Please write your name or preferred nickname here. It will only be used for leaderboard display: ")
        time = end - start 
        
        myCsvRow = [email, name, time]

        #Opening up the .csv file and writing the entry as a new row
        with open('leaderboard.csv','a') as fd:
            writer_object = writer(fd)
            writer_object.writerow(myCsvRow)
            fd.close()
        var_session = False 
        
        

