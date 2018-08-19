

create view views_count as
(select title, author, count(*) as view
from articles join log
on log.path=CONCAT('/article/',articles.slug)
group by articles.title, articles.author
order by view desc);

create view error_ratio as
select to_char(date(time), 'Mon DD, YYYY') as date, round(100.0 * sum (case log.status when '200 OK' then 0 else 1 end) / count(log.status), 1 ) as errorRatio
from log
group by date(time)
order by errorRatio desc;