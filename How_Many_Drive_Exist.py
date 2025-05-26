from pathlib import Path
import string
import os

with open("Drive_Log.txt","w") as f:
    for i in string.ascii_uppercase:
        drive=Path(rf"{i}:\\")
        if (drive.exists()):
            f.write(f"{i} exists.\n")
print("Drive list has been written.")