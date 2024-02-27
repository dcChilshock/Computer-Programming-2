
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class FormStudent(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent 
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "How many tickets?"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(118, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(103, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 38)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(152, 58)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(170, 38)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(103, 58)
		self._button2.TabIndex = 3
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(65, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(81, 23)
		self._label2.TabIndex = 4
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(65, 124)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(84, 23)
		self._label3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(62, 147)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(84, 23)
		self._label4.TabIndex = 6
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 101)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(47, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Tickets:"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(30, 124)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(29, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "Tax:"
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(21, 147)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(38, 23)
		self._label7.TabIndex = 9
		self._label7.Text = "Total:"
		# 
		# FormStudent
		# 
		self.ClientSize = System.Drawing.Size(285, 210)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "FormStudent"
		self.Text = "FormStudent"
		self.Load += self.FormStudentLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	

	def FormStudentLoad(self, sender, e):
		pass
	

	def Button1Click(self, sender, e):
		Tick = int(self._textBox1.Text)
		TickC = Tick * 7
		TaxRate = 0.06
		Tax = TickC * TaxRate
		Total = round(TickC + Tax, 2)
		self._label2.Text = "$" + str(TickC)
		self._label3.Text = "$" + str(Tax)
		self._label4.Text = "$" + str(Total)

	def Button2Click(self, sender, e):
		Application.Exit()

	def Label4Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass