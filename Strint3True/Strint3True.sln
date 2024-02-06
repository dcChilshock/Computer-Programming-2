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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(71, 30)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(223, 29)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(343, 29)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(165, 118)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(57, 118)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "label1"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(38, 164)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(82, 28)
		self._label2.TabIndex = 5
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(164, 236)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "label3"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(588, 434)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Strint3True"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = " " 
		
		string = self._textBox1.Text 
		string = string.lower()
		lcv2 = 0
		letter1 = string[lcv2]
		
		for lcv in range(len(string)):
			letter2 = string[lcv]
			while lcv != range(len(string)):
				if letter1 == letter2:
					lcv2 += 1
					lcv == 0
				else:
					lcv += 1
		self._label3.Text = "No non-repeated letters"
				
			