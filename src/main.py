import random
import tkinter as tk
from chordgen import constants


# Random Chord Generator Functions
def random_major_progression():
    # selects a random number of chords/items from the Ionian and assigns string to variable major_progression
    kinputvar = random.randint(2, 8)
    major_progression = random.choices(constants.Ionian, k=int(kinputvar))

    # Enables changes to be made to tkinter text boxes
    progressionbox.config(state="normal")

    # Inserts chord progression string contained in major_progression
    progressionbox.delete("1.0", "end")
    progressionbox.tag_configure("center", justify="center")
    progressionbox.insert("1.0", major_progression, "center")

    # Disables changes for tkinter text boxes
    progressionbox.config(state="disabled")


def random_harmonic_minor_progression():

    # selects a random number of chords/items from the Ionian and assigns string to variable major_progression
    kinputvar = random.randint(2, 8)
    harmonic_minor_progression = random.choices(
        constants.harmonic_minor, k=int(kinputvar)
    )

    # Enables changes to be made to tkinter text boxes
    progressionbox.config(state="normal")

    # Inserts chord progression string contained in major_progression
    progressionbox.delete("1.0", "end")
    progressionbox.tag_configure("center", justify="center")
    progressionbox.insert("1.0", harmonic_minor_progression, "center")

    # Disables changes for tkinter text boxes
    progressionbox.config(state="disabled")


def random_melodic_minor_progression():

    # selects a random number of chords/items from the Ionian and assigns string to variable major_progression
    kinputvar = random.randint(2, 8)
    melodic_minor_progression = random.choices(
        constants.melodic_minor, k=int(kinputvar)
    )

    # Enables changes to be made to tkinter text boxes
    progressionbox.config(state="normal")

    # Inserts chord progression string contained in major_progression
    progressionbox.delete("1.0", "end")
    progressionbox.tag_configure("center", justify="center")
    progressionbox.insert("1.0", melodic_minor_progression, "center")

    # Disables changes for tkinter text boxes
    progressionbox.config(state="disabled")

    # def random_melodic_minor_progression(): MAKE A FUNCTION FOR A RANDOM PROGRESSION
    # FROM DICT OF CHORDDS  RANDOM PROGRESSION FROM DICT OF CHORDS FROM DIFFERENT MODES!!!!!
    # def random_melodic_minor_progression():


# The CHORD GENERATOR BUTTON - Function that Retreives a String from dropdown list and deploys function based on selection but for the button
def pick_a_func_button_progression():

    selection = scale_menu.get()

    if selection == "Major":
        random_major_progression()
    elif selection == "Minor":
        random_harmonic_minor_progression()
    elif selection == "Melodic":
        random_melodic_minor_progression()


# The SCALE DISPLAY BUTTON -  Function that Retreives a String from dropdown list and displays the notes of the selected Mode
def pick_a_func_button_scale():

    # Retreives Current String Selected on the Dropdown List
    scale = scale_menu.get()

    # Print Scale Loop
    if scale == "Major":
        # Inserts Major Scale into text box
        progressionbox.config(state="normal")
        progressionbox.delete("1.0", "end")
        progressionbox.tag_configure("center", justify="center")
        progressionbox.insert("1.0", constants.Ionian, "center")

    elif scale == "Minor":
        # Inserts Harmonic Minor Scale into text box
        progressionbox.config(state="normal")
        progressionbox.delete("1.0", "end")
        progressionbox.tag_configure("center", justify="center")
        progressionbox.insert("1.0", constants.harmonic_minor, "center")

    elif scale == "Melodic":
        # Inserts Melodic Minor Scale into text box
        progressionbox.config(state="normal")
        progressionbox.delete("1.0", "end")
        progressionbox.tag_configure("center", justify="center")
        progressionbox.insert("1.0", constants.melodic_minor, "center")

    elif scale == "Ionian_in_thirds":
        # Inserts Melodic Minor Scale into text box
        progressionbox.config(state="normal")
        progressionbox.delete("1.0", "end")
        progressionbox.tag_configure("center", justify="center")
        progressionbox.insert("1.0", constants.Ionian_in_thirds, "center")

        # Disables changes for tkinter text boxes
        progressionbox.config(state="disabled")


def main():
    # Init display window
    root = tk.Tk()
    root.title("Chord Progression Generator")
    root.geometry("600x450")
    root.configure(bg="#000000")

    # Text Box
    progressionbox = tk.Text(root, spacing1=50, height=2, width=180)
    progressionbox.config(bg="#000000")
    progressionbox.config(fg="#FFFFF0")
    progressionbox.config(font=("Terminal", 18, "bold"))
    progressionbox.pack()

    # option menu
    menu_options = ["Major", "Minor", "Melodic", "Ionian_in_thirds"]
    variable1 = tk.StringVar()
    scale_menu = tk.StringVar(root)
    # sets initial name for widget
    scale_menu.set("Please Choose a Mode")
    dropdownmenu1 = tk.OptionMenu(root, scale_menu, *menu_options)
    dropdownmenu1.config(bg="#000000")
    dropdownmenu1.config(fg="#FFFFF0")
    dropdownmenu1.config(height=1, width=140)
    dropdownmenu1.config(font=("Terminal"))
    dropdownmenu1.pack()
    dropdownmenu1.config(activebackground="#FFFFF0")

    # Random Chord Progression Generator Button
    thebutton = tk.Button(
        root,
        height=5,
        width=180,
        text="Generate Chord Progression",
        font=("Terminal", 18, "bold"),
        command=pick_a_func_button_progression,
    )
    thebutton.pack(side=tk.TOP)
    thebutton.configure(bg="#000000")
    thebutton.configure(fg="#FFFFF0")
    thebutton.config(activebackground="#FFFFF0")

    # Display Notes of Selected Mode Button
    thebutton = tk.Button(
        root,
        height=5,
        width=180,
        text="Generate Notes of Scale",
        font=("Terminal", 18, "bold"),
        command=pick_a_func_button_scale,
    )
    thebutton.pack(side=tk.TOP)
    thebutton.configure(bg="#000000")
    thebutton.configure(fg="#FFFFF0")
    thebutton.config(activebackground="#FFFFF0")

    # Keep display window running
    root.mainloop()


if __name__ == "__main__":
    main()
