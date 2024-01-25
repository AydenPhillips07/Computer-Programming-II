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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Ivory
		self._label1.Location = System.Drawing.Point(38, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(181, 104)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Four 3 Digit Numbers"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Ivory
		self._label2.Location = System.Drawing.Point(67, 130)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 51)
		self._label2.TabIndex = 1
		self._label2.Text = "Number 1"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Ivory
		self._label3.Location = System.Drawing.Point(67, 205)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 51)
		self._label3.TabIndex = 2
		self._label3.Text = "Number 2"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Ivory
		self._label4.Location = System.Drawing.Point(67, 277)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(125, 51)
		self._label4.TabIndex = 3
		self._label4.Text = "Number 3"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Ivory
		self._label5.Location = System.Drawing.Point(67, 349)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(125, 51)
		self._label5.TabIndex = 4
		self._label5.Text = "Number 4"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Ivory
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(543, 9)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(279, 119)
		self._label6.TabIndex = 5
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Ivory
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(543, 137)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(279, 119)
		self._label7.TabIndex = 6
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(252, 130)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(217, 47)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(252, 205)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(217, 47)
		self._textBox2.TabIndex = 8
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(252, 277)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(217, 47)
		self._textBox3.TabIndex = 9
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(252, 349)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(217, 47)
		self._textBox4.TabIndex = 10
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Ivory
		self._button1.Location = System.Drawing.Point(543, 269)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(130, 67)
		self._button1.TabIndex = 11
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Ivory
		self._button2.Location = System.Drawing.Point(679, 269)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(130, 67)
		self._button2.TabIndex = 12
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Ivory
		self._button3.Location = System.Drawing.Point(543, 342)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(266, 67)
		self._button3.TabIndex = 13
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.ForestGreen
		self.ClientSize = System.Drawing.Size(879, 418)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		sum = num1 + num2 + num3 + num4
		avg = sum / 4
		self._label6.Text = "The sum of the four numbers is: " + str(sum)
		self._label7.Text = "The average of the four numbers is: " + str(avg)

	def Button1Click(self, sender, e):
		self._label6.Text = ""
		self._label7.text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()