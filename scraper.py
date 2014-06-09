SQLITE - selecionar entre horas

select 
    TT,
    hora
from bbb
WHERE hora BETWEEN "2014-06-03 08:57:41 PM" AND "2014-06-04 06:19:58 PM"


select 
TT,
hora
from bbb
WHERE "hora" > date ('now', 'start of day', '-24 hours')

TT G2

select
"hashtag_trend",
sum("retweet_count") as "total RT"
from "aaa"
group by "hashtag_trend"
order by "total RT" desc
