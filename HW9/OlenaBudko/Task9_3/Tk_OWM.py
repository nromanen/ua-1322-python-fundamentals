import tkinter as tk
from tkinter import messagebox as msg
from OWM import get_api_weather

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))

entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

output = tk.StringVar()


def get_weather(city):
    if not city:
        msg.showwarning(title="Warning", message="City wasn't provided, please check input")
        return
    output.set("")  # clean output
    try:
        api_response = get_api_weather(city)
    except Exception as ex:
        msg.showerror(title="Ooops", message=f"{ex}")
        entry_field.delete(0, 'end')  # clean input field
    else:
        response = f"""
        Now: {api_response.detailed_status}\n
        Wind: speed {api_response.wind()["speed"]} deg {api_response.wind()["deg"]}\n
        Humidity: {api_response.humidity}%\n
        Temperature: {int(api_response.temperature('celsius')["temp"])}C\n
        Clouds: {api_response.clouds}%\n
        """
        output.set(response)


button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="black",
                   font=('Courier', 12),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, textvariable=output, font=('Courier', 14), justify="left")
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
