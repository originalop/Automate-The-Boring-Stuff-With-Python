# This code would sort every photos in a specified directory.
> This would be helpful if you have 999999999 photos, 9999 videos and other file mixed; And you you want to sort into photos into photos folder and videos into videos folder. Videos section not yet added, will be soon.

```
import glob
import shutil
import os

imageExt = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp",
    ".heic",
    ".heif",
    ".avif",
    ".raw",
    ".psd",
    ".xcf",
    ".dds",
    ".ico",
]

src = r"C:\Experiment-Environment"
dest = r"C:\Experiment-Environment\Python_Exp"
counter = 0

# Open log file
with open(os.path.join(dest, "Log.txt"), "w") as fo:
    try:
        for ext in imageExt:
            image_files = glob.glob(rf"{src}\**\*{ext}", recursive=True)
            for file_path in image_files:
                file_name = os.path.basename(file_path)
                name, ext = os.path.splitext(file_name)
                dest_path = os.path.join(dest, file_name)

                # Handle duplicate file names
                count = 1
                while os.path.exists(dest_path):
                    new_name = f"{name}_{count}{ext}"
                    dest_path = os.path.join(dest, new_name)
                    count += 1

                shutil.move(file_path, dest_path)
                fo.write(dest_path + "\n")
                print(f"{file_path} moved to {dest_path}")
                counter += 1

        print(f"{counter} items moved.")
        fo.write(f"{counter} items moved")

    except Exception as e:
        print(f"Error: {e}")
```