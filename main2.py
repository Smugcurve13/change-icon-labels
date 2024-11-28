import os

# Define the desktop path
desktop_path = os.path.expanduser("~/Desktop")

# Invisible Unicode characters for renaming
invisible_names = [
    "\u200B", "\u200C", "\u200D", "\u2060", "\u2062", "\u2063",
    "\u3164", "\uFFA0", "\uFEFF", "\u00A0", "\u2800"
]

# Initial mappings: icon names -> invisible Unicode names
icon_renames = {
    "Dragon Ball FighterZ": invisible_names[5],
    "Yakuza Like a Dragon": invisible_names[1] + "\u2060",
    "Wuthering Waves": invisible_names[4] + "\u2063",
}

# Function to rename files
def rename_icon(file_path, new_name):
    # Generate new file path
    directory, old_name = os.path.split(file_path)
    base, extension = os.path.splitext(old_name)
    new_path = os.path.join(directory, new_name + extension)

    try:
        os.rename(file_path, new_path)
        print(f'Renamed "{old_name}" to "{new_name}{extension}"')
    except FileExistsError:
        print(f'Failed to rename "{old_name}": File with the name "{new_name}{extension}" already exists.')
    except Exception as e:
        print(f'Failed to rename "{old_name}": {e}')

# Function to check if a name is already invisible
def is_invisible(name):
    return all(char in invisible_names for char in name)

# Iterate through files on the desktop and rename as needed
for filename in os.listdir(desktop_path):
    # Skip non-shortcut files and `.url` files
    if not filename.endswith(".lnk"):
        continue

    # Extract the base name without extension
    base_name, extension = os.path.splitext(filename)

    # Skip files that are already renamed with invisible labels
    if is_invisible(base_name):
        print(f'Skipping "{base_name}{extension}" (already renamed).')
        continue

    # If the name is in the dictionary, rename it
    if base_name in icon_renames:
        old_path = os.path.join(desktop_path, filename)
        new_name = icon_renames[base_name]
        rename_icon(old_path, new_name)

print("Renaming completed!")
