import System.Drawing
import System.Windows.Forms
#import Form1
# form1 = Form1.Form1()
# from Form1 import Form1

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lavender
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(41, 46)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(452, 298)
		self._button1.TabIndex = 0
		self._button1.Text = "Show New Form"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DodgerBlue
		self.ClientSize = System.Drawing.Size(534, 417)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MultiForms"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Hello, World!")
		form1.Show()
		self.Hide()
		
		#from SecondForm import *
		#form2 = SecondForm()
		#form2.Show()