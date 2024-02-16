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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Crimson
		self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(12, 78)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(294, 76)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "DayTime (6:00 a.m. through 5:59 P.M.)"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.Crimson
		self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(12, 160)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(294, 76)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening (6:00 p.m. through 11:59 P.M.)"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Crimson
		self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(12, 242)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(294, 76)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off-Peak (12:00 a.m. through 5:59 A.M.)"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Crimson
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(537, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(174, 76)
		self._label1.TabIndex = 3
		self._label1.Text = "Call Time (In Minutes)"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(537, 110)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(174, 44)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Crimson
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(342, 78)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(150, 76)
		self._label2.TabIndex = 5
		self._label2.Text = "$0.07"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Crimson
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(342, 160)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(150, 76)
		self._label3.TabIndex = 6
		self._label3.Text = "$0.12"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Crimson
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(342, 242)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(150, 76)
		self._label4.TabIndex = 7
		self._label4.Text = "$0.05"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Crimson
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 4)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(294, 61)
		self._label5.TabIndex = 8
		self._label5.Text = "Time of Day Call Took Place"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Crimson
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(342, 4)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(150, 61)
		self._label6.TabIndex = 9
		self._label6.Text = "Rates (Per Minute)"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Crimson
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(342, 332)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(174, 95)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Crimson
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(615, 332)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(174, 95)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Crimson
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(12, 332)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(294, 150)
		self._label7.TabIndex = 13
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(859, 491)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "pg272"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label6Click(self, sender, e):
		pass

	

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label7.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def RadioButton1CheckedChanged(self, sender, e):
		rate = 0.07
		tod = "Daytime:" 
			
		callt = int(self._textBox1.Text)
		if callt <= 0:
			self._label7.Text = "Invalid Input"
		else:
			price = float(callt * rate)
			price2 = int(price)
			self._label7.Text = tod + str(callt) + " Minutes $" + str(price2)

	def RadioButton2CheckedChanged(self, sender, e):
		rate = 0.12
		tod = "Evening: "
		callt = int(self._textBox1.Text)
		if callt <= 0:
			self._label7.Text = "Invalid Input"
		else:
			price = float(callt * rate)
			self._label7.Text = tod + str(callt) + " Minutes $" + str(price)

	def RadioButton3CheckedChanged(self, sender, e):
		rate = 0.05
		tod = "Off-Peak: "
		callt = int(self._textBox1.Text)
		if callt <= 0:
			self._label7.Text = "Invalid Input"
		else:
			price = float(callt * rate)
			self._label7.Text = tod + str(callt) + " Minutes $" + str(price)