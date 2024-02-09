﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(110, 103)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(399, 226)
		self._button1.TabIndex = 0
		self._button1.Text = "Show new form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(650, 449)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Multiforms"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import * 
		form1 = Form1(self, "Hello, world!") 
		form1.Show()
		self.Hide()
		
		# from electricboogalo2 import*
		# form2 = SecondForm()
		# form2.Show()
		#self.Hide