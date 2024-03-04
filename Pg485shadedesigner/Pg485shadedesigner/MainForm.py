import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._checkedListBox1 = System.Windows.Forms.CheckedListBox()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(12, 70)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Regular"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(12, 100)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Folding "
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(12, 130)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Roman"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(105, 70)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(104, 24)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "25 inches"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(105, 100)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(104, 24)
		self._radioButton5.TabIndex = 4
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "27 inches"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(105, 131)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(104, 24)
		self._radioButton6.TabIndex = 5
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "32 inches"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(105, 162)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(104, 24)
		self._radioButton7.TabIndex = 6
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "40 inches"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(13, 218)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(104, 24)
		self._radioButton8.TabIndex = 7
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "Natural"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(13, 249)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(104, 24)
		self._radioButton9.TabIndex = 8
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "Blue "
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(8, 279)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(104, 24)
		self._radioButton10.TabIndex = 9
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "Teal"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# radioButton11
		# 
		self._radioButton11.Location = System.Drawing.Point(8, 309)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(104, 24)
		self._radioButton11.TabIndex = 10
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "Red "
		self._radioButton11.UseVisualStyleBackColor = True
		# 
		# radioButton12
		# 
		self._radioButton12.Location = System.Drawing.Point(8, 339)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(104, 24)
		self._radioButton12.TabIndex = 11
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "Green"
		self._radioButton12.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(189, 39)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(189, 74)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(189, 103)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 14
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 44)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(112, 23)
		self._label1.TabIndex = 15
		self._label1.Text = "Types of shades"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(105, 44)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(63, 23)
		self._label2.TabIndex = 16
		self._label2.Text = "How wide?"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 191)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 17
		self._label3.Text = "What color"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(105, 202)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 18
		self._label4.Text = "Cost:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(105, 223)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 19
		self._label5.Text = "label5"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(12, 13)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 20
		self._label6.Text = "Shade Designer"
		# 
		# checkedListBox1
		# 
		self._checkedListBox1.FormattingEnabled = True
		self._checkedListBox1.Location = System.Drawing.Point(123, 267)
		self._checkedListBox1.Name = "checkedListBox1"
		self._checkedListBox1.Size = System.Drawing.Size(120, 94)
		self._checkedListBox1.TabIndex = 21
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(282, 373)
		self.Controls.Add(self._checkedListBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._radioButton12)
		self.Controls.Add(self._radioButton11)
		self.Controls.Add(self._radioButton10)
		self.Controls.Add(self._radioButton9)
		self.Controls.Add(self._radioButton8)
		self.Controls.Add(self._radioButton7)
		self.Controls.Add(self._radioButton6)
		self.Controls.Add(self._radioButton5)
		self.Controls.Add(self._radioButton4)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "Pg485shadedesigner"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label5.Text = " "

	def Label5Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		SD = 0
		SS = 0
		SC = 0
		Color = 0
		Design = 0
		Size = 0 
		if self._radioButton1.Checked == True:
			SD = 0
			Design = "Regular"
		elif self._radioButton2.Checked == True:
			SD = 10
			Design = "Folding"			
		elif self._radioButton3.Checked == True:
			SD = 15
			Design = "Roman"
			
		
		if self._radioButton4.Checked == True:
			SS = 0
			Size = 25
		elif self._radioButton5.Checked == True:
			SS = 2
			Size = 27
		elif self._radioButton6.Checked == True:
			SS = 4
			Size = 32
		elif self._radioButton7.Checked == True:
			SS = 6
			Size = 40
		else:
			SD = 0
			SS = 0 
			SC = 0
	
		if self._radioButton8.Checked == True:
			SC = 5
			Color = "Natural"
		elif self._radioButton9.Checked == True:
			SC = 0
			Color = "Blue"
		elif self._radioButton10.Checked == True:
			SC = 0
			Color = "Teal"
		elif self._radioButton11.Checked == True:
			SC = 0
			Color = "Red" 
		elif self._radioButton12.Checked == True:
			SC = 0
			Color = "Green"
			
		Cost = SC + SD + SS
		self._label5.Text = str(Cost)