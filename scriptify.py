

import subprocess
import random
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime.strptime("2023-1-1 5:23:45", "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime("2023-3-29 9:13:50", "%Y-%m-%d %H:%M:%S")

# Define the list of random numbers
num_commits = [5,5,5,12,0,0,1,2,3,7, 4, 10, 3,0,0,0,0,0 ,6, 8, 4, 3 , 9, 13 , 13, 24]

# Open the stats file for writing
with open("stats2.txt", "w") as f:
    # Loop through all dates between start_date and end_date
    delta = timedelta(days=1)
    while start_date <= end_date:
        # Choose a random number from the list
        num = random.choice(num_commits)

        # Write the date and num to the stats file
        date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{date_str}: {num}\n") 
        # printing the date and num to the console
        print(f"{date_str}: {num}")

        # Run the Bash script multiple times with the current date
        for i in range(num):
            # Format the date in the required format
            date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
            commit_msg = f"Commit {i} on {date_str}"
            # Call the Bash script with the date argument
            subprocess.call(["./bash_Script.sh", date_str, commit_msg])

        # Increment the date
        start_date += delta