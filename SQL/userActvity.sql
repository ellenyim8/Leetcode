-- 1141: User Activity for the past 30 days I
select activity_date as day, count(distinct(user_id)) as active_users
from Activity
where activity_date between '2019-06-28' and '2019-07-27'
group by day
;