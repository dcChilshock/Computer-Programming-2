import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._btngeneral = System.Windows.Forms.Button()
		self._btnstudent = System.Windows.Forms.Button()
		self._btnexit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(42, 278)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(261, 118)
		self._label1.TabIndex = 0
		self._label1.Text = """Section A = 20 dollars
section b = 15 dollars 
section c = 10 dollars
Student section = 7 dollars"""
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(155, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Select Type of ticket sales:"
		# 
		# btngeneral
		# 
		self._btngeneral.Location = System.Drawing.Point(12, 39)
		self._btngeneral.Name = "btngeneral"
		self._btngeneral.Size = System.Drawing.Size(159, 54)
		self._btngeneral.TabIndex = 2
		self._btngeneral.Text = "General Sales?"
		self._btngeneral.UseVisualStyleBackColor = True
		self._btngeneral.Click += self.BtngeneralClick
		# 
		# btnstudent
		# 
		self._btnstudent.Location = System.Drawing.Point(12, 99)
		self._btnstudent.Name = "btnstudent"
		self._btnstudent.Size = System.Drawing.Size(159, 53)
		self._btnstudent.TabIndex = 3
		self._btnstudent.Text = "Student Sales?"
		self._btnstudent.UseVisualStyleBackColor = True
		self._btnstudent.Click += self.BtnstudentClick
		# 
		# btnexit
		# 
		self._btnexit.Location = System.Drawing.Point(42, 158)
		self._btnexit.Name = "btnexit"
		self._btnexit.Size = System.Drawing.Size(75, 23)
		self._btnexit.TabIndex = 4
		self._btnexit.Text = "Exit"
		self._btnexit.UseVisualStyleBackColor = True
		self._btnexit.Click += self.BtnexitClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(458, 405)
		self.Controls.Add(self._btnexit)
		self.Controls.Add(self._btnstudent)
		self.Controls.Add(self._btngeneral)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg435ticketsalespython"
		self.ResumeLayout(False)

	def BtnstudentClick(self, sender, e):
		from FormStudent import * 
		formStudent = FormStudent(self) 
		formStudent.Show()
		self.Hide()

	def BtngeneralClick(self, sender, e):
		from FormGeneral import * 
		formGeneral = FormGeneral(self) 
		formGeneral.Show()
		self.Hide()

	def BtnexitClick(self, sender, e):
		Application.Exit()