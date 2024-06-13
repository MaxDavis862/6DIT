import sqlite3
import datetime

conn = sqlite3.connect('/Users/maxdavis/Dev/DIT/6DIT/rowing1.db')
cursor = conn.cursor()

#SQL Statement to get boat data, the print the statement after the fetchall
def getrace(race):
    #querystr = f'select RR.PLACE, RR.TIME, R.FIRSTNAME, R.LASTNAME from race_result RR, rowers R, rower_race_results RRR where RR.RACE = \'{racenames[race]}\' and RR.RACE_RESULT_ID = RRR.RACE_RESULT_ID and RRR.ROWER_ID = R.ROWER_ID'
    querystr = f'select RR.PLACE, RR.TIME, R.FIRSTNAME, R.LASTNAME from race_result RR, rowers R, rower_race_results RRR where RR.RACE_RESULT_ID = {race} and RR.RACE_RESULT_ID = RRR.RACE_RESULT_ID and RRR.ROWER_ID = R.ROWER_ID'

    cursor.execute(querystr)
    queryresult = cursor.fetchall()

    duration = str(datetime.timedelta(milliseconds=queryresult[0][1]))
    print(f'Place: {queryresult[0][0]} \t Time: (min:sec:ms) {duration[2:10]}')
    print(f'Firstname \t Lastname')
    for row in queryresult:
        if len(row[2]) <= 6:
            print(f'{row[2]} \t\t {row[3]}')
        else:
            print(f'{row[2]} \t {row[3]}') 
        
def getrower(rower):
    querystr = f'select  R.FIRSTNAME, R.LASTNAME, RR.RACE, RR.PLACE, RR.TIME from race_result RR, rowers R, rower_race_results RRR where R.ROWER_ID = \'{rower}\' and RR.RACE_RESULT_ID = RRR.RACE_RESULT_ID and RRR.ROWER_ID = R.ROWER_ID'
    cursor.execute(querystr)
    queryresult = cursor.fetchall()   
    print(f'Race: \t\t\t Place: \t Time: (min:sec:ms)')
    for row in queryresult:    
        duration = str(datetime.timedelta(milliseconds=row[4]))
        if len(row[2]) <= 6:
            print(f'{row[2]} \t\t {row[3]} \t\t {duration[2:10]}')
        else:
            print(f'{row[2]} \t {row[3]} \t\t {duration[2:10]}')

def addrower(firstname,lastname):    
    sqlstr = f"insert into rowers (\"firstname\",\"lastname\") values (\"{firstname}\", \"{lastname}\")"    
    conn.execute(sqlstr)
    conn.commit()
           
def addrace(race, place, time):
    sqlstr = f"insert into race_result (\"race\",\"place\",\"time\") values (\"{race}\", {place}, {time})"    
    conn.execute(sqlstr)
    conn.commit()
    
def addrowertorace(rower_id, race_result_id):
    sqlstr = f"insert into rower_race_results (\"rower_id\",\"race_result_id\") values ({rower_id}, {race_result_id})"    
    conn.execute(sqlstr)
    conn.commit()    

def getrowers():
    querystr = f'select rower_id, firstname, lastname from rowers'
    cursor.execute(querystr)
    queryresult = cursor.fetchall()
    for row in queryresult:
        print(row)

def getraceresult():
    querystr = f'select race_result_id, race from race_result'
    cursor.execute(querystr)
    queryresult = cursor.fetchall()
    for row in queryresult:
        print(row)

def main():    
    print()
    VA = str.upper(input("Add or view data? Use A or V "))    
    if VA == "V":
        RB = str.upper(input("Filter data by race or by rower? Use RACE or ROWER "))        
        if RB == 'ROWER':           
            getrowers()
            rower = str(input("What rower from the above list would you like to see results for? Use the leftmost number. "))            
            getrower(rower)
            main()
        elif RB == 'RACE':
            getraceresult()
            race = str(input("What race result from the above list would you like to view? Use the leftmost number. "))    
            getrace(race)
            main()
        else:
            print('Not a valid option. Try again.')
            main()
    elif VA == "A":    
        option = str.upper(input("Add Rower (ARO), Add Race (ARA), Add Rower to a Race (ARR)"))
        print(option)
        if (option == "ARO"):                   
            firstname = input("What is the rowers first name? ")
            lastname = input("What is the rowers last name? ")
            addrower(firstname,lastname)
            main()
        elif (option == "ARA"):
            race = input("What is the race name? ")
            place = input("What place did the boat come? ")
            time = int(input("What time did the boat get? (Please enter in milliseconds e.g. 393320) "))
            addrace(race,place,time)
            main()
        elif (option =="ARR"):
            # select # from rowers, show and prompt to select
            getrowers()
            rower_id = input("select the ROWER_ID value the rower to add to a race ")
            getraceresult()
            race_result_id = input("select the race_result_id value the race to add the rower to ")
            addrowertorace(rower_id,race_result_id)  
            main()
        else:
            print('Not a valid option. Try again')
            main()
    else:
        print('Not a valid option. Try again')
        main()        

if __name__ == "__main__":
    main()















#while(True):
 #   cols = stat.split(',')
    
    '''query = statementbuilder(cols)
    whole_roster(query)'''
    #break
    #else:
    #    print("Invalid input")

conn.close()


'''
def statementbuilder(options):   #
    columns = ''
    for i in options:             # iterates over the data from options
        columns += column_names[i]    #  adds the name of each column to the string saved under columns
        columns += ','               #   adds a comma after each name of column in the string
    cols = columns[:len(columns)-1]    #  removes the last character in the line
    return f'select {cols} from '

def whole_roster(query):
    #cursor.execute('select * from basketballdata;')    
    cursor.execute(query) 
    wholeroster = cursor.fetchall()
    ## in here print headers from cursor
    for i in wholeroster:
        print (i)
'''
#headings = [description[0] for description in cursor.description]
#print (headings[1])