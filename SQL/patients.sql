--1527: Patients with a condition
SELECT * FROM PATIENTS
WHERE CONDITIONS LIKE 'DIAB1%' OR CONDITIONS LIKE '% DIAB1%'
;
