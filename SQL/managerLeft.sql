-- 1978: Employees whose manager left the company
select employee_id from Employees e
where salary<30000 and manager_id is not null and not exists (
    select * from employees f where f.employee_id=e.manager_id
)
order by employee_id
;
