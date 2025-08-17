-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

WITH FollowNum AS (
    SELECT
        requester_id AS id,
        COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY requester_id
),
FollowerNum AS (
    SELECT
        accepter_id AS id,
        COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
)
SELECT
    FollowNum.id,
    FollowNum.num + FollowerNum.num AS num
FROM FollowNum
LEFT JOIN FollowerNum ON FollowNum.id = FollowerNum.id
ORDER BY num DESC
LIMIT 1