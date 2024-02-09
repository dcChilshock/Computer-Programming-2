
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class electricboogalo2(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(154, 117)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(192, 103)
		self._button1.TabIndex = 0
		self._button1.Text = "go home form"
		self._button1.UseVisualStyleBackColor = True
		# 
		# electricboogalo2
		# 
		self.ClientSize = System.Drawing.Size(502, 400)
		self.Controls.Add(self._button1)
		self.Name = "electricboogalo2"
		self.Text = "electricboogalo2"
		self.ResumeLayout(False)

