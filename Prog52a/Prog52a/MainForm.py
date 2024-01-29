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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(116, 289)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(245, 288)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(391, 287)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(28, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(40, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Length:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(28, 79)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(138, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "area:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(28, 182)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(119, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "perimeter:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(245, 13)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(321, 182)
		self._label5.TabIndex = 7
		self._label5.Text = "label5"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(74, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(74, 42)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 10
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(28, 38)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(40, 23)
		self._label2.TabIndex = 11
		self._label2.Text = "width:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleTurquoise
		self.ClientSize = System.Drawing.Size(578, 442)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = "area: "
		self._label4.Text = "perimeter: "

	def Button1Click(self, sender, e):
		length = int(self._textBox1.Text)
		width =int(self._textBox2.Text)
		area = length * width
		perimeter = (length * 2) + (width * 2)
		self._label3.Text = "area: " + str(area)
		self._label4.Text = "perimeter: " + str(perimeter)
		