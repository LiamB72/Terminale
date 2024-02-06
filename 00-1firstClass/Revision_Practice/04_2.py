hours = int(input("Hours : "))
minutes = int(input("Minutes : "))
seconds = int(input("Seconds : "))

if hours < 0 or minutes < 0 or seconds < 0:
    print(f"{hours} H {minutes} min {seconds} s is not a valid time.")
else:
    total_Time = hours * 3600 + minutes * 60 + seconds
    print(f"{hours} H {minutes} min {seconds} s = {total_Time} s")