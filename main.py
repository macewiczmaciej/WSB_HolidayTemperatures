import datetime
import tkinter
from tkinter import Entry, ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import HolidayService
import TemperatureService


def draw_plot():
    temperatures = []
    selected_holiday = cb.get()
    from_year = int(txt_from_year.get())
    to_year = int(txt_to_year.get())

    for i in range(from_year, to_year + 1):
        temperatures.append(TemperatureService.TemperatureService.get_holiday_temperature(
            HolidayService.HolidayService.get_holiday_date(selected_holiday, i)))
    dates = list(range(from_year, to_year + 1))

    fig = Figure(figsize=(5, 5), dpi=100)
    plot = fig.add_subplot(111)

    plot.set_xlabel('Year')
    plot.set_ylabel('Temperature °C')
    plot.bar(dates, temperatures)
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)


form = tkinter.Tk()
form.title("My Temperature App")
form.geometry("1000x600")

lbl_info = tkinter.Label(form, text="Temperatures over the years", font=("Times New Roman", 20), fg="blue")
lbl_info.grid(row=0, column=1, pady=10, padx=10)

left_frame = tkinter.Frame(form)
left_frame.grid(row=1, column=0)

right_frame = tkinter.Frame(form)
right_frame.grid(row=1, column=1)

tkinter.Label(left_frame, text="Enter year between 2014 and 2021").grid(row=1, column=1)

tkinter.Label(left_frame, text="From: ").grid(row=2, column=0)
txt_from_year = tkinter.Entry(left_frame, width=20)
txt_from_year.grid(row=2, column=1, pady=5, padx=5)

tkinter.Label(left_frame, text="To: ").grid(row=3, column=0)
txt_to_year = tkinter.Entry(left_frame, width=20)
txt_to_year.grid(row=3, column=1, pady=5, padx=5)

plot_frame = tkinter.Frame(right_frame)
plot_frame.grid(row=0, column=0, pady=5, padx=5)

holidays = HolidayService.HolidayService.get_holidays()

tkinter.Label(left_frame, text="Holiday: ").grid(row=0, column=0)
cb = ttk.Combobox(left_frame, values=holidays, width=20)
cb.grid(row=0, column=1, pady=5, padx=5)

btnShow = tkinter.Button(form, width=30, height=2, text="Show plot", command=draw_plot)
btnShow.grid(row=4, column=0, padx=20, pady=20)

tkinter.mainloop()
