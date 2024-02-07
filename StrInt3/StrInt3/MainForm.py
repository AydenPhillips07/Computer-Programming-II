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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Crimson
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(209, 57)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter a Word"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Crimson
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 119)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(209, 57)
		self._label2.TabIndex = 1
		self._label2.Text = "First Non-repeated Character"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Crimson
		self._label3.Location = System.Drawing.Point(342, 119)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(255, 57)
		self._label3.TabIndex = 2
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Crimson
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(342, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(255, 44)
		self._textBox1.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Crimson
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(53, 344)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 85)
		self._button1.TabIndex = 4
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Crimson
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(342, 344)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 85)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Crimson
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(642, 344)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(157, 85)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(893, 461)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "StrInt3"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		self._label1.Text = "Hi!"

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text.lower()
		for lcv in range(len(word)):
			for lcv2 in range(lcv+1, len(word)):
				letter = word[lcv]
				letter2 = word[lcv2]
				if letter != letter2:
					self._label3.Text += letter + " "

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()