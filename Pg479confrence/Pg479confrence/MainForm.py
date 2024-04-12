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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._textBox8 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(58, 389)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 34)
		self._button1.TabIndex = 0
		self._button1.Text = "Confrence Options"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(198, 389)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 34)
		self._button2.TabIndex = 1
		self._button2.Text = "Reset"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(342, 389)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(110, 34)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(40, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Regestration"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(40, 57)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(59, 98)
		self._label2.TabIndex = 4
		self._label2.Text = """Name:

Company:

Address:

City:"""
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(198, 57)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(59, 99)
		self._label3.TabIndex = 5
		self._label3.Text = """Phone:

Email:

State:

Zip:"""
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(93, 57)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(93, 83)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(92, 109)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 8
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(92, 135)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 9
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(239, 135)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(100, 20)
		self._textBox5.TabIndex = 10
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(239, 109)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(100, 20)
		self._textBox6.TabIndex = 11
		# 
		# textBox7
		# 
		self._textBox7.Location = System.Drawing.Point(239, 83)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(100, 20)
		self._textBox7.TabIndex = 12
		# 
		# textBox8
		# 
		self._textBox8.Location = System.Drawing.Point(239, 57)
		self._textBox8.Name = "textBox8"
		self._textBox8.Size = System.Drawing.Size(100, 20)
		self._textBox8.TabIndex = 13
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(45, 202)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 14
		self._label4.Text = "Total Cost:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(555, 435)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox8)
		self.Controls.Add(self._textBox7)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg479confrence"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = " " 
		self._textBox2.Text = " "
		self._textBox3.Text = " "
		self._textBox4.Text = " "
		self._textBox5.Text = " "
		self._textBox6.Text = " "
		self._textBox7.Text = " "
		self._textBox8.Text = " "
		self._label4.Text = " "