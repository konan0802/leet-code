-- https://leetcode.com/problems/second-highest-salary/

-- こっちが自分の回答
SELECT
    salary AS SecondHighestSalary
FROM (
    SELECT
        salary,
        RANK() OVER(ORDER BY salary) AS salary_rank
    FROM Employee
) AS EmployeeRank
WHERE salary_rank = 2

-- こっちが正解
-- 2位が存在しない場合、NULLが返ってくるようになる
SELECT(
    SELECT DISTINCT
        salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary