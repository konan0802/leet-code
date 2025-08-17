-- https://leetcode.com/problems/restaurant-growth/

WITH CustomerAgg AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
Agg AS (
    SELECT
        visited_on,
        RANK() OVER (ORDER BY visited_on) AS rank_num,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount
    FROM CustomerAgg
)
SELECT
    visited_on,
    amount,
    ROUND(average_amount, 2) AS average_amount
FROM Agg
WHERE rank_num >= 7