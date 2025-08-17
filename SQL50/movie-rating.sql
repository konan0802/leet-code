-- https://leetcode.com/problems/movie-rating/

WITH Master AS (
    SELECT
        MovieRating.movie_id,
        Movies.title,
        MovieRating.user_id,
        Users.name,
        MovieRating.rating,
        MovieRating.created_at
    FROM MovieRating
    LEFT JOIN Movies ON MovieRating.movie_id = Movies.movie_id
    LEFT JOIN Users ON MovieRating.user_id = Users.user_id
),
MaxUser AS (
    SELECT
        name,
        COUNT(*) AS cnt
    FROM Master
    GROUP BY name
),
MaxMovie AS (
    SELECT
        title,
        AVG(rating) AS cnt
    FROM Master
    WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
    GROUP BY title
)
(SELECT name AS results FROM MaxUser ORDER BY cnt DESC, name ASC LIMIT 1)
UNION ALL
(SELECT title AS results FROM MaxMovie ORDER BY cnt DESC, title ASC LIMIT 1)