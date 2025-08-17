-- https://leetcode.com/problems/department-top-three-salaries/

WITH RankDepartmentEmployeeSalary AS (
    SELECT
        departmentId,
        salary,
        RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM (
        SELECT DISTINCT
            departmentId,
            salary
        FROM Employee
    ) AS UniqueDepartmentEmployeeSalary
)
SELECT
    Department.name AS Department,
    Employee.name AS Employee,
    Employee.salary AS Salary
FROM Employee
LEFT JOIN Department
  ON Employee.departmentId = Department.id
LEFT JOIN RankDepartmentEmployeeSalary
  ON Employee.departmentId = RankDepartmentEmployeeSalary.departmentId
 AND Employee.salary = RankDepartmentEmployeeSalary.salary
WHERE salary_rank <= 3
ORDER BY Department ASC, Salary DESC