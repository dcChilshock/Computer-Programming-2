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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(135, 276)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(216, 276)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(298, 277)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(61, 91)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(61, 67)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 67)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(42, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "num1:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 94)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(42, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "num2:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 121)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(42, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "num3:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(13, 148)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(42, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "num4:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(13, 171)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(207, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Sum:"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(13, 194)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(197, 23)
		self._label6.TabIndex = 10
		self._label6.Text = "average:"
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(61, 118)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 11
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(61, 144)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 12
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RosyBrown
		self.ClientSize = System.Drawing.Size(717, 451)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		sum = num1 + num2 + num3 + num4
		average = sum / 4
		self._label5.Text = "Sum: " + str(sum)

	def Button2Click(self, sender, e):
		self._label5.Text = "Sum: "
		self._label6.Text = "average: "

	def Button3Click(self, sender, e):
		Application.Exit()

	def TextBox2TextChanged(self, sender, e):
		pass