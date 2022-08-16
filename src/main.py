from dataclasses import dataclass
from enum import Enum, auto
import random
import tkinter as tk

# import mingus.core.progressions as progressions
# import mingus.core.scales as scales


class FunctionType(Enum):
    SCALE = auto()
    PROGRESSION = auto()


class Scale(Enum):
    # Roman numerals represent 1 of 7 chords in a mode
    IONIAN = ["I", "ii", "iii", "IV", "V", "vi", "viio"]
    HARMONIC_MINOR = ["i", "iio", "bIII+", "iv", "V", "bVI", "viio"]
    MELODIC_MINOR = ["i", "ii", "bIII+", "IV", "V", "vio", "viio"]
    # Interval Training
    IONIAN_IN_THIRDS = ["I", "iii", "V", "viio", "ii", "IV", "vi"]

    @classmethod
    def from_menu_option(cls, scale_option: str):
        scale_option_to_scale = {
            "Major": Scale.IONIAN,
            "Minor": Scale.HARMONIC_MINOR,
            "Melodic": Scale.MELODIC_MINOR,
            "Ionian in 3rds": Scale.IONIAN_IN_THIRDS,
        }
        return scale_option_to_scale[scale_option]


@dataclass
class ColourPalette:
    FOREGROUND = "#FFFFF0"
    BACKGROUND = "#000000"


def update_text_ui(
    selected_scale_option: str, text_box: tk.Text, function_type: FunctionType
):
    """
    Update UI with a new chord progression.
    """

    # Enable text changes
    text_box.config(state="normal")

    # Delete existing text
    text_box.delete("1.0", "end")

    # Center text
    text_box.tag_configure("center", justify="center")

    # Determine text
    selected_scale: list = Scale.from_menu_option(selected_scale_option).value

    # Show scale unless we've asked for a progression in the scale
    text_fields: list = selected_scale
    if function_type == FunctionType.PROGRESSION:

        def get_random_progression_for_scale(chord_scale: list, number_of_results=None):
            if not number_of_results:
                number_of_results = random.randint(2, 8)

            major_progression = random.choices(chord_scale, k=number_of_results)
            return major_progression

        text_fields = get_random_progression_for_scale(selected_scale)

    text: str = " ".join(text_fields)

    # Insert text
    text_box.insert("1.0", text, "center")

    # Disable text changes
    text_box.config(state="disabled")


def main():
    # Init display window
    root = tk.Tk()
    root.title("Chord Progression Generator")
    root.geometry("600x450")
    root.configure(bg=ColourPalette.BACKGROUND)

    # Text Box
    progressionbox = tk.Text(root, spacing1=50, height=2, width=180)
    progressionbox.config(bg=ColourPalette.BACKGROUND)
    progressionbox.config(fg=ColourPalette.FOREGROUND)
    progressionbox.config(font=("Terminal", 18, "bold"))
    progressionbox.pack()

    # option menu
    menu_options = ["Major", "Minor", "Melodic", "Ionian in 3rds"]

    scale_menu = tk.StringVar(root)
    # sets initial name for widget
    scale_menu.set("Select Mode/Scale")
    dropdownmenu1 = tk.OptionMenu(root, scale_menu, *menu_options)
    dropdownmenu1.config(bg=ColourPalette.BACKGROUND)
    dropdownmenu1.config(fg=ColourPalette.FOREGROUND)
    dropdownmenu1.config(height=1, width=140)
    dropdownmenu1.config(font=("Terminal"))
    dropdownmenu1.pack()
    dropdownmenu1.config(activebackground=ColourPalette.FOREGROUND)

    # Random Chord Progression Generator Button
    submit_button = tk.Button(
        root,
        height=5,
        width=180,
        text="Generate Chord Progression",
        font=("Terminal", 18, "bold"),
        command=lambda: update_text_ui(
            scale_menu.get(), progressionbox, FunctionType.PROGRESSION
        ),
    )
    submit_button.pack(side=tk.TOP)
    submit_button.configure(bg=ColourPalette.BACKGROUND)
    submit_button.configure(fg=ColourPalette.FOREGROUND)
    submit_button.config(activebackground=ColourPalette.FOREGROUND)

    # Display Notes of Selected Mode Button
    submit_button = tk.Button(
        root,
        height=5,
        width=180,
        text="Generate Notes of Scale",
        font=("Terminal", 18, "bold"),
        command=lambda: update_text_ui(
            scale_menu.get(), progressionbox, FunctionType.SCALE
        ),
    )
    submit_button.pack(side=tk.TOP)
    submit_button.configure(bg=ColourPalette.BACKGROUND)
    submit_button.configure(fg=ColourPalette.FOREGROUND)
    submit_button.config(activebackground=ColourPalette.FOREGROUND)

    # Keep display window running...
    root.mainloop()


if __name__ == "__main__":
    main()
