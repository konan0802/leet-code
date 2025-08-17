-- https://leetcode.com/problems/product-price-at-a-given-date/

WITH UniqueProducts AS (
    SELECT DISTINCT
        product_id
    FROM Products
),
LatestPrice AS (
    SELECT
        product_id,
        new_price,
        RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS latest_change
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT
    UniqueProducts.product_id,
    ifnull(LatestPrice.new_price, 10) AS price
FROM UniqueProducts
LEFT JOIN LatestPrice
ON UniqueProducts.product_id = LatestPrice.product_id
WHERE LatestPrice.new_price IS NULL OR LatestPrice.latest_change = 1