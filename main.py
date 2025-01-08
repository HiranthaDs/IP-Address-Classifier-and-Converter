# main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from ip_calculator import calculate_ip_class, convert_to_binary

def calculate():
    # Retrieve input from the user
    try:
        octet1 = int(entry_octet1.get())
        octet2 = int(entry_octet2.get())
        octet3 = int(entry_octet3.get())
        octet4 = int(entry_octet4.get())

        # Calculate IP class, subnet mask, network ID, and host ID
        ip_class, subnet_mask, network_id, host_id = calculate_ip_class(octet1, octet2, octet3, octet4)

        # Update the results in the UI
        entry_class.delete(0, tk.END)
        entry_class.insert(0, ip_class)

        entry_subnet_mask.delete(0, tk.END)
        entry_subnet_mask.insert(0, subnet_mask)

        entry_network_id.delete(0, tk.END)
        entry_network_id.insert(0, network_id)

        entry_host_id.delete(0, tk.END)
        entry_host_id.insert(0, host_id)

        # Convert IP to binary
        binary_ip = convert_to_binary(octet1, octet2, octet3, octet4)
        entry_binary.delete(0, tk.END)
        entry_binary.insert(0, binary_ip)

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main tkinter window
root = tk.Tk()
root.title("IP Clover - Easy IP Diagnostic Tool")
root.geometry("500x600")  # Set the window size to 500x600

# Load the image for background
background_image = PhotoImage(file=r"C:\Users\Administrator\Desktop\Git Work\ip_clover\pythonProject1\images\background1.png")

# Create a Label widget to display the image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Set the label to cover the entire window

# Add a headline Label
headline_label = tk.Label(root, text="IP Converter", font=("Arial", 24, "bold"), fg="white", bg="#9f3131")
headline_label.pack(pady=20)

# Label for Entering IP Address
label_enter_ip = tk.Label(root, text="Enter IP Address", font=("Arial", 16), fg="white", bg="#9f3131")
label_enter_ip.pack(pady=10)

# Create a frame for the inputs (without borders)
frame_input = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_input.pack(pady=10, padx=30, fill="x")

# Add input fields for the IP address
entry_octet1 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet1.grid(row=0, column=0, padx=5)

label_dot1 = tk.Label(frame_input, text=".", font=("Arial", 14), bg="#f0f0f0")
label_dot1.grid(row=0, column=1)

entry_octet2 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet2.grid(row=0, column=2, padx=5)

label_dot2 = tk.Label(frame_input, text=".", font=("Arial", 14), bg="#f0f0f0")
label_dot2.grid(row=0, column=3)

entry_octet3 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet3.grid(row=0, column=4, padx=5)

label_dot3 = tk.Label(frame_input, text=".", font=("Arial", 14), bg="#f0f0f0")
label_dot3.grid(row=0, column=5)

entry_octet4 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet4.grid(row=0, column=6, padx=5)

# Add a "Calculate" button
btn_calculate = tk.Button(root, text="Calculate", font=("Arial", 14), bg="#04AA6D", fg="white", command=calculate)
btn_calculate.pack(pady=20)

# Create a frame for the outputs (without borders)
frame_output = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame_output.pack(pady=10, padx=30, fill="x")

# Output fields for the results
label_class = tk.Label(frame_output, text="Detected Class:", font=("Arial", 12), bg="#f0f0f0")
label_class.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_class = tk.Entry(frame_output, width=20, font=("Arial", 12))
entry_class.grid(row=0, column=1, padx=5, pady=5)

label_subnet_mask = tk.Label(frame_output, text="Detected Subnet Mask:", font=("Arial", 12), bg="#f0f0f0")
label_subnet_mask.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_subnet_mask = tk.Entry(frame_output, width=20, font=("Arial", 12))
entry_subnet_mask.grid(row=1, column=1, padx=5, pady=5)

label_network_id = tk.Label(frame_output, text="Network ID:", font=("Arial", 12), bg="#f0f0f0")
label_network_id.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_network_id = tk.Entry(frame_output, width=20, font=("Arial", 12))
entry_network_id.grid(row=2, column=1, padx=5, pady=5)

label_host_id = tk.Label(frame_output, text="Host ID:", font=("Arial", 12), bg="#f0f0f0")
label_host_id.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_host_id = tk.Entry(frame_output, width=20, font=("Arial", 12))
entry_host_id.grid(row=3, column=1, padx=5, pady=5)

# Add a field for binary IP address output
label_binary_ip = tk.Label(frame_output, text="Binary Representation:", font=("Arial", 12), bg="#f0f0f0")
label_binary_ip.grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_binary = tk.Entry(frame_output, width=20, font=("Arial", 12))
entry_binary.grid(row=4, column=1, padx=5, pady=5)

# Start the tkinter event loop
root.mainloop()
