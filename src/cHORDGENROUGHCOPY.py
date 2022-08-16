import random
import tkinter as tk
from tkinter import *


# Random Chord Generator Functions
def random_major_progression():
    
    # selects a random number of chords/items from the Ionian and assigns string to variable major_progression
    kinputvar = random.randint(2, 6)
    Ionian = ("I", "ii", "iii", "IV", "V", "vi", "viio")
    major_progression = random.choices(Ionian, k=int(kinputvar))
    
    # Enables changes to be made to tkinter text boxes
    progressionbox.config(state='normal')
    
    
    # Inserts chord progression string contained in major_progression
    progressionbox.delete('1.0', 'end')
    progressionbox.insert('1.0', major_progression)
    
    # Disables changes for tkinter text boxes
    progressionbox.config(state='disabled')
    
    
def random_harmonic_minor_progression():
    
    # selects a random number of chords/items from the Ionian and assigns string to variable major_progression
    kinputvar = random.randint(2, 6)
    harmonic_minor = ("i", "iio", "bIII+", "iv", "V", "bVI", "viio")
    harmonic_minor_progression = random.choices(harmonic_minor, k=int(kinputvar))
    
    # Enables changes to be made to tkinter text boxes
    progressionbox.config(state='normal')
    
    # Inserts chord progression string contained in major_progression
    progressionbox.delete('1.0', 'end')
    progressionbox.insert('1.0', harmonic_minor_progression)
    
    # Disables changes for tkinter text boxes
    progressionbox.config(state='disabled')
def random_melodic_minor_progression():
    
    # selects a random number of chords/items from the Ionian and assigns string to variable major_progression
    kinputvar = random.randint(2, 6)
    melodic_minor = ("i", "ii", "bIII+", "IV", "V", "vio", "viio")
    melodic_minor_progression = random.choices(melodic_minor, k=int(kinputvar))
    
    # Enables changes to be made to tkinter text boxes
    progressionbox.config(state='normal')
    
    # Inserts chord progression string contained in major_progression
    progressionbox.delete('1.0', 'end')
    progressionbox.insert('1.0', melodic_minor_progression)
    
    # Disables changes for tkinter text boxes
    progressionbox.config(state='disabled')
    
    # def random_melodic_minor_progression(): MAKE A FUNCTION FOR A RANDOM PROGRESSION 
    # FROM DICT OF CHORDDS  RANDOM PROGRESSION FROM DICT OF CHORDS FROM DIFFERENT MODES!!!!!
    # def random_melodic_minor_progression():
# how to make more than one window for more button options tkinter

def do_function():
    # define a mapping from the choice value to a function name
    func_map = {
        "Major":random_major_progression,
        "Minor":random_harmonic_minor_progression,
        "Melodic":random_melodic_minor_progression
    }
    # using the map, get the function
    function = func_map[var.get()]

    # call the function
    function()
    
def func(val):
    if val == "Major":
        random_melodic_minor_progression()
    elif val == "Minor":
        random_harmonic_minor_progression()
    elif val == "Melodic":
        random_melodic_minor_progression()


# Init display window
root = tk.Tk()
root.title('Chord Progression Generator')
root.geometry('1200x600')

# Chord Progressionbox
progressionlabel = tk.Label(root, text = 'Chord Progression')
progressionlabel.pack()
progressionbox = tk.Text(root, height=5, width=140)
progressionbox.config(state='disabled', bg='#dddddd')
progressionbox.pack()

#2 option menus offering different selections
options1 = ["Major", "Minor", 'Melodic']
variable1 = StringVar()
drop_title1 = StringVar(root)
#sets initial name for widget
drop_title1.set("Please Choose Options 1 Or 2")
dropdownmenu1 = OptionMenu(root, drop_title1, *options1, command=func)
dropdownmenu1.pack(side=RIGHT)

# The Major Chord button
thebutton = tk.Button(root, height=8, width=140, text='Generate a Major Chord Progression', command=random_major_progression)
thebutton.pack()

# The Harmonic Minor Chord button
thebutton = tk.Button(root, height=8, width=140, text='Generate a Harmonic Chord Progression', command=random_harmonic_minor_progression)
thebutton.pack()

# The Melodic Minor Chord button
thebutton = tk.Button(root, height=8, width=140, text='Generate a Melodic Chord Progression', command=random_melodic_minor_progression)
thebutton.pack()

# Keep display window running
root.mainloop()
