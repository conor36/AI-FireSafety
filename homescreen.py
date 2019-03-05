import tkinter as tk
from tkinter import *
from main import *


class Welcome_Screen(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.canvas = tk.Canvas(self, width=1000, height=700, bg="#ff8080", borderwidth=0, highlightthickness=0)
		self.canvas.pack(padx=(20), pady=(20))
		self.layout_button()
		#self.image()
		self.greeting()

	# create buttons for layouts

	def layout_button(self):
		self.layout1 = tk.Button(self, text="Layout 1", command=self.layout1)
		self.layout1.configure(width = 25, activebackground = "#33B5E5", relief=FLAT)
		self.layout1_Window = self.canvas.create_window(100,500, anchor=NW, window = self.layout1)

		self.layout2 = tk.Button(self, text="Layout 2", command=self.layout1)
		self.layout2.configure(width = 25, activebackground = "#33B5E5", relief=FLAT)
		self.layout2_Window = self.canvas.create_window(400,500, anchor=NW, window = self.layout2)

		self.layout3 = tk.Button(self, text="Layout 3", command=self.layout1)
		self.layout3.configure(width = 25, activebackground = "#33B5E5", relief=FLAT)
		self.layout3_Window = self.canvas.create_window(700,500, anchor=NW, window = self.layout3)	

	# button to exit

		self.close = tk.Button(self, text="Close", command=self.quit) #Leaves the game
		self.close.configure(width = 25, activebackground = "#33B5E5", relief=FLAT)
		self.close_Window = self.canvas.create_window(400,600, anchor=NW, window = self.close)
	'''		
	# add images to screen
	def image(self):
		self.image1 = PhotoImage(file="layout1.png")
		self.canvas.create_image(100,300, image=self.image1, anchor=NW)

		self.image2 = PhotoImage(file="layout2.png")
		self.canvas.create_image(400,300, image=self.image2, anchor=NW)

		self.image3 = PhotoImage(file="layout3.png")
		self.canvas.create_image(700,300, image=self.image3, anchor=NW)
	'''		

	def layout1(self):
		
		self.withdraw()
		main()

	def layout2(self):
		self.withdraw()
		# class from other file

	def layout3(self):
		self.withdraw()
		# class from other file


	def greeting(self):
		self.canvas.create_text(500,150,font = "Time 50 italic bold", text="Welcome")
		self.canvas.create_text(500,225,font = "Time 20 italic bold", text="Please select a layout")


if __name__ == "__main__":
	screen = Welcome_Screen()
	screen.mainloop()