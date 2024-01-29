﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(112, 290)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(293, 290)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(222, 343)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(45, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Radius:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 40)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(140, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Area:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(140, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Circumfrence:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(65, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(612, 445)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = "Area: "
		self._label3.Text = "Circumfrence: "

	def Button1Click(self, sender, e):
		radius = float(self._textBox1.Text)
		circumfrence = 2 * 3.14159 * radius
		area = 3.14159 * (radius ** 2)
		self._label2.Text ="Area: " + str(round(area, 3))
		self._label3.Text = "Circumfrence: " + str(round(circumfrence, 3))
		