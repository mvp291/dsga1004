SELECT T.medallion, CONCAT(100 * (SUM(CASE WHEN T.pickup_latitude = 0 AND T.pickup_longitude = 0 AND T.dropoff_latitude = 0 AND T.dropoff_longitude = 0 THEN 1 ELSE 0 END) / COUNT(*)), '%') as percentage_of_trips
FROM trips T
GROUP BY T.medallion
ORDER BY T.medallion ASC;