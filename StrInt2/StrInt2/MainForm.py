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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Black
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Crimson
		self._button1.Location = System.Drawing.Point(59, 252)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(131, 88)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Black
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Crimson
		self._button2.Location = System.Drawing.Point(369, 252)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(131, 88)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Black
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Crimson
		self._button3.Location = System.Drawing.Point(697, 252)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(131, 88)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Crimson
		self._label1.Location = System.Drawing.Point(25, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(198, 75)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Text:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Black
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Crimson
		self._label2.Location = System.Drawing.Point(25, 113)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(198, 75)
		self._label2.TabIndex = 4
		self._label2.Text = "Anagrams?"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Crimson
		self._label3.Location = System.Drawing.Point(257, 113)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(387, 75)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Black
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.Crimson
		self._textBox1.Location = System.Drawing.Point(257, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(167, 44)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Black
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.Crimson
		self._textBox2.Location = System.Drawing.Point(477, 19)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(167, 44)
		self._textBox2.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Crimson
		self.ClientSize = System.Drawing.Size(881, 503)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "StrInt2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text
		anagram = self._textBox2.Text
		word = word.lower()
		anagram = anagram.lower()
		if len(word) != len(anagram):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = anagram.index(c)
				
				if index != -1:
					anagram = anagram[0:index] + anagram[index+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(anagram) == 0
			

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		pass