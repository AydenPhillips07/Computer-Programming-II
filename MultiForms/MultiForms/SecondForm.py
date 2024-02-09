
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class SecondForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self.SuspendLayout()
		# 
		# SecondForm
		# 
		self.ClientSize = System.Drawing.Size(982, 468)
		self.Name = "SecondForm"
		self.Text = "SecondForm"
		self.ResumeLayout(False)

