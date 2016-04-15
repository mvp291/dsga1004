SELECT medallion_type AS medallion_type, COUNT(*) AS total_trips, SUM(fares.fare_amount) AS total_revenue, CONCAT(100*AVG(fares.tip_amount / fares.fare_amount), '%') AS avg_tip_percentage
FROM medallions, fares
WHERE medallions.medallion = fares.medallion
GROUP BY medallion_type
ORDER BY medallion_type ASC;