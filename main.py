import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import urllib.request
import json


def check_json(text):
	try:
		json.loads(text)
	except:
		return False
	else:
		return True


def save_file():
	text = edit_area.get('1.0', tk.END)
	if not check_json(text):
		mb.showerror(title="Error", message="Сохараняемый документ - не формата JSON")
		return

	name = fd.asksaveasfilename(filetypes=[("JSON files", "*.json"),])

	file = open(name, 'w')
	file.write(text)
	file.close()


def load_file():
	try:
		url = sd.askstring('', 'Введите URL адрес файла JSON')
		data = urllib.request.urlopen(url)
	except:
		mb.showerror(title="Error", message="Неверный URL")
	else:
		text = data.read().decode('utf-8')
		edit_area.delete('1.0', tk.END)
		edit_area.insert('1.0', text)




window = tk.Tk()
window.title('kolychestiy editor')

menu = tk.Menu(window)
window.config(menu = menu)

window.attributes('-zoomed', True)

menu.add_command(label = 'load', command = load_file)
menu.add_command(label = 'save', command = save_file)

edit_area = tk.Text(
	window,
	font = 'monospace',
	wrap = 'word',
	bg = "#000",
	fg = "#FFF",
	insertbackground = "#CC6"
)

edit_area.pack(
	fill = 'both',
	expand = 1
)	

window.mainloop()