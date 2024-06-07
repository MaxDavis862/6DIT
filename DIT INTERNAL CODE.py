import sqlite3

column_names = {
    "1":"boat",
    "2":"boattime",
    "3":"boatplace",
}

conn = sqlite3.connect('INTERNAL.db')

cursor = conn.cursor()

def statementbuilder(options):   #
    columns = ''
    for i in options:             # iterates over the data from options
        columns += column_names[i]    #  adds the name of each column to the string saved under columns
        columns += ','               #   adds a comma after each name of column in the string
    cols = columns[:len(columns)-1]    #  removes the last character in the line
    return f'select {cols} from Maxrowing;'

def whole_roster(query):
    #cursor.execute('select * from basketballdata;')    
    cursor.execute(query) 
    wholeroster = cursor.fetchall()
    ## in here print headers from cursor
    for i in wholeroster:
        print (i)

#headings = [description[0] for description in cursor.description]
#print (headings[1])

while(True):
    stat = str(input("What statistic would you like?\n1. Boat\n2. Boat time\n3.Boat place\neg. 1,2,3 "))
    cols = stat.split(',')
    
#if 'key1' in my_dict:
#    print("blah")
#else:
#    print("boo")

#    if 1 <= stat <= 7:
#        input = ["1","2","3"]
    query = statementbuilder(cols)
    whole_roster(query)
    #break
    #else:
    #    print("Invalid input")

conn.close()


