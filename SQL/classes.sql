--596: Classes more than 5 students
SELECT CLASS FROM COURSES 
GROUP BY CLASS 
HAVING COUNT(DISTINCT STUDENT) >= 5
; 
