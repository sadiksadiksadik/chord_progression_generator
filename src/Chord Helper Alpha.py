import random

TheModes = {
    "Ionian": ["I", "ii", "iii", "IV", "V", "vi", "vio"],

    "Mixolydian": ["I", "ii", "iii", "IV", "vm", "vi", "bVII"],

    "Lydian": ["I", "II", "iii", "#ivdim", "V", "vi", "vii"],

    "Dorian": ["i", "ii", "bIII", "IV", "vm", "vidim", "bVII"],

    "Aeolian": ["i", "iidim", "III", "iv", "vm", "bVI", "bVII"],

    "Phrygian": ["i", "bII", "bIII", "iv", "vo", "bVI", "bvii"],
}

    # majormodes = ["Lydian", "Ionian", "Mixolydian",
    #       "Dorian", "Aeolian", "Phrygian"]
    # mode = (random.choice(majormodes))

    # User inputs a Mode from selection, a random section of the items contained within the array called
    # are then printed and 'K'determines the number of items printed from the array
while True:
    #kinput = random.randint(1, 6)
    
    kinput = input("How many Chords would you like in your Progression: ")
    


    print ("-----------------------------------------")
    print ("____________Modes Available______________")
    print ("Lydian/Ionian/Mixolydian/Dorian/Aeolian/Phrygian")
    print ("_________________________________________")
    mode = input(
        'Please pick a mode: ')

    print("___________________________________________")
    if mode == "Lydian":
        print(random.choices(TheModes.get("Lydian"), k=int(kinput)))
    elif mode == "Ionian":
        print(random.choices(TheModes.get("Ionian"), k=int(kinput)))
    elif mode == "Mixolydian":
        print(random.choices(TheModes.get("Mixolydian"), k=int(kinput)))
    elif mode == "Dorian":
        print(random.choices(TheModes.get("Dorian"), k=int(kinput)))
    elif mode == "Aeolian":
        print(random.choices(TheModes.get("Aeolian"), k=int(kinput)))
    elif mode == "Phrygian":
        print(random.choices(TheModes.get("Phrygian"), k=int(kinput)))
        print("_________________________________________")
        print("_________________________________________")
    restart = input(
        "Would you like to try again? y/n: "
        )
    if restart == "n":
        break
