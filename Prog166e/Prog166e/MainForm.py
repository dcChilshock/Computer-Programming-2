import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(293, 44)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(120, 95)
		self._listBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(155, 44)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "decimals and stuff"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(56, 178)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(326, 178)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 4
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(194, 247)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 5
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Pink
		self.ClientSize = System.Drawing.Size(734, 425)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog166e"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()
		

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		domenator = 2 
		numerator = 1
		
		self._listBox1.Items.Clear()
		while domenator <= 15:
			while numerator < domenator:
				fraction = float(numerator) / float(domenator)
				fractionstring = str(numerator) + "/" + str(domenator)
				self._listBox1.Items.Add(fractionstring + " = " + str(round(fraction, 5)))
				numerator += 1
			numerator = 1
			domenator += 1
		