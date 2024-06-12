-- Select U16 Quad
select RR.RACE, RR.PLACE, RR.TIME, R.FIRSTNAME, R.LASTNAME
    from race_result RR, rowers R, rower_race_results RRR
    where RR.RACE = "U16 Coxed Quad Sculls"
    and RR.RACE_RESULT_ID = RRR.RACE_RESULT_ID
    and RRR.ROWER_ID = R.ROWER_ID