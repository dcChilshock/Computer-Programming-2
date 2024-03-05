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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self._checkBox6 = System.Windows.Forms.CheckBox()
		self._checkBox7 = System.Windows.Forms.CheckBox()
		self._checkBox8 = System.Windows.Forms.CheckBox()
		self._checkBox9 = System.Windows.Forms.CheckBox()
		self._checkBox10 = System.Windows.Forms.CheckBox()
		self._checkBox11 = System.Windows.Forms.CheckBox()
		self._checkBox12 = System.Windows.Forms.CheckBox()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(199, 44)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(199, 70)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(199, 99)
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
		self._label2.Location = System.Drawing.Point(8, 197)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(63, 23)
		self._label2.TabIndex = 16
		self._label2.Text = "How wide?"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(105, 44)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(88, 23)
		self._label3.TabIndex = 17
		self._label3.Text = "What color"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(137, 254)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 18
		self._label4.Text = "Cost:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(137, 277)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 19
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
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(13, 70)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(83, 24)
		self._checkBox1.TabIndex = 21
		self._checkBox1.Text = "Regular"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(13, 100)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(83, 24)
		self._checkBox2.TabIndex = 22
		self._checkBox2.Text = "Folding"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(13, 131)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 23
		self._checkBox3.Text = "Roman"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Location = System.Drawing.Point(8, 223)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(104, 24)
		self._checkBox4.TabIndex = 24
		self._checkBox4.Text = "25"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox5
		# 
		self._checkBox5.Location = System.Drawing.Point(8, 253)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(104, 24)
		self._checkBox5.TabIndex = 25
		self._checkBox5.Text = "27"
		self._checkBox5.UseVisualStyleBackColor = True
		# 
		# checkBox6
		# 
		self._checkBox6.Location = System.Drawing.Point(8, 283)
		self._checkBox6.Name = "checkBox6"
		self._checkBox6.Size = System.Drawing.Size(104, 24)
		self._checkBox6.TabIndex = 26
		self._checkBox6.Text = "32"
		self._checkBox6.UseVisualStyleBackColor = True
		# 
		# checkBox7
		# 
		self._checkBox7.Location = System.Drawing.Point(8, 313)
		self._checkBox7.Name = "checkBox7"
		self._checkBox7.Size = System.Drawing.Size(104, 24)
		self._checkBox7.TabIndex = 27
		self._checkBox7.Text = "40"
		self._checkBox7.UseVisualStyleBackColor = True
		# 
		# checkBox8
		# 
		self._checkBox8.Location = System.Drawing.Point(101, 72)
		self._checkBox8.Name = "checkBox8"
		self._checkBox8.Size = System.Drawing.Size(92, 24)
		self._checkBox8.TabIndex = 28
		self._checkBox8.Text = "Natural"
		self._checkBox8.UseVisualStyleBackColor = True
		# 
		# checkBox9
		# 
		self._checkBox9.Location = System.Drawing.Point(101, 102)
		self._checkBox9.Name = "checkBox9"
		self._checkBox9.Size = System.Drawing.Size(82, 24)
		self._checkBox9.TabIndex = 29
		self._checkBox9.Text = "Blue"
		self._checkBox9.UseVisualStyleBackColor = True
		# 
		# checkBox10
		# 
		self._checkBox10.Location = System.Drawing.Point(101, 131)
		self._checkBox10.Name = "checkBox10"
		self._checkBox10.Size = System.Drawing.Size(92, 24)
		self._checkBox10.TabIndex = 30
		self._checkBox10.Text = "Teal"
		self._checkBox10.UseVisualStyleBackColor = True
		# 
		# checkBox11
		# 
		self._checkBox11.Location = System.Drawing.Point(101, 161)
		self._checkBox11.Name = "checkBox11"
		self._checkBox11.Size = System.Drawing.Size(88, 24)
		self._checkBox11.TabIndex = 31
		self._checkBox11.Text = "red"
		self._checkBox11.UseVisualStyleBackColor = True
		# 
		# checkBox12
		# 
		self._checkBox12.Location = System.Drawing.Point(101, 186)
		self._checkBox12.Name = "checkBox12"
		self._checkBox12.Size = System.Drawing.Size(104, 24)
		self._checkBox12.TabIndex = 32
		self._checkBox12.Text = "green"
		self._checkBox12.UseVisualStyleBackColor = True
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(101, 9)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(169, 27)
		self._label7.TabIndex = 33
		self._label7.Text = "Select 1 out of each category"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(282, 373)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._checkBox12)
		self.Controls.Add(self._checkBox11)
		self.Controls.Add(self._checkBox10)
		self.Controls.Add(self._checkBox9)
		self.Controls.Add(self._checkBox8)
		self.Controls.Add(self._checkBox7)
		self.Controls.Add(self._checkBox6)
		self.Controls.Add(self._checkBox5)
		self.Controls.Add(self._checkBox4)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
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
		if self._checkBox1.Checked == True:
			SD = 0
			Design = "Regular"
		elif self._checkBox2.Checked == True:
			SD = 10
			Design = "Folding"			
		elif self._checkBox3.Checked == True:
			SD = 15
			Design = "Roman"
			
		
		if self._checkBox4.Checked == True:
			SS = 0
			Size = 25
		elif self._checkBox5.Checked == True:
			SS = 2
			Size = 27
		elif self._checkBox6.Checked == True:
			SS = 4
			Size = 32
		elif self._checkBox7.Checked == True:
			SS = 6
			Size = 40
		else:
			SD = 0
			SS = 0 
			SC = 0
	
		if self._checkBox8.Checked == True:
			SC = 5
			Color = "Natural"
		elif self._checkBox9.Checked == True:
			SC = 0
			Color = "Blue"
		elif self._checkBox10.Checked == True:
			SC = 0
			Color = "Teal"
		elif self._checkBox11.Checked == True:
			SC = 0
			Color = "Red" 
		elif self._checkBox12.Checked == True:
			SC = 0
			Color = "Green"
			
		Cost = SC + SD + SS
		self._label5.Text = str(Cost)
