import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Green
		self._textBox1.Location = System.Drawing.Point(13, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(242, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Maroon
		self._textBox2.Location = System.Drawing.Point(13, 40)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(242, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Orange
		self._label1.Location = System.Drawing.Point(6, 63)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(255, 118)
		self._label1.TabIndex = 2
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Cyan
		self._button1.Location = System.Drawing.Point(5, 184)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(127, 59)
		self._button1.TabIndex = 3
		self._button1.Text = "calc"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Indigo
		self._button2.Location = System.Drawing.Point(6, 249)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(248, 62)
		self._button2.TabIndex = 4
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Chartreuse
		self._button3.Location = System.Drawing.Point(138, 184)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(123, 59)
		self._button3.TabIndex = 5
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(266, 313)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lp3-7"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label1.Text = ""
		

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		from ClLP37 import *
		obj1 = ClLP37(num1, num2)	
		obj2 = ClLP37(num2, num1)
		obj1.calc()
		obj2`.calc()
		div1 = obj1.getDiv()
		mod1 = obj1.getMod()
		div2, mod2 = obj2.getDivMod()
		
		self._label1.Text = str(num1) + "/" + str(num2) + "=" + str(div1) + "\n"
		self._label1.Text += str(num1) + "%" + str(num2) + "=" + str(mod1) + "\n\n"
		self._label1.Text += str(num2) + "/" + str(num1) + "=" + str(div2) + "\n"
		self._label1.Text += str(num2) + "%" + str(num1) + "=" + str(mod2) + "\n"
		
		

	def Button3Click(self, sender, e):
		Application.Exit()