import os
import time
from gi.repository import Notify
import commands
def battery():
        try:
                state=commands.getoutput('upower -i /org/freedesktop/UPower/devices/battery_BAT0| grep -E "state"')
                print state

                # Run till battery is fully charged
                full=0
                while(full==0):
                        state=commands.getoutput('upower -i /org/freedesktop/UPower/devices/battery_BAT0| grep -E "state"')
                        print commands.getoutput('clear')
                        print state
                        if(state=='    state:               fully-charged'):
                                full=1
                print "FULLY CHARGED"

                # Reminding every minute when battery is fully charged
                while state=='    state:               fully-charged':
                        Notify.init("BAT FULL")
                        st=Notify.Notification.new("Battery","fully-charged","dialog-information")
                        st.show()
                        state=commands.getoutput('upower -i /org/freedesktop/UPower/devices/battery_BAT0| grep -E "state"')
                        if(state!='    state:               fully-charged'):
                                battery()
                        time.sleep(60)
                      
                # battery() # call itself when the charge is disconnected
        except:
                print "interrupted..Exiting"
battery()
