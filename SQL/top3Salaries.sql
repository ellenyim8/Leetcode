-- 185: Department Top 3 Salaries
select d.name as Department, e.name as Employee, salary as Salary
from Department d right join Employee e
on d.id=e.departmentId
where
(
    select count(distinct Salary) from Employee e1
    where e1.departmentId=d.id and e1.salary >= e.salary ) <= 3
and d.name is not null
order by d.id desc
;
