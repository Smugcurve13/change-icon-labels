import os


# Mapping of current names (without ".url") to new desired names
icon_renames = {
    "division2": "2",
    "fortnite": "fortnite",
    "Grand Theft Auto V": "Grand Theft Auto V",
    "DRAGON BALL": "DRAGON BALL",
    "Need for Speed": "Need for Speed",
    "Dragon Ball FighterZ": "Dragon Ball FighterZ",
    "Fall Guys": "Fall Guys",
    "Rocket League": "Rocket League",
    "Brawlhalla": "Brawlhalla",
    "helldiver": "helldiver",
    "dbx": "dbx",
    "Yakuza Like a Dragon": "Yakuza Like a Dragon",
    "yakuza gaiden": "yakuza gaiden",
    "Palworld": "Palworld",
    "Wuthering Waves": "Wuthering Waves",
    "Brota": "Brota"
}

# Get the path to the desktop
desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")

for file_name in os.listdir(desktop_path):
    if file_name.endswith(".url"):
        print(file_name)

# Process each file on the desktop
for file_name in os.listdir(desktop_path):
    # Check if the file is a shortcut (.url file)
    if file_name.endswith(".url"):
        # Extract the base name without the ".url" extension
        base_name = file_name[:-4]
        # Check if the base name exists in the mapping
        if base_name in icon_renames:
            # Get the new name from the mapping
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
