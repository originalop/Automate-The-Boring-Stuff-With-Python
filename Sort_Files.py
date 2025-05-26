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

video_extensions = [
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    ".mpeg",
    ".mpg",
    ".3gp",
    ".m4v",
    ".ogv",
    ".mts",
    ".m2ts",
    ".ts",
    ".vob",
    ".f4v",
    ".f4p",
    ".f4a",
    ".f4b",
    ".divx",
    ".xvid",
    ".rm",
    ".rmvb",
    ".asf",
    ".amv",
    ".drc",
    ".bik",
    ".bk2",
    ".mve",
    ".nsv",
    ".yuv",
    ".svi",
    ".ivf",
    ".trp",
    ".dat",
    ".evo",
    ".mk3d",
    ".wtv",
    ".dvr-ms",
    ".ismv",
    ".gxf",
]

src = r"C:\Experiment-Environment"
dest = r"C:\Temp"
counter = 0

# Open log file
with open(os.path.join(dest, "imageLog.txt"), "w") as fo:
    try:
        for ext in imageExt:
            image_files = glob.glob(rf"{src}\**\*{ext}", recursive=True)
            for singleImagePath in image_files:
                file_name = os.path.basename(singleImagePath)
                name, ext = os.path.splitext(file_name)
                dest_path = os.path.join(dest, file_name)
                print(dest_path)
                # Handle duplicate file names
                count = 1
                while os.path.exists(dest_path):
                    new_name = f"{name}_{count}{ext}"
                    dest_path = os.path.join(dest, new_name)
                    count += 1

                shutil.move(singleImagePath, dest_path)
                fo.write(dest_path + "\n")
                print(f"{singleImagePath} moved to {dest_path}")
                counter += 1

        print(f"{counter} items moved.")
        fo.write(f"{counter} items moved")

    except Exception as e:
        print(f"Error: {e}")
