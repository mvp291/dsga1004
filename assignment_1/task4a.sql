SELECT vehicle_type, COUNT(*) AS total_trips, SUM(fares.fare_amount) AS total_revenue, CONCAT(100*AVG(fares.tip_amount / fares.fare_amount), '%') AS avg_tip_percentage
FROM medallions, fares
WHERE medallions.medallion = fares.medallion
GROUP BY vehicle_type
ORDER BY vehicle_type ASC;