hours = int(input("Hours : "))
minutes = int(input("Minutes : "))
seconds = int(input("Seconds : "))

total_Time = hours * 3600 + minutes * 60 + seconds
print(f"{hours} H {minutes} min {seconds} s = {total_Time} s")