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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Tan
		self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Location = System.Drawing.Point(43, 202)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(43, 250)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(43, 312)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(216, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(216, 94)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(117, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(68, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "word 1:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(117, 94)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(68, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "word 2:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(349, 225)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(214, 118)
		self._label3.TabIndex = 7
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(327, 202)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Anagrams"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 1)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(122, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Checking for anagrams"
		self._label5.Click += self.Label5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PapayaWhip
		self.ClientSize = System.Drawing.Size(934, 415)
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
		self.Text = "strInt2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		#show button 
		
		self._label3.Text = " " 
		
		word = self._textBox1.Text 
		anagram = self._textBox2.Text
		
		word = word.lower()
		anagram = anagram.lower()
		
		if len(word) != len(anagram):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = anagram.index(c)
				
				if index != -1:
					anagram = anagram[0:index] + anagram[index+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(anagram) == 0)

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " " 
		self._label3.Text = " " 

	def Button3Click(self, sender, e):
		Application.Exit()