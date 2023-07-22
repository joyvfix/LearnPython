# import psutil
# from pynotifier import Notification

# battery = psutil.sensors_battery()
# plugged = battery.power_plugged
# percent = battery.percent

# if percent <= 30 and plugged != True:
#     Notification(
#         title="Battery Low",
#         description=str(percent) + "% Battery remain!!",
#         duration=5,  # Duration in seconds

#     ).send()
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
# import psutil
# from pynotifier import Notification

# battery = psutil.sensors_battery()
# plugged = battery.power_plugged
# percent = battery.percent

# if percent < 60 and not plugged:
#     Notification(
#         title="Battery Low",
#         description=str(percent) + "% Battery remaining!",
#         duration=5  # Duration in seconds
#     ).send()
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged:
    status = "Plugged in"
else:
    status = "Not plugged in"

print(f"Battery status: {status}")
print(f"Battery percentage: {percent}%")
