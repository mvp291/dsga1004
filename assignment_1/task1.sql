CREATE VIEW alltrips AS
(SELECT  T.medallion, T.hack_license, T.vendor_id, T.pickup_datetime, T.rate_code, T.store_and_fwd_flag, T.dropoff_datetime,
T.passenger_count, T.trip_time_in_secs, T.trip_distance, T.pickup_longitude, T.pickup_latitude, T.dropoff_longitude,
T.dropoff_latitude, F.payment_type, F.fare_amount, F.surcharge, F.mta_tax, F.tip_amount, F.tolls_amount, F.total_amount
FROM fares F, trips T
WHERE F.medallion = T.medallion AND F.hack_license = T.hack_license AND F.vendor_id = T.vendor_id AND F.pickup_datetime = T.pickup_datetime
ORDER BY T.medallion, T.hack_license, T.vendor_id, T.pickup_datetime, T.pickup_longitude ASC);

select * from alltrips;