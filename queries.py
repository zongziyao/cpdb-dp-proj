algtn_by_area_qstr = "select area_id,\
 count(allegation_id) as total_allegation\
 from data_allegation_areas\
 where area_id = 1546\
 group by area_id;"
#  order by total_allegation desc limit 1;"

algtn_by_race_qstr = "select race,\
 count(allegation_id) as total_allegation\
 from data_victim\
 where race = 'Black'\
 group by race;"

algtn_by_race_and_gender_qstr = "select race,\
 count(allegation_id) as total_allegation\
 from data_victim\
 where race = 'Asian/Pacific Islander'\
 and gender = 'F'\
 group by race;"

officer_population_by_race_qster = "select race,\
 count(id) as total_population\
 from data_officer\
 group by race\
 order by total_population desc limit 1;"

algtn_by_officer_id_qster = "select officer_id,\
 count(allegation_id) as total_allegation\
 from data_officerallegation\
 where officer_id = 12\
 group by officer_id;"
