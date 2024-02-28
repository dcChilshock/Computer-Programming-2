import System.Drawing
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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gold
		self._button1.Location = System.Drawing.Point(12, 106)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 25)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gold
		self._button2.Location = System.Drawing.Point(11, 137)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(130, 25)
		self._button2.TabIndex = 1
		self._button2.Text = "exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gold
		self._button3.Location = System.Drawing.Point(11, 168)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(129, 25)
		self._button3.TabIndex = 2
		self._button3.Text = "clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(191, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "What size pizza (diameter) in inches?"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(13, 40)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(129, 20)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Gold
		self._label2.Location = System.Drawing.Point(14, 67)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(114, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Total cost of the pizza."
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(11, 80)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(171, 23)
		self._label3.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Silver
		self.ClientSize = System.Drawing.Size(194, 196)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lp3-2ClassForm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		dim = int(self._textBox1.Text)
		from Class1 import * 
		obj = Class1(dim)
		obj.calc()
		fin = obj.find()
		cost = obj.costt()
		self._label3.Text = "$" + str(cost)

	def Button3Click(self, sender, e):
		self._textBox1.Text = " "
		self._label3.Text = " " 

	def Button2Click(self, sender, e):
		Application.Exit()