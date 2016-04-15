SELECT T.medallion, COUNT(*) AS num_trips
FROM trips AS T
GROUP BY T.medallion
ORDER BY T.medallion ASC;