using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int numB = int.Parse(textBox1.Text);
            if (numB == 0)
                label2.Text = "You earned 0 points!";
            else if (numB > 0 && numB < 2)
                label2.Text = "You earned 5 points!";
            else if (numB > 1 && numB < 3)
                label2.Text = "You earned 15 points!";
            else if (numB > 2 && numB < 3)
                label2.Text = "You earned 30 points!";
        

            
        }
    }
}
