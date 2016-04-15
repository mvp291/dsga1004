SELECT T.medallion, T.pickup_datetime
FROM trips AS T
GROUP BY T.medallion, T.pickup_datetime
HAVING COUNT(*) > 1
ORDER BY T.medallion ASC;