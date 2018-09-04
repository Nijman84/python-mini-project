# Do something while the time is in a certain window
from __future__ import print_function
import time

if (time.strftime("%H:%M:%S")) > (time.strftime("14:00:00")):
    print("Outside of acceptable trigger window. " +
          "Must be triggeed before 14:00"
          )
    exit(1)
else:
    print("Within acceptable time bounds. Continuing.")

while (time.strftime("%H:%M:%S")) < (time.strftime("08:00:00")):
    print("The current time is:", time.strftime("%H:%M:%S") +
          " - too early to trigger")
    time.sleep(10)

print("Ready to trigger now the time is:", time.strftime("%H:%M:%S"))

print("    _(_)(_)(_)(_)_      _(_)_     (_)          (_) _(_)(_)(_)(_)_   ")
print("   (_)          (_)   _(_) (_)_   (_)          (_)(_)          (_)  ")
print("   (_)_  _  _  _    _(_)     (_)_ (_)          (_)(_)_  _  _  _     ")
print("     (_)(_)(_)(_)_ (_) _  _  _ (_)(_)          (_)  (_)(_)(_)(_)_   ")
print("    _           (_)(_)(_)(_)(_)(_)(_)          (_) _           (_)  ")
print("   (_)_  _  _  _(_)(_)         (_)(_)_  _  _  _(_)(_)_  _  _  _(_)  ")
print("     (_)(_)(_)(_)  (_)         (_)  (_)(_)(_)(_)    (_)(_)(_)(_)    ")
