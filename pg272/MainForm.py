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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Gold
		self._radioButton1.Location = System.Drawing.Point(25, 85)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(270, 40)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Daytime (6:00 am - 5:59 pm)"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.Gold
		self._radioButton2.Location = System.Drawing.Point(25, 131)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(270, 40)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening (6:00 pm - 11:59 pm)"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Gold
		self._radioButton3.Location = System.Drawing.Point(25, 177)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(270, 40)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off-Peak (12:00 am - 5:59 am)"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gold
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(25, 32)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(270, 40)
		self._label1.TabIndex = 3
		self._label1.Text = "Rate Category"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Gold
		self._label2.Location = System.Drawing.Point(555, 32)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(138, 40)
		self._label2.TabIndex = 4
		self._label2.Text = "Total Call Time (In Minutes)"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(555, 85)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(138, 38)
		self._textBox1.TabIndex = 5
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gold
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(339, 32)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(138, 40)
		self._label3.TabIndex = 8
		self._label3.Text = "Rate per Minute"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Gold
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(339, 85)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(138, 38)
		self._label4.TabIndex = 9
		self._label4.Text = "$0.07"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Gold
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(339, 131)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(138, 38)
		self._label5.TabIndex = 10
		self._label5.Text = "$0.12"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Gold
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(339, 177)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(138, 38)
		self._label6.TabIndex = 11
		self._label6.Text = "$0.05"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gold
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(25, 233)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(134, 76)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gold
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(25, 315)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(134, 76)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gold
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(165, 271)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(134, 76)
		self._button3.TabIndex = 14
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Gold
		self._label7.Location = System.Drawing.Point(508, 177)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(286, 214)
		self._label7.TabIndex = 15
		self._label7.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(815, 414)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "pg272"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		rate = 0.00
		mins = int(self._textBox1.Text)
		bill = rate * mins
		price = round(bill, 2)
		t = ""
		if RadioButton1.Checked: 
			rate = 0.07
			t = "DayTime"
		if RadioButton2.Checked:
			rate = 0.12
			t = "Evening"
		if RadioButton3.Checked: 
			rate = 0.05
			t = "Off-Peak"
		self._label7.Text = t + str(bill)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label7.Text = ""
		

	def Button3Click(self, sender, e):
		Application.Exit()

	

	def RadioButton1CheckedChanged(self, sender, e):
		pass

	def RadioButton2CheckedChanged(self, sender, e):
		pass

	def RadioButton3CheckedChanged(self, sender, e):
		pass