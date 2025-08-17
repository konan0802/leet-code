-- https://leetcode.com/problems/consecutive-numbers/

SELECT DISTINCT 
    num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num) OVER (ORDER BY id) AS before_num,
        LEAD(num) OVER (ORDER BY id) AS after_num
    FROM Logs
)AS AA
WHERE num = before_num
  AND num = after_num
;