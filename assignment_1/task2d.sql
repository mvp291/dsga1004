SELECT DATE(F.pickup_datetime) AS 'day', SUM(F.fare_amount + F.surcharge + F.tip_amount + F.mta_tax + F.tolls_amount) AS total_revenue
FROM fares AS F
GROUP BY DATE(F.pickup_datetime)
ORDER BY DATE(F.pickup_datetime) ASC;