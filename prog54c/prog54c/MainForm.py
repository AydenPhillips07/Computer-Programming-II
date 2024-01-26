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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleTurquoise
		self._button1.Location = System.Drawing.Point(623, 112)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(116, 56)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleTurquoise
		self._button2.Location = System.Drawing.Point(623, 195)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(116, 56)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleTurquoise
		self._button3.Location = System.Drawing.Point(623, 291)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(116, 56)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DodgerBlue
		self._label1.Location = System.Drawing.Point(30, 25)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(192, 94)
		self._label1.TabIndex = 3
		self._label1.Text = "Radius"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DodgerBlue
		self._label2.Location = System.Drawing.Point(30, 176)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(503, 94)
		self._label2.TabIndex = 4
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DodgerBlue
		self._label3.Location = System.Drawing.Point(30, 291)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(503, 94)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(259, 48)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(255, 38)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkTurquoise
		self.ClientSize = System.Drawing.Size(848, 394)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = 3.14159
		radius = float(self._textBox1.Text)
		area = pi * radius ** 2
		circumference = 2 * pi * radius
		a2 = round(area, 3)
		c2 = round(circumference, 3)
		self._label2.Text = "Area: " + str(a2)
		self._label3.Text = "Circumference: " + str(c2)

	def Button2Click(self, sender, e):
		self._label2.Text = ""
		self._label3.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()