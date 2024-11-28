import os

# Define a set of invisible Unicode characters for the new icon labels
# (Each character is different to ensure no conflicts)
invisible_names = [
    "\u200B", "\u200C", "\u200D", "\u2060", "\u2061", "\u2062", "\u2063", 
    "\uFEFF", "\u180E", "\u3164", "\uFFA0", "\u1D159"
]

# Mapping of current names (without ".url") to new invisible Unicode names
icon_renames = {
    "division2": invisible_names[0],
    "fortnite": invisible_names[1],
    "Grand Theft Auto V": invisible_names[2],
    "DRAGON BALL": invisible_names[3],
    "Need for Speed": invisible_names[4],
    "Dragon Ball FighterZ": invisible_names[5],
    "Fall Guys": invisible_names[6],
    "Rocket League": invisible_names[7],
    "Brawlhalla": invisible_names[8],
    "helldiver": invisible_names[9],
    "dbx": invisible_names[10],
    "Yakuza Like a Dragon": invisible_names[11],
}

# Get the path to the desktop
desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")

# Process each file on the desktop
for file_name in os.listdir(desktop_path):
    # Check if the file is a URL shortcut (.url file)
    if file_name.endswith(".url"):
        # Extract the base name without the ".url" extension
        base_name = file_name[:-4]
        # Check if the base name exists in the mapping
        if base_name in icon_renames:
            # Get the new name (invisible Unicode) from the mapping
            new_name = icon_renames[base_name] + ".url"
            # Rename the file
            old_path = os.path.join(desktop_path, file_name)
            new_path = os.path.join(desktop_path, new_name)
            try:
                os.rename(old_path, new_path)
                print(f'Renamed "{file_name}" to "{new_name}"')
            except Exception as e:
                print(f'Error renaming "{file_name}": {e}')

print("Renaming process completed.")
