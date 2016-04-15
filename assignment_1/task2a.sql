
SELECT F.fare_amount AS amount, count(*) AS num_trips
FROM fares AS F
GROUP BY F.fare_amount
ORDER BY F.fare_amount ASC;
