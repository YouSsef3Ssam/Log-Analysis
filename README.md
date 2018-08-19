# Log Analysis

## What is that?

* create a reporting tool that prints out reports based on the data in the database.
* This reporting tool is a Python program using the psycopg2 module to connect to the database.

## What you need

To Start First you need download and install

1. <a href="https://www.python.org/downloads" target="_blank"> **Python 3** </a>
2. <a href="https://www.vagrantup.com" target="_blank"> **Vagrant** </a>
3. <a href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1" target="_blank"> **VirtualBox** </a>
4. <a href="https://www.postgresql.org/download/windows/" target="_blank"> **Postgresql Database** </a>

## How to run
1. You need to download <a href="https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip" target="_blank">FSND-Virtual-Machine.zip</a>

2. You need to Download newsdata.sql from <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip" target = "_blank">Here</a>

3. unzip FSND-Virtual-Machine and open it inside the vagrant subdirectory run this commands
```
$ vagrant up
$ vagrant ssh
```
4. Inside the vagrant folder copy newsdata.sql then run this command
```
$ psql -d news -f newsdata.sql

```
5. Run This command to connect newsdata database
```
$ psql -d news
```
## The database includes three tables:

1. The authors table includes information about the authors of articles.
2. The articles table includes the articles themselves.
3. The log table includes one entry for each time a user has accessed the site.

## Then Create the following two views

### views_count
```
create view views_count as
select title, author, count(*) as view
from articles join log
on log.path=CONCAT('/article/',articles.slug)
group by articles.title, articles.author
order by view desc;
```

### error_ratio
```
create view error_ratio as
select to_char(date(time), 'Mon DD, YYYY') as date, round(100.0 * sum (case log.status when '200 OK' then 0 else 1 end) / count(log.status), 1 ) as errorRatio
from log
group by date(time)
order by errorRatio desc;
```

## finally
Run logAnalysis.py
```
$ python3 logAnalysis.py

```

## Contact Me

* **Youssef Essam**
* Egypt, Cairo
* <a href="https://www.facebook.com/yossef.essam.1213" target="_blank">Facebook</a>
* <a href="mailto:youssef.3ssam1@gmail.com" target="_blank">Gmail</a>
* +201116008332
