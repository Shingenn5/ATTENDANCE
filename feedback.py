import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

def submit_feedback():
    """
    Retrieves the text from the input fields and prints it to the console.
    """
    # .get() is used for single-line Entry widgets
    name = name_entry.get()
    email = email_entry.get()
    
    # For the multi-line Text widget, we specify the start ('1.0') and end ('end-1c')
    # '1.0' means line 1, character 0. 'end-1c' gets all text except the final newline.
    feedback = feedback_text.get("1.0", "end-1c")
    
    # Print the collected feedback to the console
    print("\n----- FEEDBACK RECEIVED -----")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback: {feedback}")
    print("---------------------------\n")

# --- GUI Setup ---

# Create the main window
root = tk.Tk()
root.title("Feedback Form")
root.geometry("450x350") # Set a default size for the window

# Use a frame for better organization
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)

# --- Widgets ---

# 1. Header
# Create a custom font for the header
header_font = tkfont.Font(family="Helvetica", size=16, weight="bold")

header_label = ttk.Label(main_frame, text="We'd Love Your Feedback!", font=header_font)
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# 2. Name Field
name_label = ttk.Label(main_frame, text="Name:")
name_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

name_entry = ttk.Entry(main_frame, width=40)
name_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# 3. Email Field
email_label = ttk.Label(main_frame, text="Email:")
email_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

email_entry = ttk.Entry(main_frame, width=40)
email_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# 4. Feedback Text Box
feedback_label = ttk.Label(main_frame, text="Feedback:")
feedback_label.grid(row=3, column=0, sticky="nw", padx=5, pady=5) # 'n' for north alignment

feedback_text = tk.Text(main_frame, width=40, height=8)
feedback_text.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

# 5. Submit Button
submit_button = ttk.Button(main_frame, text="Submit", command=submit_feedback)
submit_button.grid(row=4, column=1, sticky="e", padx=5, pady=15) # 'e' for east alignment

# Configure column weights to make the entry fields resize with the window
main_frame.columnconfigure(1, weight=1)

# --- Start the Application ---
root.mainloop()