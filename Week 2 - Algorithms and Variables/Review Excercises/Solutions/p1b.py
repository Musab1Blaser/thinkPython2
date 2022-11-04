dist_in_km = 10
time_in_minutes = 42
time_in_seconds = 42

km_per_mile = 1.61
miles = dist_in_km / km_per_mile

total_time_in_seconds = 60 * time_in_minutes + time_in_seconds
time_in_hours = total_time_in_seconds/3600

speed = miles/time_in_hours
speed = round(speed)

print(speed)