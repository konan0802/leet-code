-- https://leetcode.com/problems/product-sales-analysis-iii/

WITH FirstYear AS (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)
SELECT
    Sales.product_id,
    Sales.year AS first_year,
    Sales.quantity,
    Sales.price
FROM Sales
JOIN FirstYear
  ON Sales.product_id = FirstYear.product_id
 AND Sales.year = FirstYear.first_yearGROUP BY Sales.product_id;

-- こっちの方が適切
WITH FirstYear AS (
    SELECT
        product_id,
        year,
        quantity,
        price ,
        Rank() OVER(PARTITION BY PRODUCT_ID ORDER BY YEAR ASC ) AS First_year
    FROM SALES 
)
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM FirstYear
WHERE First_year = 1;