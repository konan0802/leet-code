-- https://leetcode.com/problems/immediate-food-delivery-ii/

WITH CustomerMinOrder AS (
    SELECT
        customer_id,
        MIN(order_date) AS order_date
    FROM Delivery
    GROUP BY customer_id
)
SELECT
    ROUND(COUNT(Delivery.order_date = Delivery.customer_pref_delivery_date OR NULL) / COUNT(*) * 100, 2) AS immediate_percentage
FROM Delivery
JOIN CustomerMinOrder
  ON Delivery.customer_id = CustomerMinOrder.customer_id
 AND Delivery.order_date = CustomerMinOrder.order_date