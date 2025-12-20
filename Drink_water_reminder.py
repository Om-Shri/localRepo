## Drink water reminder
## ALL OPERATING SYSTEM.
import time
from plyer import notification
while True:
    notification.notify(
        title="Reminder",
        message="Drink one glass of water.You are dehydrated.",
    )
    time.sleep(3600)

## ONLY FOR WINDOWS.BUT THIS IS PROPERLY WORK IN VERSON 3.10 3.11 OR LOWER VERSONS.

from win10toast import ToastNotifier

toast = ToastNotifier()

while True:
    toast.show_toast(
        "Water Reminder",
        "Drink one glass of water",
        duration=5
    )
    time .sleep(3600)