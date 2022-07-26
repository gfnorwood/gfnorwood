# Author: @gfnorwood
# Purpose: The purpose of this method is to extend a logging utility to capture activity.  
# Import Statements

import io
import time
from datetime import datetime
from datetime import time

# Global Variables

now = datetime.now()

# Functions

def LogActivity(activity):
    
    now = datetime.now()
    
    with open("log.txt", "a") as file:
        file.write(str(now) + " " + activity +"\n")

    print(str(now) + " " + activity)
 

LogActivity("Start Procedure")
LogActivity("Do some cool things")
LogActivity("End Procedure")
