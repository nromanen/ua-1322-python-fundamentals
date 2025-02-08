import tkinter as tk
from tkinter import font
from OMW_task3 import get_weather_api

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

def check_input_format(location: str) -> str:
    location = location.strip()
    if location.find(",") >= 0:
        location = [x.replace(" ", "") for x in location.split(",")]
        location = location[0].capitalize() + ", " + location[-1].upper()
    elif location.find(" ") >= 0:
        location = [x.replace(" ", "") for x in location.split(" ")]
        location = location[0].capitalize() + ", " + location[-1].upper()
    return location

def get_weather(location: str) -> None:
    location = check_input_format(location)
    w = get_weather_api(location)
    if w:
        formated_w = f"{location} Weather:\n\
{w.detailed_status}\n\
Wind: {w.wind()}\n\
Humidity: {w.humidity}%\n\
Temperature: {w.temperature('celsius')}\n\
Rain: {w.rain}\n\
Heat Index: {w.heat_index}\n\
Clouds: {w.clouds}\n\
"
    else: formated_w = "City not found"

    label.config(text=formated_w, wraplength=label.winfo_width())


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 10), anchor="nw", justify="left")
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

