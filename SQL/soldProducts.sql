--1484: Group sold products by the date
select sell_date, count(distinct product) as num_sold, group_concat(distinct product order by product asc separator ',' ) as products 
from activities 
group by sell_date
;