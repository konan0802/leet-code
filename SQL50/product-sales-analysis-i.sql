-- https://leetcode.com/problems/product-sales-analysis-i/

SELECT product_name, year, price
FROM Sales
LEFT JOIN Product
ON Sales.product_id = Product.product_id