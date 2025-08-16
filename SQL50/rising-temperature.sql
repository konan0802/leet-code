-- https://leetcode.com/problems/rising-temperature/

SELECT TODAY.id
FROM Weather AS TODAY
LEFT JOIN Weather AS YESTERDAY ON TODAY.recordDate = DATE_ADD(YESTERDAY.recordDate, INTERVAL 1 DAY)
ON TODAY.recordDate = DATE_ADD(YESTERDAY.recordDate, INTERVAL 1 DAY)
WHERE TODAY.temperature > YESTERDAY.temperature