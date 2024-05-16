import os

def list_files(directory):
    files = os.listdir(directory)
    return files

# Directory path to the "Images" directory
images_directory = "/storage/emulated/0/Images/"  # Adjust the path as needed

file_scores = [ 100, 45, 76, 14, 66]
file_list = []
# List all files in the "Images" directory
image_files = list_files(images_directory)
print("Files in the 'Images' directory:")
for file_name in image_files:
    file_list.append(file_name)

print(file_list)

file_marked = dict( zip(file_list, file_scores))

print (" so these are the script and their marks")
print(file_marked)
name = "seyh"


















