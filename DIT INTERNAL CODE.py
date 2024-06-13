import sqlite3
import datetime

column_names = {
    "1":"rowers",
    "2":"time",
    "3":"place",
}

rowernames = {
    '1':'Max Davis',
    '2':'Jasper Crawford',
    '3':'Charlie Manser',
    '4':'Seb Watson',
    '5':'Harry Lightfoot',
    '6':'Abbey Pedersen',
    '7':'Mia Pagan',
    '8':'McKellar Thornton',
}

racenames = {
    "0":"U17 Coxed Quad Sculls",
    "1":"U16 Coxed Quad Sculls",
    "2":"U16 Double Sculls",

}
conn = sqlite3.connect('/Users/maxdavis/Dev/DIT/6DIT/rowing1.db')

cursor = conn.cursor()


#SQL Statement to get boat data, the print the statement after the fetchall
def getrace(race):
    querystr = f'select RR.PLACE, RR.TIME, R.FIRSTNAME, R.LASTNAME from race_result RR, rowers R, rower_race_results RRR where RR.RACE = \'{racenames[race]}\' and RR.RACE_RESULT_ID = RRR.RACE_RESULT_ID and RRR.ROWER_ID = R.ROWER_ID'

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
    
    '''querystr = f'select  R.FIRSTNAME, R.LASTNAME, RR.RACE, RR.PLACE, RR.TIME from race_result RR, rowers R, rower_race_results RRR where R.ROWER_ID = \'{rowernames[rower]}\' and RR.RACE_RESULT_ID = RRR.RACE_RESULT_ID and RRR.ROWER_ID = R.ROWER_ID'''

    querystr = f'select  R.FIRSTNAME, R.LASTNAME, RR.RACE, RR.PLACE, RR.TIME from race_result RR, rowers R, rower_race_results RRR where R.ROWER_ID = \'{rower}\' and RR.RACE_RESULT_ID = RRR.RACE_RESULT_ID and RRR.ROWER_ID = R.ROWER_ID'

    cursor.execute(querystr)
    queryresult = cursor.fetchall()

    #print(queryresult)
    #milliseconds = int(queryresult[0][1])
    #duration = str(datetime.timedelta(milliseconds=milliseconds))
    #duration = str(datetime.timedelta(milliseconds=queryresult[0][1]))
    #print(f'Place: {queryresult[0][0]} \t Time(min:sec:ms): {duration[2:10]}')
    
    print(f'Race: \t\t\t Place: \t Time: (min:sec:ms)')
    for row in queryresult:
        if len(row[2]) <= 6:
            print(f'{row[2]} \t\t {row[3]} \t\t {row[4]}')
        else:
            print(f'{row[2]} \t {row[3]} \t\t {row[4]}')

def addrower():
    '''
    sql insert

    cursor.execute(sql insert)
    
    
    
    
    '''
    


def addrace():
    'addrace'




VA = str.upper(input("Add or view data? Use A or V "))

if VA == "V":
    RB = str.upper(input("Filter data by race or by rower? Use RACE or ROWER "))
    
if VA == "A":
    print("add result")

if RB == 'ROWER':
    rower = str(input("What rower would you like to see results for? \n1 for Max Davis\n2 for Jasper Crawford\n3 for Charlie Manser\n4 for Seb Watson\n5 for Harry Lightfoot\n6 for Abbey Pedersen\n7 for Mia Pagan\n8 for McKellar Thornton "))
    print('You have selected ' + rowernames[rower])
    getrower(rower)

if RB == 'RACE':
    race = str(input("What race would you like to view?\n0 for U17 Quad\n1 for U16 Quad\n2 for U16 Double "))
    print('You have selected ' + racenames[race])
    getrace(race)

    
if RB != "RACE" or "ROWER":
    print("Invalid input. Try using 'RACE' or 'ROWER' ")
















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