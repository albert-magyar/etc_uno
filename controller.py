from numpy import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import warnings
import serial
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]

if not arduino_ports:
    raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0],9600)

running = True
etc_0 = 0.0

def set_etc_pct(percent):
  ser.write(chr(int(percent)).encode())
  print ser.readline()

def stop_running():
  running = False

axis_color = 'lightgoldenrodyellow'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.25, bottom=0.25)

# Add two sliders for tweaking the parameters
etc_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg=axis_color)
etc_slider = Slider(etc_slider_ax, 'ETC %', 0.0, 100.0, valinit=etc_0)
def slider_on_changed(val):
    set_etc_pct(val)
    fig.canvas.draw_idle()
etc_slider.on_changed(slider_on_changed)

# Add a button for resetting the parameters
quit_button_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
quit_button = Button(quit_button_ax, 'Quit', color=axis_color, hovercolor='0.975')
def quit_button_on_clicked(mouse_event):
    quit()
quit_button.on_clicked(quit_button_on_clicked)

  
plt.show()