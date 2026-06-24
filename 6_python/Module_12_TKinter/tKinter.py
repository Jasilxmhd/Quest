import tkinter as tk

# Create main window
root = tk.Tk()
root.title("TRAKiT")
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Hello, BRO!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="Click Me")
button.pack()

# Run the application
root.mainloop()


