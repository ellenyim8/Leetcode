-- 1378 - Replace Employee id with the unique identifier
SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI
using (id) 
;

