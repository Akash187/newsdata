#! /usr/local/lib python3
import psycopg2

DBNAME = "news"


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Problem connecting to database.")


def most_popular_three_articles():
    db, c = connect()
    print("Q1. What are the most popular three articles of all time?")
    """
    querrying top three most popular article.
    """
    c.execute("select title, views from most_popular_article limit 3")
    most_popular_three_articles = c.fetchall()
    for row in most_popular_three_articles:
        print(str(row[0]) + " --> " + str(row[1]) + "views")
    db.close()


def most_popular_article_author():
    db, c = connect()
    print("Q2. Who are the most popular article authors of all time?")
    """
    using view most_popular_article to query most popular author and
    there views by joining authors table.
    """
    c.execute(
        "select authors.name, sum(most_popular_article.views) as views"
        " from authors join most_popular_article on"
        " authors.id = most_popular_article.author"
        " GROUP BY name ORDER BY views desc")
    popular_article_author = c.fetchall()
    for row in popular_article_author:
        print(str(row[0]) + " --> " + str(row[1]) + "views")
    db.close()


def percent_error():
    db, c = connect()
    print("Q3. On which days did more than 1% of requests lead to errors?")
    """
    the query return table with two column date and percent_error where
    percent_error is more than 1%
    """
    c.execute("select date, percent_error from percent_error_per_day"
              " where percent_error > 1.00")
    percent_error = c.fetchall()
    for row in percent_error:
        print(str(row[0]) + " --> " + str(row[1]) + "% errors")
    db.close()


if __name__ == '__main__':
    most_popular_three_articles()
    print("")
    most_popular_article_author()
    print("")
    percent_error()
