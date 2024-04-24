using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg266
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int numA = int.Parse(textBox1.Text);
            int numB = int.Parse(textBox2.Text);
            if (numA > numB)
                label4.Text = "Value A is larger than Value B";
            else if (numA < numB)
                label4.Text = "Value B is larger than Value A";
            else
                label4.Text = "Values are equal";
        }

        private void label2_Click(object sender, EventArgs e)
        {
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label4.Text = "";
            textBox1.Text = "";
            textBox2.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
