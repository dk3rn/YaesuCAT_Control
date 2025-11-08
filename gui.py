import customtkinter as ctk
import omnipyrig
import time




def convert_number():
    # Lese die eingegebene Zahl aus dem Eingabefeld
    number_input = entry.get()

    try:
        # Wandle die Zahl in zwei Teile um (vor und nach dem Komma)
        integer_part, decimal_part = number_input.split('.')

        # Formatiere die ganze und die Dezimalzahlen in das erforderliche Format
        formatted_string = f"FA{int(integer_part):03}{int(decimal_part):03}000"

        # Setze das Ergebnis im Ergebnis-Label
        result_label.config(text=f"Ergebnis: {formatted_string}")
    except ValueError:
        # Fehlerbehandlung, falls das Format nicht korrekt ist
        result_label.config(text="Bitte eine gültige Zahl im Format X.XXX eingeben.")


def apf_on():
    OmniClient.setCustomCommand("CO020001;", 10, 9)
    time.sleep(100 / 1000)

def apf_off():
    OmniClient.setCustomCommand("CO020000;", 10, 9)
    time.sleep(100 / 1000)
    
def btn_cw_l():
    OmniClient.setCustomCommand("MD03;", 10, 9)
    time.sleep(100 / 1000)

def btn_lsb():
    OmniClient.setCustomCommand("MD01;", 10, 9)
    time.sleep(100 / 1000)

def btn_usb():
    OmniClient.setCustomCommand("MD02;", 10, 9)
    time.sleep(100 / 1000)

def btn_nar():
    print("NAR Button gedrückt")

def btn_mid():
    print("MID Button gedrückt")

def btn_wid():
    print("WID Button gedrückt")

def btn_15m():
    OmniClient.setCustomCommand("FA021002000;", 0, 9)
    time.sleep(100 / 1000)

def btn_17m():
    OmniClient.setCustomCommand("FA018070000;", 0, 0)
    time.sleep(100 / 1000)

def btn_20m():
    OmniClient.setCustomCommand("FA014002000;", 0, 9)
    time.sleep(100 / 1000)

def btn_30m():
    OmniClient.setCustomCommand("FA010110000;;", 0, 9)
    time.sleep(100 / 1000)

def btn_40m():
    OmniClient.setCustomCommand("FA007002000;", 0, 9)
    time.sleep(100 / 1000)

def btn_20wpm():
    OmniClient.setCustomCommand("KS020;", 0, 9)
    time.sleep(100 / 1000)

def btn_22wpm():
    OmniClient.setCustomCommand("KS022;", 0, 9)
    time.sleep(100 / 1000)

def btn_23wpm():
    OmniClient.setCustomCommand("KS023;", 0, 9)
    time.sleep(100 / 1000)
def btn_25wpm():
    OmniClient.setCustomCommand("KS025;", 0, 9)
    time.sleep(100 / 1000)

def btn_28wpm():
    OmniClient.setCustomCommand("KS028;", 0, 9)
    time.sleep(100 / 1000)

def btn_10w():
    OmniClient.setCustomCommand("PC010;", 0, 9)
    time.sleep(100 / 1000)

def btn_24w():
    OmniClient.setCustomCommand("PC024;", 0, 9)
    time.sleep(100 / 1000)

def btn_42w():
    OmniClient.setCustomCommand("PC042;", 0, 9)
    time.sleep(100 / 1000)
def btn_84w():
    OmniClient.setCustomCommand("PC084;", 0, 9)
    time.sleep(100 / 1000)

def btn_100w():
    OmniClient.setCustomCommand("PC100;", 0, 9)
    time.sleep(100 / 1000)
    
def btn_key_on():
    OmniClient.setCustomCommand("KR1;", 0, 9)
    time.sleep(100 / 1000)

def btn_key_off():
    OmniClient.setCustomCommand("KR0;", 0, 9)
    time.sleep(100 / 1000)


def create_window():
    ctk.set_appearance_mode("dark")
    window = ctk.CTk()
    window.title("FT-710 Tiny Ctrl")
    window.geometry("400x185")

    # Buttons erstellen mit entsprechenden Funktionen
    buttons = [
        ("APF ON", apf_on, 0, 0),
        ("APF OFF", apf_off, 0, 1),
        ("CW_L", btn_cw_l, 0, 2),
        ("LSB", btn_lsb, 0, 3),
        ("USB", btn_usb, 0, 4),
        ("15m", btn_15m, 2, 0),
        ("17m", btn_17m, 2, 1),
        ("20m", btn_20m, 2, 2),
        ("30m", btn_30m, 2, 3),
        ("40m", btn_40m, 2, 4),
        ("20WPM", btn_20wpm, 3, 0),
        ("22WPM", btn_22wpm, 3, 1),
        ("23WPM", btn_23wpm, 3, 2),
        ("25WPM", btn_25wpm, 3, 3),
        ("28WPM", btn_28wpm, 3, 4),
        ("10W", btn_10w, 4, 0),
        ("24W", btn_24w, 4, 1),
        ("42W", btn_42w, 4, 2),
        ("84W", btn_84w, 4, 3),
        ("100W", btn_100w, 4, 4),
        ("Keyer On", btn_key_on, 5, 0),
        ("Keyer Off", btn_key_off, 5, 1)

    ]


    for text, command, row, col in buttons:
        button = ctk.CTkButton(master=window, text=text, command=command, width=60, height=25)
        button.grid(row=row, column=col, padx=5, pady=5)

    # Slider erstellen
    def slider_event(value):
        print(f"Slider Value: {value}")

    #slider = ctk.CTkSlider(master=window, from_=-250, to=250, command=slider_event)
    #slider.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Mausradsteuerung
    #slider.bind("<MouseWheel>", lambda event: slider.set(slider.get() + event.delta/120))




    window.mainloop()

if __name__ == "__main__":
    # create a new instance
    OmniClient = omnipyrig.OmniRigWrapper()

    # set the active rig to 1 (as defined in OmniRig GUI)
    OmniClient.setActiveRig(1)
    RigType = OmniClient.getParam("RigType")
    print(f'Rig 1: {RigType}')

    create_window()





# Label für die Eingabeaufforderung
prompt_label = ctk.Label(root, text="Gib eine Zahl im Format X.XXX ein:")
prompt_label.pack()

# Eingabefeld für die Zahl
entry = tk.Entry(root)
entry.pack()

# Button zum Konvertieren der Zahl
convert_button = tk.Button(root, text="Konvertieren", command=convert_number)
convert_button.pack()

# Label, um das Ergebnis anzuzeigen
result_label = tk.Label(root, text="")
result_label.pack()

# Startet die Tkinter-Hauptschleife
root.mainloop()