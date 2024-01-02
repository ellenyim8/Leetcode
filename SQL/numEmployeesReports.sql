-- 1731: The number of employees which report to each employee
-- Write your PostgreSQL query statement below
-- avg(age) rounded to nearest int
select e1.employee_id, e1.name, count(distinct e2.employee_id) as reports_count, round(avg(e2.age)) as average_age
from Employees e1
inner join Employees e2
on e1.employee_id=e2.reports_to
group by e1.employee_id, e1.name
order by e1.employee_id
;
