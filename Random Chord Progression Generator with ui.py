import random
import tkinter as tk

# Random Chord Generator Functions
def random_major_progression():
    
    # selects a random number of chords/items from the Ionian and assigns string to variable major_progression
    kinputvar = random.randint(1, 4)
    Ionian = ("I", "ii", "iii", "IV", "V", "vi", "vio")
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
    kinputvar = random.randint(1, 4)
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
    kinputvar = random.randint(1, 4)
    melodic_minor = ("i", "ii", "bIII+", "IV", "V", "vio", "viio")
    melodic_minor_progression = random.choices(melodic_minor, k=int(kinputvar))
    
    # Enables changes to be made to tkinter text boxes
    progressionbox.config(state='normal')
    
    # Inserts chord progression string contained in major_progression
    progressionbox.delete('1.0', 'end')
    progressionbox.insert('1.0', melodic_minor_progression)
    
    # Disables changes for tkinter text boxes
    progressionbox.config(state='disabled')


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


