import tkinter as tk
from subprocess import call

def run_file(file_name):
    venv_activate = 'env\\Scripts\\activate'  # Use double backslashes in the path
    script_command = f'python {file_name}.py'  # Concatenate folder path with file name
    full_command = f'{venv_activate} && {script_command}'
    print(full_command)

    try:
        call(full_command, shell=True)
        result_label.config(text=f"File '{file_name}.py' executed successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error executing the file: {str(e)}", fg="red")

# Create main window
window = tk.Tk()
window.title("File Runner")
window.geometry("400x300")  # Set window size
window.configure(bg="#f0f0f0")  # Set background color

# Create and configure widgets
title_label = tk.Label(window, text="Choose an Option", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

button_letter = tk.Button(window, text="Run For Alphabets", command=lambda: run_file('alphabets'), font=("Arial", 14, "bold"), padx=20, pady=10, bg="#4CAF50", fg="white", bd=0, highlightthickness=0)
button_letter.pack(pady=10)

button_letter = tk.Button(window, text="Run For Gestures", command=lambda: run_file('gesture'), font=("Arial", 14, "bold"), padx=20, pady=10, bg="#4CAF50", fg="white", bd=0, highlightthickness=0)
button_letter.pack(pady=10)


result_label = tk.Label(window, text="", font=("Arial", 12), fg="#333", bg="#f0f0f0")
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
