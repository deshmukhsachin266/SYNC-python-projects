import datetime
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        now = datetime.datetime.now()
        alarm = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
        
        if alarm < now:
            alarm = alarm + datetime.timedelta(days=1)  # If the alarm time is in the past, set it for the next day
        
        time_diff = alarm - now
        seconds = time_diff.total_seconds()
        
        root.after(int(seconds * 1000), show_alarm_message)  # Schedule the alarm to show after the time difference
        
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM format.")

def show_alarm_message():
    messagebox.showinfo("Alarm", "Wake up!")
    
# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create label and entry for alarm time
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create button to set the alarm
button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

# Start the main event loop
root.mainloop()
