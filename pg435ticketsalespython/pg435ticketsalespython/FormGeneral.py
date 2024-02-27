
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class FormGeneral(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent 
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "How many tickets?"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(120, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(154, 20)
		self._textBox1.TabIndex = 1
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(13, 67)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(130, 24)
		self._radioButton1.TabIndex = 2
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Section A : 20 dollars "
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(12, 97)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(131, 24)
		self._radioButton2.TabIndex = 3
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Section B : 15 dollars"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(13, 127)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(130, 24)
		self._radioButton3.TabIndex = 4
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Section C : 10 dollars"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 40)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Pick a Section."
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(149, 73)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Total Cost:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(149, 98)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Tickets:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(149, 127)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Tax:"
		self._label5.Click += self.Label5Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(176, 39)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(95, 39)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 11
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(13, 155)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(260, 102)
		self._label6.TabIndex = 12
		self._label6.Text = "label6"
		# 
		# FormGeneral
		# 
		self.ClientSize = System.Drawing.Size(286, 267)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "FormGeneral"
		self.Text = "FormGeneral"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		Tick = int(self._textBox1.Text) 
		Tax = 0.06
		Total = 0
		Section = 100
		Taxt = 0
		TickC = 0
		if self._radioButton1.Checked:
			Section = 20
		elif self._radioButton2.Checked:
			Section = 15
		elif self._radioButton3.Checked:
			Section = 10
		Tax = 0.06
		TickC = Tick * Section
		TaxT = Tax * TickC
		
		self._label4.Text = "$" + str(TickC)
		self._label5.Text = "$" + str(TaxT)
		Total = Taxt + TickC
		self._label3.Text = "$" + str(Total)

	def Button2Click(self, sender, e):
		Application.Exit()

	def Label5Click(self, sender, e):
		pass