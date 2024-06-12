drop table rowers;
drop table race_result;
drop table rower_race_results;

CREATE TABLE ROWERS(
ROWER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL
);


CREATE TABLE RACE_RESULT(
RACE_RESULT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
RACE TEXT NOT NULL,
PLACE INT NOT NULL,
TIME INT NOT NULL
);


create table ROWER_RACE_RESULTS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ROWER_ID INTEGER,
RACE_RESULT_ID INTEGER,
foreign key (ROWER_ID)
    references ROWERS (ROWER_ID)
foreign key (RACE_RESULT_ID)
    references RACE_RESULT (RACE_RESULT_ID)
);