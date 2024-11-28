import os

# Mapping of new names for your desktop icons
icon_names = {
    "division2": "-",
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
    "Brotato": "Brotato"
}

# Path to the desktop
desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")

# Rename the icons on the desktop
for file_name in os.listdir(desktop_path):
    # Check if the file is a shortcut (.lnk file)
    if file_name.endswith(".lnk"):
        # Remove the ".lnk" extension to get the base name
        base_name = file_name[:-4]
        # Check if this icon matches one of the keys in our dictionary
        if base_name in icon_names:
            # Construct the new file name
            new_name = icon_names[base_name] + ".lnk"
            # Rename the file
            old_path = os.path.join(desktop_path, file_name)
            new_path = os.path.join(desktop_path, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed "{file_name}" to "{new_name}"')

print("Renaming completed.")
