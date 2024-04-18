
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
		
	
	def InitializeComponent(self):
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(12, 0)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(220, 32)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Confrence Registration: $896"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(12, 38)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(198, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Opening Night dinner & keynote: $30"
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
		self._button2.Click += self.Button2Click
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Intro to E-Commerce",
			"The Future of the web",
			"Advanced Visual Basic",
			"Network security"]))
		self._comboBox1.Location = System.Drawing.Point(23, 89)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 4
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self.Close()
		self.myparent.Show()