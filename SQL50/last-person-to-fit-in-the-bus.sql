-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/

WITH BoardBus AS (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn) AS total
    FROM Queue
)
SELECT person_name
FROM BoardBus
WHERE total <= 1000
ORDER BY total DESC
LIMIT 1