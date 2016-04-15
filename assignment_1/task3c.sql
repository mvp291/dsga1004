SELECT T.hack_license AS hack_license, COUNT(DISTINCT T.medallion) AS num_taxis_used
FROM trips T
GROUP BY T.hack_license
ORDER BY T.hack_license ASC;