-- https://leetcode.com/problems/exchange-seats/

WITH BeforeStudent AS (
    SELECT
        id,
        student,
        LAG(student) OVER (ORDER BY id ROWS 1 PRECEDING) AS before_student,
        LEAD(student) OVER (ORDER BY id ROWS 1 PRECEDING) AS after_student
    FROM Seat
)
SELECT
    id,
    CASE
        WHEN id%2 = 1 THEN ifnull(after_student, student)
        ELSE ifnull(before_student, student)
    END AS student
FROM BeforeStudent