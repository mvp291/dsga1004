SELECT agent_name, SUM(fare_amount) AS total_revenue
FROM medallions, fares
WHERE medallions.medallion = fares.medallion
GROUP BY agent_number
ORDER BY total_revenue DESC, agent_name
LIMIT 10;