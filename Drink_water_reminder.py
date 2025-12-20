## Drink water reminder
##  WINDOWS SYSTEM.
import time
from plyer import notification
sedule = input("Enter hours for notification (1,2,3,4...) :")

hours = int(sedule)*3600

while True:
    notification.notify(
        title="Reminder",
        message="Drink one glass of water.You are dehydrated.",
    )
    time.sleep(hours)
    # for i in range(hours):
    #     print(i)
    #     time.sleep(1)
