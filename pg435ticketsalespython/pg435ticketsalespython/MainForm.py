import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label2 = System.Windows.Forms.Label()
		self._btngeneral = System.Windows.Forms.Button()
		self._btnstudent = System.Windows.Forms.Button()
		self._btnexit = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CornflowerBlue
		self._label2.Location = System.Drawing.Point(13, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(139, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Select Type of ticket sales:"
		# 
		# btngeneral
		# 
		self._btngeneral.BackColor = System.Drawing.Color.PowderBlue
		self._btngeneral.Location = System.Drawing.Point(13, 39)
		self._btngeneral.Name = "btngeneral"
		self._btngeneral.Size = System.Drawing.Size(159, 54)
		self._btngeneral.TabIndex = 2
		self._btngeneral.Text = "General Sales?"
		self._btngeneral.UseVisualStyleBackColor = False
		self._btngeneral.Click += self.BtngeneralClick
		# 
		# btnstudent
		# 
		self._btnstudent.BackColor = System.Drawing.Color.PowderBlue
		self._btnstudent.Location = System.Drawing.Point(13, 100)
		self._btnstudent.Name = "btnstudent"
		self._btnstudent.Size = System.Drawing.Size(159, 53)
		self._btnstudent.TabIndex = 3
		self._btnstudent.Text = "Student Sales?"
		self._btnstudent.UseVisualStyleBackColor = False
		self._btnstudent.Click += self.BtnstudentClick
		# 
		# btnexit
		# 
		self._btnexit.BackColor = System.Drawing.Color.PowderBlue
		self._btnexit.Location = System.Drawing.Point(13, 158)
		self._btnexit.Name = "btnexit"
		self._btnexit.Size = System.Drawing.Size(269, 47)
		self._btnexit.TabIndex = 4
		self._btnexit.Text = "Exit"
		self._btnexit.UseVisualStyleBackColor = False
		self._btnexit.Click += self.BtnexitClick
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Lavender
		self._label3.Location = System.Drawing.Point(178, 39)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 54)
		self._label3.TabIndex = 5
		self._label3.Text = "Ticket Sales to the general public."
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Lavender
		self._label4.Location = System.Drawing.Point(179, 100)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 53)
		self._label4.TabIndex = 6
		self._label4.Text = "Ticket Sales to the student body."
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSlateGray
		self.ClientSize = System.Drawing.Size(281, 213)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._btnexit)
		self.Controls.Add(self._btnstudent)
		self.Controls.Add(self._btngeneral)
		self.Controls.Add(self._label2)
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