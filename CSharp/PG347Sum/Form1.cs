using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;



namespace PG347Sum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int variable = int.Parse(Interaction.InputBox("Enter a positive integer", "Input Needed"));
            int sum = 0;
            for (int lcv = 0; lcv <= variable; lcv++) {
                sum += lcv;
            }
               
                
                
            MessageBox.Show(sum.ToString());
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
