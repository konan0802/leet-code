-- https://leetcode.com/problems/customers-who-bought-all-products/

WITH ProductNum AS (
    SELECT
        COUNT(*) AS cnt
    FROM Product
),
CustomerNum AS (
    SELECT
        customer_id,
        COUNT(*) AS cnt
    FROM (
        SELECT DISTINCT
            customer_id,
            product_key
        FROM Customer
    ) AS DisCustomer
    GROUP BY customer_id
)
SELECT customer_id
FROM CustomerNum
CROSS JOIN ProductNum
WHERE CustomerNum.cnt = ProductNum.cnt

-- こっちの方がわかりやすい
select customer_id
from (
    select
        customer_id,
        count(distinct product_key) as cnt
    from Customer
    group by customer_id
) t
where cnt = (select count(*) from Product);