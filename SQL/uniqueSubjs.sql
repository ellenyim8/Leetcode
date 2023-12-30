-- 2356: Number of unique subjects taught by each teacher
select distinct teacher_id, count(distinct subject_id) as cnt 
from teacher 
group by teacher_id 
;
