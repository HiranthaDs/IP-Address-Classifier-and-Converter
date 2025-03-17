import tkinter as tk
from tkinter import messagebox
from ip_calculator import calculate_ip_class, convert_to_binary

def calculate():
    """Handles user input, validates the IP, and updates the output fields."""
    try:
        octet1 = int(entry_octet1.get())
        octet2 = int(entry_octet2.get())
        octet3 = int(entry_octet3.get())
        octet4 = int(entry_octet4.get())

        # Ensure octets are in valid range (0-255)
        if any(o < 0 or o > 255 for o in [octet1, octet2, octet3, octet4]):
            raise ValueError("Each octet must be between 0 and 255.")

        # Calculate IP class, subnet mask, network ID, and host ID
        ip_class, subnet_mask, network_id, host_id = calculate_ip_class(octet1, octet2, octet3, octet4)

        # Update the results in the UI
        entry_class.config(state=tk.NORMAL)
        entry_subnet_mask.config(state=tk.NORMAL)
        entry_network_id.config(state=tk.NORMAL)
        entry_host_id.config(state=tk.NORMAL)
        entry_binary.config(state=tk.NORMAL)

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

        # Disable fields again
        entry_class.config(state=tk.DISABLED)
        entry_subnet_mask.config(state=tk.DISABLED)
        entry_network_id.config(state=tk.DISABLED)
        entry_host_id.config(state=tk.DISABLED)
        entry_binary.config(state=tk.DISABLED)

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {str(e)}")

# Create the main tkinter window
root = tk.Tk()
root.title("IP Clover - Easy IP Diagnostic Tool")
root.geometry("500x600")  # Set the window size to 500x600
root.configure(bg="#9f3131")  # Set dark red background

# Add a headline Label
headline_label = tk.Label(root, text="IP Converter", font=("Arial", 24, "bold"), fg="white", bg="#9f3131")
headline_label.pack(pady=20)

# Label for Entering IP Address
label_enter_ip = tk.Label(root, text="Enter IP Address:", font=("Arial", 16), fg="white", bg="#9f3131")
label_enter_ip.pack(pady=10)

# Create a frame for the input fields
frame_input = tk.Frame(root, bg="#9f3131")
frame_input.pack(pady=10, padx=30)

# Add input fields for the IP address
entry_octet1 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet1.grid(row=0, column=0, padx=5)

label_dot1 = tk.Label(frame_input, text=".", font=("Arial", 14), fg="white", bg="#9f3131")
label_dot1.grid(row=0, column=1)

entry_octet2 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet2.grid(row=0, column=2, padx=5)

label_dot2 = tk.Label(frame_input, text=".", font=("Arial", 14), fg="white", bg="#9f3131")
label_dot2.grid(row=0, column=3)

entry_octet3 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet3.grid(row=0, column=4, padx=5)

label_dot3 = tk.Label(frame_input, text=".", font=("Arial", 14), fg="white", bg="#9f3131")
label_dot3.grid(row=0, column=5)

entry_octet4 = tk.Entry(frame_input, width=5, font=("Arial", 14), justify="center")
entry_octet4.grid(row=0, column=6, padx=5)

# Add a "Calculate" button
btn_calculate = tk.Button(root, text="Calculate", font=("Arial", 14), bg="#04AA6D", fg="white", command=calculate)
btn_calculate.pack(pady=20)

# Create a frame for the outputs
frame_output = tk.Frame(root, bg="#9f3131")
frame_output.pack(pady=10, padx=30, fill="x")

# Output fields for the results
def add_output_field(row, label_text):
    label = tk.Label(frame_output, text=label_text, font=("Arial", 12), fg="white", bg="#9f3131")
    label.grid(row=row, column=0, sticky="e", padx=5, pady=5)
    entry = tk.Entry(frame_output, width=20, font=("Arial", 12), state=tk.DISABLED)
    entry.grid(row=row, column=1, padx=5, pady=5)
    return entry

entry_class = add_output_field(0, "Detected Class:")
entry_subnet_mask = add_output_field(1, "Subnet Mask:")
entry_network_id = add_output_field(2, "Network ID:")
entry_host_id = add_output_field(3, "Host ID:")
entry_binary = add_output_field(4, "Binary Representation:")

# Start the tkinter event loop
root.mainloop()
