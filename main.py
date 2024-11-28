import os

# Define the directory containing the desktop icons
desktop_path = os.path.expanduser("~/Desktop")

# Invisible Unicode characters for renaming
invisible_names = [
    "\u200B\u200B", "\u200C\u200C", "\u200D\u200D", "\u2060\u2060",
    "\u2062\u2062", "\u2063\u2063", "\u2064\u2064", "\u3164\u3164",
    "\uFFA0\uFFA0", "\uFEFF\uFEFF", "\u00A0\u00A0", "\u2800\u2800"
]

# Define mappings: original icon names -> Unicode invisible names
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
    "yakuza gaiden": invisible_names[0] + "\u200C",  # Ensures unique name
    "Palworld": invisible_names[1] + "\u200D",       # Ensures unique name
    "Wuthering Waves": invisible_names[2] + "\u2060",  # Ensures unique name
    "Brotato": invisible_names[3] + "\u2062",       # Ensures unique name
}

# Iterate through files on the desktop and rename based on the dictionary
for filename in os.listdir(desktop_path):
    # Skip non-shortcut files
    if not filename.endswith(".lnk") and not filename.endswith(".url"):
        continue

    # Extract the base name without extension
    base_name, extension = os.path.splitext(filename)

    # If the name is in the dictionary, rename it
    if base_name in icon_renames:
        new_name = icon_renames[base_name] + extension
        old_path = os.path.join(desktop_path, filename)
        new_path = os.path.join(desktop_path, new_name)

        try:
            os.rename(old_path, new_path)
            print(f'Renamed "{filename}" to "{new_name}"')
        except FileExistsError:
            print(f'Failed to rename "{filename}": File with the name "{new_name}" already exists.')
        except Exception as e:
            print(f'Failed to rename "{filename}": {e}')

print("Renaming completed!")
