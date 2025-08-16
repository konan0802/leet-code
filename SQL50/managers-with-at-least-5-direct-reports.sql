-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

WITH directs AS (
    SELECT
        managerId,
        COUNT(*) AS cnt
    FROM Employee
    GROUP BY managerId
)
SELECT name
FROM directs
JOIN Employee ON directs.managerId = Employee.id
WHERE cnt >= 5