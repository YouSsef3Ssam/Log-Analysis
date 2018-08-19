#!/usr/bin/env python3

import psycopg2


def getReady(query):
    try:
        db = psycopg2.connect(dbname="LogAnalysis", user="postgres")
        c = db.cursor()
        c.execute(query)
        data = c.fetchall()
        db.close()
        return data
    except:
        print ("Unable to connect to the database")


def popularArticles():
    query = '''select views_count.title,views_count.view from
    views_count limit 3'''
    result = getReady(query)
    i = 1
    print("1) What are the most popular three articles of all time? \n")
    for title, views in result:
        print("Article " + str(i) + ": "+title+" — " + str(views)+"Views. \n")
        i = i + 1


def popularAuthors():
    query = ''' select authors.name, sum(views_count.view) as views
            from views_count, authors
            where views_count.author = authors.id
            group by authors.name
            order by views desc 10'''
    result = getReady(query)
    print("2) Who are the most popular article authors of all time? \n")
    i = 1
    for name, views in result:
        print("Author " + str(i) + ":  "+name+" — " + str(views) + "Views. \n")
        i = i + 1


def requestError():
    query = ''' select date, errorRatio from error_ratio
    where errorRatio > 1 '''
    result = getReady(query)
    print("3) On which days did more than 1% of requests lead to errors? \n")
    i = 1
    for date, ratio in result:
        print(str(i) + ": " + date + " — " + str(ratio) + "% errors \n")
        i = i + 1
popularArticles()
popularAuthors()
requestError()
