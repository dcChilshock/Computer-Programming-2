import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._FileMenu = System.Windows.Forms.ToolStripMenuItem()
		self._ColorMenu = System.Windows.Forms.ToolStripMenuItem()
		self._HelpMenu = System.Windows.Forms.ToolStripMenuItem()
		self._AboutMenu = System.Windows.Forms.ToolStripMenuItem()
		self._RedMenu = System.Windows.Forms.ToolStripMenuItem()
		self._GreenMenu = System.Windows.Forms.ToolStripMenuItem()
		self._BlackMenu = System.Windows.Forms.ToolStripMenuItem()
		self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._BlueMenu = System.Windows.Forms.ToolStripMenuItem()
		self._label1 = System.Windows.Forms.Label()
		self._toolStripSeparator1 = System.Windows.Forms.ToolStripSeparator()
		self._visiableToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._toolStripSeparator2 = System.Windows.Forms.ToolStripSeparator()
		self._hEHEHEHHEHEHToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._FileMenu,
			self._ColorMenu,
			self._HelpMenu]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(284, 24)
		self._menuStrip1.TabIndex = 0
		self._menuStrip1.Text = "menuStrip1"
		# 
		# FileMenu
		# 
		self._FileMenu.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._exitToolStripMenuItem]))
		self._FileMenu.Name = "FileMenu"
		self._FileMenu.Size = System.Drawing.Size(37, 20)
		self._FileMenu.Text = "File"
		# 
		# ColorMenu
		# 
		self._ColorMenu.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._RedMenu,
			self._GreenMenu,
			self._BlackMenu,
			self._BlueMenu,
			self._toolStripSeparator1,
			self._visiableToolStripMenuItem,
			self._toolStripSeparator2,
			self._hEHEHEHHEHEHToolStripMenuItem]))
		self._ColorMenu.Name = "ColorMenu"
		self._ColorMenu.Size = System.Drawing.Size(48, 20)
		self._ColorMenu.Text = "Color"
		# 
		# HelpMenu
		# 
		self._HelpMenu.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._AboutMenu]))
		self._HelpMenu.Name = "HelpMenu"
		self._HelpMenu.Size = System.Drawing.Size(44, 20)
		self._HelpMenu.Text = "Help"
		# 
		# AboutMenu
		# 
		self._AboutMenu.Name = "AboutMenu"
		self._AboutMenu.Size = System.Drawing.Size(152, 22)
		self._AboutMenu.Text = "About"
		# 
		# RedMenu
		# 
		self._RedMenu.Name = "RedMenu"
		self._RedMenu.Size = System.Drawing.Size(167, 22)
		self._RedMenu.Text = "Red"
		self._RedMenu.Click += self.RedMenuClick
		# 
		# GreenMenu
		# 
		self._GreenMenu.Name = "GreenMenu"
		self._GreenMenu.Size = System.Drawing.Size(167, 22)
		self._GreenMenu.Text = "Green"
		self._GreenMenu.Click += self.GreenMenuClick
		# 
		# BlackMenu
		# 
		self._BlackMenu.Name = "BlackMenu"
		self._BlackMenu.Size = System.Drawing.Size(167, 22)
		self._BlackMenu.Text = "Black"
		self._BlackMenu.Click += self.BlackMenuClick
		# 
		# exitToolStripMenuItem
		# 
		self._exitToolStripMenuItem.Name = "exitToolStripMenuItem"
		self._exitToolStripMenuItem.Size = System.Drawing.Size(93, 22)
		self._exitToolStripMenuItem.Text = "Exit"
		self._exitToolStripMenuItem.Click += self.ExitToolStripMenuItemClick
		# 
		# BlueMenu
		# 
		self._BlueMenu.Name = "BlueMenu"
		self._BlueMenu.Size = System.Drawing.Size(167, 22)
		self._BlueMenu.Text = "Blue"
		self._BlueMenu.Click += self.BlueMenuClick
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
		# toolStripSeparator1
		# 
		self._toolStripSeparator1.Name = "toolStripSeparator1"
		self._toolStripSeparator1.Size = System.Drawing.Size(164, 6)
		# 
		# visiableToolStripMenuItem
		# 
		self._visiableToolStripMenuItem.Name = "visiableToolStripMenuItem"
		self._visiableToolStripMenuItem.Size = System.Drawing.Size(167, 22)
		self._visiableToolStripMenuItem.Text = "Visiable"
		self._visiableToolStripMenuItem.Click += self.VisiableToolStripMenuItemClick
		# 
		# toolStripSeparator2
		# 
		self._toolStripSeparator2.Name = "toolStripSeparator2"
		self._toolStripSeparator2.Size = System.Drawing.Size(164, 6)
		# 
		# hEHEHEHHEHEHToolStripMenuItem
		# 
		self._hEHEHEHHEHEHToolStripMenuItem.Name = "hEHEHEHHEHEHToolStripMenuItem"
		self._hEHEHEHHEHEHToolStripMenuItem.Size = System.Drawing.Size(167, 22)
		self._hEHEHEHHEHEHToolStripMenuItem.Text = "HEHEHEHHEHEH"
		self._hEHEHEHHEHEHToolStripMenuItem.Click += self.HEHEHEHHEHEHToolStripMenuItemClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "Pg447MenuDemo"
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def ExitToolStripMenuItemClick(self, sender, e):
		Application.Exit()



	def RedMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Red

	def GreenMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Green

	def HEHEHEHHEHEHToolStripMenuItemClick(self, sender, e):
		self._label1.ForeColor = Color.Yellow
		

	def BlackMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Black

	def BlueMenuClick(self, sender, e):
		self._label1.ForeColor = Color.Blue

	def VisiableToolStripMenuItemClick(self, sender, e):
		if self._VisiableToolStripMenuItem.Checked == True:
			self._label1.Visible = True
		if self._VisiableToolStripMenuItem.Checked == False:
			self._label1.Visible = False
		