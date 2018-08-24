#!/usr/bin/env python3
import psycopg2


def main():
    # Q1. What are the most popular three articles of all time?
    articles = get_popular_three_article()
    print("Q1. What are the most popular three articles of all time")
    print("Ans.")
    for (title, view) in articles:
        print("    {} - {} views".format(title, view))
        print("")

    # Q2. Who are the most popular article authors of all time?
    authors = get_popular_three_authors()
    print("Q2. Who are the most popular article authors of all time?")
    print("Ans.")
    for (author, view) in authors:
        print("    {} - {} views".format(author, view))
        print("")
    # Q3. On which days did more than 1% of requests lead to errors?
    all_perc = get_daily_perc()
    print("Q2. On which days did more than 1% of requests lead to errors?")
    print("Ans.")
    for (date, perc) in all_perc:
        print("    {} - {}%".format(date, perc))
        print("")


DBNAME = "news"


def get_popular_three_article():
    """Return  most popular three articles of all time"""
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print("unable to connect database")
    c = db.cursor()
    c.execute("""select title,count(title) from articles,log where 
    slug = substring(path,10) group by title order by 2 desc limit 3""")
    top_three = c.fetchall()
    db.close()
    return top_three


def get_popular_three_authors():
    """Return  most popular three authors of all time"""
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print("unable to connect database")
    c = db.cursor()
    c.execute("""select name,count(name) from articles,log,authors 
    where slug = substring(path,10) and author = authors.id 
    group by name order by 2 desc limit 3;""")
    top_three = c.fetchall()
    db.close()
    return top_three
    
    
def get_daily_perc():
    """Return daily error request rate which is > 1% """
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print("unable to connect database")
    c = db.cursor()
    c.execute(" select * from daily_perc where perc > 1;")
    daily_perc = c.fetchall()
    db.close()
    return daily_perc
    
    
if __name__ == '__main__':
    main()
