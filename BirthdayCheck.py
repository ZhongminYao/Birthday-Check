import datetime
#initializing all global variables
date_now = datetime.datetime.now()
date_user = datetime.datetime.now()
date_year_now = 0
date_dayTotal_now = 0  # if it's Jan 8th, then this variable = 8, like the day in the year
name_user = "name"
year_user = 0
month_user = 0
day_user = 0

date_user_dayTotal = 0
user_date_list = []
user_name_list = []
user_dic_byName = {}
user_dic_byIndex = {}

switch = True   # a boolean variable that is returned in a function 
                # in order to control a while statement

# A function that reads the current time
def readDateNow():
    global date_now
    global date_year_now
    global date_dayTotal_now

    date_now = datetime.datetime.now() # get the current time as data type datetime.datetime
    date_year_now = int(date_now.strftime("%Y"))  # get the year 
    date_dayTotal_now = int(date_now.strftime("%j")) # get the day in the year

# A function that read the user input
def readDateUser():
    global name_user
    global year_user
    global month_user
    global day_user
    global user_date_list
    global date_user_dayTotal
    
    name_user = input("What's your name?\n")
    while True:   # make sure that the input is correct
        str_year_user = input("Please enter the 4 digit year you were born.\n")
        if len(str_year_user) == 4:   # check if the input is 4 digit
            break
    year_user = int(str_year_user)  # change to integer
    while True:   # make sure that the input is correct
        str_month_user = input("Please enter the numercal month you were born.\n")
            # make sure that the input is either 1 digit or 2 digit
        if len(str_month_user) == 1 or len(str_month_user) == 2:
            break
    month_user = int(str_month_user) # change to integer
    while True:
        str_day_user = input("Please enter the day you were born.\n")
            # make sure that the input is either 1 digit or 2 digit
        if len(str_day_user) == 1 or len(str_day_user) == 2:
            break
    day_user = int(str_day_user)  # change to integer

    # assign these three variable as date with data type datetime.datetime
    date_user = datetime.datetime(year_user, month_user, day_user) 
    user_date_list.append(date_user) # add the date to the list
    user_name_list.append(name_user) # add the name to the list
    date_user_dayTotal = int(date_user.strftime("%j"))  # get the day in the year

 # two global variables   
age_user = 0
dayDif_user = 0

# a function that calulate the age
def birthdayCheck():
    global age_user
    global dayDif_user
    if date_dayTotal_now >= date_user_dayTotal:
        age_user = date_year_now - year_user
        dayDif_user = date_dayTotal_now - date_user_dayTotal
    elif date_dayTotal_now < date_user_dayTotal:
        age_user = date_year_now - 1 - year_user
        dayDif_user = date_dayTotal_now + 365 - date_user_dayTotal
    else:  
        print("Something Wrong\n")
    if dayDif_user == 0:
        print("Happy Birthday!")


# a class that can read in values from argument and print out the result
class User:
    def __init__(self, name, age, days):
        self.name = name
        self.age = age
        self.days = days

    def showMsg(self):
        print("You are " + str(self.age) + " years and " + str(self.days) + " days old!")

# use list comprehension to print all elements in the list
def printList():
    [print(element) for element in user_date_list if element != None]

# a funciton that pass arguments to corresponding functions
def printDic(name, index, choice):
    if choice == 'n':
        print(user_dic_byName[name])
    if choice == 'i':
        print(user_dic_byIndex[index])

# ask user to play again
def askAgain(prompt, retries = 3, reminder = "Please try again!\n"):  # default argument
    while True:
        user_answer = input(prompt)
        if user_answer in ('y', 'ye', 'yes'):
            return True
        if user_answer in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1  # chance is decremented by 1
        if retries < 0 :
            raise ValueError('Invalid user response\n')
        print(reminder)

# a funciton that ask user if he/she want to see the date list
def askReviewList():
    while True:
        user_answer = input("Do you want to review all the dates you have checked?\n")
        if user_answer in ('y', 'ye', 'yes'):
            printList()
            break
        elif user_answer in ('n', 'no', 'nop', 'nope'):
            break
        else: 
            print("Please just type 'y' or 'n' ")

# ask user how he/she wants to search the dictionary
def askSearchDic_How():
    global user_dic_byName
    global user_dic_byIndex
    # use zip to combine two lists into a dictionary
    user_dic_byName = dict(zip(user_name_list, user_date_list)) 
    # use enumerate to generate a dictionary with date list and corresponding index
    user_dic_byIndex = {index:element for index,element in enumerate(user_date_list)}

    while True:
        user_answer = input("How do you want to search? Name or Index?\n")
        if user_answer in ('Name', 'name', 'n'):
            while True:
                name_search = input("What is the name?\n")
                if name_search in user_dic_byName:  # check if the key is in the dictionary
                    printDic(name_search,0,'n')
                    break
                else:
                    print("Please make sure the name is correct and you really checked that name ")
            break
        elif user_answer in ('Index', 'index', 'i', 'ind'):
            while True:
                while True:
                    try:
                        index_search = int(input("What is the index(number)?\n"))
                    except ValueError:
                        print("Please only type numbers for index.\n")
                        continue
                    else:
                        break

                if index_search in user_dic_byIndex: # check if the key is in the dictionary
                    printDic(" ",index_search, 'i') 
                    break
                else:
                    print("index 0 means the first person you checked, keep in mind.\n")
            break
        else: 
            print("Please just type 'n' or 'i' \n")

def askSearchDic():
    while True:
        user_answer = input("Do you want to search for a specific date you have checked?\n")
        if user_answer in ('y', 'ye', 'yes'):
            askSearchDic_How()
        elif user_answer in ('n', 'no', 'nop', 'nope'):
            break
        else: 
            print("Please just type 'y' or 'n' ")

 
def main():
    global switch
    try:
        while(switch):
            readDateNow()
            readDateUser()
            birthdayCheck()
            user1 = User(name_user, age_user, dayDif_user)    
            user1.showMsg()
            switch = askAgain("Do you want to start over?\n")
            if switch:  # if user wants to play again
                pass
            else:   # if user does not want to play again
                switch == False   
                break
        
        askReviewList()
        askSearchDic()
    
    # specific exception catch
    except ValueError: 
        print(""" Wrong answer!!!
        Make sure you type 'y','ye','yes' if you want to start over,
        and you type 'n','no','nop', 'nope' if you want to quit 
        """)
    except:
        print("An exception occurred\n")

if __name__== "__main__":
    main()
    
