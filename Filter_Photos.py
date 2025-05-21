import glob

all_python_files = glob.glob(r"E:\PHOTOS\**\*.jpg", recursive=True)
for i in all_python_files:
    print(i)
# Explanation:
# 1. import glob
# This imports the glob module, which is used to find all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.

# 2. glob.glob("**/*.py", recursive=True)
# glob.glob() searches for files matching a pattern.

# "**/*.py" means:

# **/ looks through all directories and subdirectories (recursively).

# *.py matches all files ending with .py (Python files).

# recursive=True tells glob to search recursively through subdirectories, not just the current directory.

# So, all_python_files will be a list of all .py files found anywhere under the current directory, including all nested folders.

# 3. for i in all_python_files:
# This loops through each file path in the list of .py files found.

# 4. print(i)
# This prints the path of each .py file found.