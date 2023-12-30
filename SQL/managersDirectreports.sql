-- 570: Managers with at least 5 direct reports
select m.name from Employee m JOIN 
(
    select e.managerId, count(*) as direct_reports
    from Employee e 
    group by e.managerId
    having count(*) >= 5
) e1 on m.id=e1.managerId
;
