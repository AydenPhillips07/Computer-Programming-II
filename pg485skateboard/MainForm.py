import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(149, 98)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(455, 55)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "$60        The Master Thrasher"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(149, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(426, 82)
		self._label1.TabIndex = 1
		self._label1.Text = "Pick a Deck Style"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(149, 159)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(455, 55)
		self._checkBox2.TabIndex = 2
		self._checkBox2.Text = "$45        The Dictator of Grind"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.Location = System.Drawing.Point(149, 220)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(455, 55)
		self._checkBox3.TabIndex = 3
		self._checkBox3.Text = "$50        The Street King"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(619, 208)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(169, 69)
		self._button1.TabIndex = 4
		self._button1.Text = "Next ->"
		self._button1.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(800, 307)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._checkBox1)
		self.Name = "MainForm"
		self.Text = "pg485skateboard"
		self.ResumeLayout(False)

