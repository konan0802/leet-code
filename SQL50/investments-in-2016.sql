-- https://leetcode.com/problems/investments-in-2016/

WITH SameTiv2015 AS (
    SELECT
        tiv_2015,
        COUNT(*) AS cnt
    FROM Insurance
    GROUP BY tiv_2015
    HAVING cnt >= 2
),
UniqueCity AS (
    SELECT
        CONCAT(lat, lon) AS latlon,
        COUNT(*) AS cnt
    FROM Insurance
    GROUP BY latlon
    HAVING cnt = 1
)
SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT
        tiv_2015,
        tiv_2016,
        CONCAT(lat, lon) AS latlon
    FROM Insurance
) AS FormatInsurance
JOIN SameTiv2015 ON FormatInsurance.tiv_2015 = SameTiv2015.tiv_2015
JOIN UniqueCity ON FormatInsurance.latlon = UniqueCity.latlon
