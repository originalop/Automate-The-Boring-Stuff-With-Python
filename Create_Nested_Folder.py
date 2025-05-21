import os
from pathlib import Path
path=Path(r"E:\RAW-DATA")
newFolder=Path(r"A\B\C\D\E\F\G\H\I\J\K\L\M\N\O\P\Q\R\S\T\U\V\W\X\Y\Z")
os.makedirs(path/newFolder) # `/` operator concate path for Path object, not for string.
print(f"{newFolder} created!")