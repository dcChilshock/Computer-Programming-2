
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(23, 38)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(220, 58)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "checkBox1"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(23, 122)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "checkBox2"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(23, 220)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 29)
		self._button1.TabIndex = 2
		self._button1.Text = "Reset"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(139, 220)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 29)
		self._button2.TabIndex = 3
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.ResumeLayout(False)

