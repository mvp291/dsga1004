SELECT T.passenger_count AS number_of_passengers, count(*) AS num_trips
FROM trips as T
GROUP BY T.passenger_count
ORDER BY T.passenger_count ASC;