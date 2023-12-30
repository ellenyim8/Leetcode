-- 1633 - percentage of users attended a contest 
select contest_id, ROUND(COUNT(user_id) * 100.00 / 
    (select COUNT(*) from Users), 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id
;
