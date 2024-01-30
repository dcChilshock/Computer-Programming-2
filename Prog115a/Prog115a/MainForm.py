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
		self._listBox1.Location = System.Drawing.Point(132, 77)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(120, 95)
		self._listBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(63, 77)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(63, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Numbers : "
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 179)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(116, 50)
		self._button1.TabIndex = 2
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(134, 178)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(118, 51)
		self._button2.TabIndex = 3
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(258, 179)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 50)
		self._button3.TabIndex = 4
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumSlateBlue
		self.ClientSize = System.Drawing.Size(865, 428)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog115a"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		#normal if thing another thing else if and on and on 
		#while loops are just if statements that repeat
		lcv = 2 #loop control variable
		#keep loop going for 36 numbers exactly
		while lcv <= 36:
			self._listBox1.Items.Add(str(lcv))
			lcv += 2