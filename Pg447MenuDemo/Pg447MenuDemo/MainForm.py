import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 141)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(260, 111)
		self._label1.TabIndex = 1
		self._label1.Text = "Hello world!"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg447MenuDemo"
		self.ResumeLayout(False)


	def ExitToolStripMenuItemClick(self, sender, e):
		Application.Exit()



	def RedMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Red

	def GreenMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Green

	def HEHEHEHHEHEHToolStripMenuItemClick(self, sender, e):
		self._label1.ForeColor = Color.Yellow
		self.BackColor = Color.Gold

	def BlackMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Black

	def BlueMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Blue

	def VisiableToolStripMenuItemClick(self, sender, e):
		self._label1.Visible = not self._label1.Visible
		
		

	def AboutMenuClick(self, sender, e):
		self._label1.Text = "Menu system demo\n Designed for starting out with windows form applications about menu form."