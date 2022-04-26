import random

TheModes = {
    "Ionian": ["I", "ii", "iii", "IV", "V", "vi", "vio"],
    "Mixolydian": ["I", "ii", "iii", "IV", "vm", "vi", "bVII"],
    "Lydian": ["I", "II", "iii", "#ivdim", "V", "vi", "vii"],
    "Dorian": ["i", "ii", "bIII", "IV", "vm", "vidim", "bVII"],
    "Aeolian": ["i", "iidim", "III", "iv", "vm", "bVI", "bVII"],
    "Phrygian": ["i", "bII", "bIII", "iv", "vo", "bVI", "bvii"],
}

# User inputs a Mode from selection, a random section of the items contained within the array called
# are then printed and 'K'determines the number of items printed from the array

while True:
    mode = input(
        'Please pick a mode: Lydian, Ionian, Mixolydian,Dorian, Aelian, Phrygian or Locrian///'
    )

    if mode == "Lydian":

        print(random.choices(TheModes.get("Lydian"), k=4))
    elif mode == "Ionian":
        print(random.choices(TheModes.get("Ionian"), k=4))
    elif mode == "Mixolydian":
        print(random.choices(TheModes.get("Mixolydian"), k=4))
    elif mode == "Dorian":
        print(random.choices(TheModes.get("Dorian"), k=4))
    elif mode == "Aeolian":
        print(random.choices(TheModes.get("Aeolian"), k=4))
    elif mode == "Phrygian":
        print(random.choices(TheModes.get("Phrygian"), k=4))

    restart = input("Would you like to try again? ")

    if restart == "yes" or "y":
        continue

    else :
        
        break