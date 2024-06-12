'''

View or add result

V/A -> user input

V= list of boats -> query -> select all boats from table -> display to user
-> user inputs which boat they want to view results -> sql query to get results -> 

A= Add to database -> what to add -> 


make erd

'''

import datetime
print(str(datetime.timedelta(milliseconds=393320)))

'''

select RR.PLACE, RR.TIME, RR.BOAT, R.FIRSTNAME, R.LASTNAME
from rowing_results RR, Rowers R, resultrowers RRS
where RR.boat = "U17 Coxed Quad Sculls"
and RR.ID = RRS.RESULTID
and RRS.ROWERID = R.ROWER_ID

'''