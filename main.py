from datetime import datetime, timedelta
import time

current_time = datetime.now()
target_date = datetime(2016, 9, 12, 15, 25, 0, 0)

time_left = str(target_date - current_time)

hours = time_left[0]
minutes = time_left[2:4]
seconds = time_left[5:7]

print hours + " hours " + minutes + " minutes and " + seconds + " seconds until you may leave."

def convert_to_seconds(hours, minutes, seconds):
	total_seconds = int(hours) * 60 * 60
	total_seconds += int(minutes) * 60
	total_seconds += int(seconds)

	return total_seconds

total_seconds = convert_to_seconds(hours, minutes,seconds)
	
for second in range(total_seconds):
	print str(total_seconds - second) + " seconds are left in your work day."
	time.sleep(1)
