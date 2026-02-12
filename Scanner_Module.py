import tkinter as tk
import tkinter.ttk as ttk
import threading
import psutil

try:
    

    gpu_available = True
except ImportError:
    gpu_available = False


 


def get_cpu_info():
    """Get CPU information"""
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        return f"CPU: {cpu_percent}% usage - Cores: {cpu_count}"
    except Exception as e:
        return f"CPU: Error - {str(e)}"


def get_ram_info():
    """Get RAM information"""
    try:
        ram = psutil.virtual_memory()
        return f"RAM: {ram.percent}% usage - {ram.used // (1024**3)}GB / {ram.total // (1024**3)}GB"
    except Exception as e:
        return f"RAM: Error - {str(e)}"


def update_scan_results():
    """Update all scan results"""
    
    cpu_label.config(text=get_cpu_info())
    ram_label.config(text=get_ram_info())
    scan_button.config(state="normal", text="Start Scan")



def scan_in_thread():
    """Run scan in background thread to avoid freezing GUI"""
    scan_button.config(state="disabled", text="Scanning...")
    update_scan_results()


def start_scan_button_command():
    """Start scan in a background thread"""
    thread = threading.Thread(target=scan_in_thread)
    thread.daemon = True
    thread.start()


title = "Scanner Module"
root = tk.Tk()
root.title(title)
root.geometry("400x250")

# Create labels



cpu_label = tk.Label(
    root, text="CPU: Not scanned yet", font=("Arial", 11), justify="left"
)
cpu_label.pack(pady=10, padx=10, fill="x")

ram_label = tk.Label(
    root, text="RAM: Not scanned yet", font=("Arial", 11), justify="left"
)
ram_label.pack(pady=10, padx=10, fill="x")

# Create scan button
scan_button = tk.Button(
    root,
    text="Start Scan",
    command=start_scan_button_command,
    bg="blue",
    fg="white",
    font=("Arial", 14, "bold"),
)
scan_button.pack(pady=20)

root.mainloop()
