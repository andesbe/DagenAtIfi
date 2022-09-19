class Team:
    def __init__(self, num, name, size, score):
        self.num = num
        self.name = name
        self.size = size
        self.score = score

    def add_victory(self):
        self.score += 1

    def __repr__(self):
        return f'Team Number: {self.num} |-| Team Name: {self.name} |-| Member Count: {self.size} |-| Team Score: {self.score}'

def NewTournament():
    teams = []

    TeamCounter=int(input('How many Teams will be in the tournament? '))

    print('')
    for i in range(TeamCounter):
        NameOfTeam=input(f'Please Enter Team {i+1} Name: ')
        MemberCount=int(input('How Many Members in Team? '))
        print('')
        teams.append( Team( i+1, NameOfTeam, MemberCount, 0) )


def Score(teams):
    winner = input('Which Team Won the Event? ')
    for team in teams:
        if team.name == winner:
            team.add_victory()
            break
            print('Updated Leaderboard')

def Leaderboard():
    for t in teams: #does not work, does nothing
        print(t)
    
def Menu():
    MenuLoop=1
    while MenuLoop==1:
        print('1.Create Tournament')
        print('2.Update Existing Tournament')
        print('3.View Leaderboard')
        print('4.Exit')
        MenuOption=input('')
        if MenuOption=='1':
            print('Creating Tournament')
            NewTournament()#runs the new tournament function
            MenuLoop-=1
            Menu()
        elif MenuOption=='2':
            print('Updating Tournament')
            MenuLoop-=1
            EventName=input('Which Event Was Completed? ')
            winner=input('Which Team Won the Event? ')
            print('Event Winner:', winner, '||', 'Event:',EventName)
            print('Is this correct? Y/N')
            Check=input('')
            if Check=='y':
                print('Updating Leaderboard')
                Score(teams)
                Menu()
                    
                
                
        elif MenuOption=='3':
            MenuLoop-=1
            Leaderboard()
                
        elif MenuOption=='4':
            print('Exiting Program...')
        else:
            print('Error, please choose an option from the list below.')#keeps looping if user is not choosing a correct number from list


#start of program
teams = []        

print('░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗')
print('░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝')
print('░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░')
print('░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░')
print('░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗')
print('░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝')#welcome user
print('')
Username=input('Enter Username: ')
Password=input('Enter Password: ')
if Username =='Admin' and Password == 'Admin':#very basic login system for security of school
    print('Logging in...')
    print('User Verified')
    Menu()
else:
    print('User Does Not Exist.')#stops pupils gaining unauthorised access