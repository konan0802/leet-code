-- https://leetcode.com/problems/count-salary-categories/

WITH CategoryMaster AS (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary' AS category
    UNION
    SELECT 'High Salary' AS category
),
CategoryAccounts AS (
    SELECT
        account_id,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category
    FROM Accounts
),
CategoryAccountsAgg AS (
    SELECT
        category,
        COUNT(*) AS accounts_count
    FROM CategoryAccounts
    GROUP BY category
)
SELECT
    CategoryMaster.category,
    ifnull(accounts_count, 0) AS accounts_count
FROM CategoryMaster
LEFT JOIN CategoryAccountsAgg
ON CategoryMaster.category = CategoryAccountsAgg.category

-- こっちの方がわかりやすい
select 
    count(case when income > 50000 then 1 end) as high,
    count(case when income between 20000 and 50000 then 1 end) as avg,
    count(case when income < 20000 then 1 end) as low
from accounts