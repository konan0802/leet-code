-- https://leetcode.com/problems/game-play-analysis-iv/

WITH FirstLogin AS (
    SELECT
        player_id,
        MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)
SELECT
    ROUND(COUNT(FirstLogin.first_date IS NOT NULL OR NULL) / COUNT(DISTINCT Activity.player_id), 2) AS fraction
FROM Activity
LEFT JOIN FirstLogin
  ON Activity.player_id = FirstLogin.player_id
 AND Activity.event_date = DATE_ADD(FirstLogin.first_date, INTERVAL 1 DAY)