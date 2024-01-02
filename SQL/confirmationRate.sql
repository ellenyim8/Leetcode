--1934: Confirmation rate
select s.user_id,
        ifnull(round(coalesce(confirmed_cnt, 0) / nullif(total_requests, 0), 2), 0) as confirmation_rate
from Signups s
left join
(select c.user_id, 
        count(case when action='confirmed' then 1 end) as confirmed_cnt,
        count(*) as total_requests
from Confirmations c
group by c.user_id 
)
c on s.user_id=c.user_id
;
