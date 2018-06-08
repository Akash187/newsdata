import psycopg2

DBNAME = "news"

db = psycopg2.connect("dbname={}".format(DBNAME))
c = db.cursor()

"""
        Creating a table of slug and views by extracting slug from log table
        path column using substring function to compare with articles slug
        using join.
        """
c.execute(
    "CREATE VIEW slug_with_views AS SELECT articles.slug AS slug, count(*) AS views FROM log JOIN articles ON articles.slug = substring(log.path,10,100) GROUP BY articles.slug"
)

"""
creating a table of most popular article containing article
author, article title and views by joining table articles and view
slug_with_views on slug.
"""
c.execute(
    "CREATE VIEW most_popular_article AS SELECT articles.author ,articles.title, slug_with_views.views FROM articles JOIN slug_with_views ON articles.slug = slug_with_views.slug ORDER BY views DESC"
)

"""
    the query result in a view views_per_day which contain no. of request on a
    particular date.
    """
c.execute(
    "CREATE VIEW views_per_day AS SELECT substring(text(time),1,10) AS date, count(*) AS views FROM log GROUP BY substring(text(time),1,10)")

"""
the query result in a view error_per_day which contain no. of  request result
in a error on that date.
"""
c.execute(
    "CREATE VIEW error_per_day AS SELECT substring(text(time),1,10) AS date, count(*) AS error FROM log WHERE status != '200 OK' GROUP BY substring(text(time),1,10)"
)

"""
the querry calculate the percentage error on a particular date.
"""
c.execute(
    "CREATE VIEW percent_error_per_day AS SELECT views_per_day.date, round((error_per_day.error*100.0)/views_per_day.views::DECIMAL,2) AS percent_error FROM error_per_day JOIN views_per_day ON error_per_day.date = views_per_day.date"
)
db.close()
