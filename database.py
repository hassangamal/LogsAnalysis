# pick random word

import psycopg2


def question_one():
    conn = psycopg2.connect("dbname=news user=postgres"
                            " password=hassan host=localhost")
    cur = conn.cursor()
    cur.execute("select title , count(*) as num_view "
                "from  articles inner join log "
                "on log.path like concat('%', articles.slug, '%') "
                "where log.status like '200%'"
                "group by articles.title "
                "order by num_view desc "
                "limit 3")
    rows = cur.fetchall()
    print("1. What are the most popular three articles of all time?")
    idx = 1
    for row in rows:
        print(idx, ' - ', row[0], ' -> ', row[1])
        idx += 1
    conn.commit()
    cur.close()
    conn.close()


def question_two():
    conn = psycopg2.connect("dbname=news user=postgres"
                            " password=hassan host=localhost")
    cur = conn.cursor()
    cur.execute("select authors.name , count(*) as num_view "
                "from  authors inner join articles "
                "on authors.id=articles.author "
                "inner join log "
                "on log.path like concat('%', articles.slug, '%') "
                "where log.status like '200%'"
                "group by authors.name "
                "order by num_view desc "
                "limit 3")
    rows = cur.fetchall()
    print("2. Who are the most popular article authors of all time?")
    idx = 1
    for row in rows:
        print(idx, ' - ', row[0], ' -> ', row[1])
        idx += 1
    conn.commit()
    cur.close()
    conn.close()


# 12908
def question_third():
    conn = psycopg2.connect("dbname=news user=postgres"
                            " password=hassan host=localhost")
    cur = conn.cursor()

    cur.execute(" create view dataerror as "
                "select substring(cast(log.time as text), 0, 11) as date , count(log.status) as error from log "
                "where log.status like '%404%' "
                "group by date "
                )
    cur.execute(" create view alldata as "
                "select substring(cast(log.time as text), 0, 11) as date , count(log.status) as all from log "
                "group by date "
                )
    cur.execute("create view final_query as select alldata.date, "
                "((dataerror.error / alldata.all::float)*100) as all_error "
                "from alldata inner "
                "join dataerror on "
                "alldata.date=dataerror.date "
                )

    cur.execute(" select date,all_error from final_query where all_error>1;"

                )
    rows = cur.fetchall()
    print("3-On which days did more than 1% of requests lead to errors?")
    idx = 1
    for row in rows:
        print(idx, ' - ', row[0], '->', row[1])
        idx += 1
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    # first query in data base
    print("first Question :")
    question_one()
    print("second Question :")
    question_two()
    print("third Question :")
    question_third()
