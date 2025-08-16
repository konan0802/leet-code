-- https://leetcode.com/problems/confirmation-rate/

WITH ConfRate AS (
    SELECT
        user_id,
        ROUND(COUNT(action = 'confirmed' OR NULL) / COUNT(*), 2) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id
)
SELECT
    Signups.user_id,
    ifnull(confirmation_rate, 0) AS confirmation_rate
FROM Signups
LEFT JOIN ConfRate ON Signups.user_id = ConfRate.user_id