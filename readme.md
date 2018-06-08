# Logs Analysis Project

A python script that will use information from the database to discover what kind of articles the site's readers like.

## Requirements

In order to run this program you will need the following:

1. Virtual machine with vagrant
2. Download the required vagrant file from "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile"
3. Python2 or python3
4. python library psycopg2
5. Download the data from "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"

## Instructions

Start virtual machine
(i). Go to vagrant directory of you device on bash shell.
(ii). Then run vagrant up.
(iii). Finally run vagrant ssh.

2. Change directory to the project containing file in vagrant directory.
3. load the data and start postgresql using command "psql -d news -f newsdata.sql"
4. On another bash shell go to the file directory as previously leaving first bash shell open run the python file "news.py".
4. Enjoy!

## View Info

The database querry contain view to avoid writting too many sql querry in a single statement.

1. slug_with_views :- the view contain two column one is 'slug' and other is no. of 'views'. 
2. most_popular_article :- the view contain three column one is 'author' which contain author id other is 'title' of article and last is its 'views'.
3. views_per_day :- the view contain two column one is 'date' and other is number of request that day as 'views'.
4. error_per_day :- the view contain two column one is 'date' and other is 'error' which contain total no of error in request.
5. percent_error_per_day :- the view contain two row one is 'date' and other is 'percent_error' which contain percent of request lead to error that day. 