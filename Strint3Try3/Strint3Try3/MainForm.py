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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(34, 49)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "get letter"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(155, 49)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(308, 48)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(34, 119)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Insert word:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(180, 172)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(225, 151)
		self._label2.TabIndex = 4
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(34, 172)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(149, 40)
		self._label3.TabIndex = 5
		self._label3.Text = "First letter of inserted word:"
		self._label3.Click += self.Label3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(155, 116)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(528, 404)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Strint3Try3"
		self.ResumeLayout(False)
		self.PerformLayout()
		


	def Button1Click(self, sender, e):
		self._label3.Text = " " 
		
		string = self._textBox1.Text 
		string = string.lower()
		lcv = 0
		lcv2 = 1
		letter1 = string[0:1]
		count = 0
		self._label2.Text = letter1

	def Button2Click(self, sender, e):
		self._label3.Text = " " 
		self._label2.Text = " " 
		self.textBox1.Text = " " 

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label3Click(self, sender, e):
		pass