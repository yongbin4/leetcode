# Write your MySQL query statement below
SELECT IFNULL(euni.unique_id, NULL) AS unique_id,e.name
FROM Employees e
LEFT JOIN EmployeeUNI euni on e.id = euni.id
ORDER BY e.id;