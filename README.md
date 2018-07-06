# LogsAnalysis
Logs data analysis report of a news database usingLogs data analysis report of a news database using postgresql and Python. This project was evaluated and met specifications as a part of the full stack web developer NanoDegree program by Udacity. postgresql and Python.

#Installation:

1- install python3.3

2- install postgresql

3- install virtualbox or set up Linux

4- install vagrant

    -run the command vagrant up
    -run the command vagrant ssh

5- create views in postgresql
        -"create or replace view dataerror as "
                "select substring(cast(log.time as text), 0, 11) as date, "
                "count(log.status) as error "
                "from log "
                "where log.status like '%404%' "
                "group by date "
                
        -"create or replace view  alldata as "
                "select substring(cast(log.time as text), 0, 11) as date , count(log.status) as all from log "
                "group by date "
                
        -"create or replace view final_query as "
                "select alldata.date, "
                "((dataerror.error / alldata.all::float)*100) as all_error "
                "from alldata "
                "inner join dataerror on alldata.date=dataerror.date "
             
#Requirements:
1-database.py

2-output.txt

3- download newdata.sql file from "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"

#How to run the project?

1- Open IDLE (Python 3.3) .

2- install postgres

3- run psql -d news -f newsdata.sql

4- run python database.py
