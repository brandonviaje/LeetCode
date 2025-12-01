-- Write your PostgreSQL query statement below-- 

-- wanna find all employees that earn more than their manager --

-- managers will have a null managerID, if its null then they are an employee --
-- want to query where managerId isn't null (means they have a manger), check if the managerId = employee id and check if the the employees salary is greater than their manager

--- maybe a self join? --
SELECT e1.name AS Employee
FROM Employee e1, Employee e2
WHERE(e1.managerId IS NOT NULL AND e1.managerId = e2.id AND e1.salary > e2.salary);