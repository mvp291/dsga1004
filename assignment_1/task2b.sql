SELECT count(*) AS num_trips
FROM fares AS F
WHERE F.total_amount < 10;