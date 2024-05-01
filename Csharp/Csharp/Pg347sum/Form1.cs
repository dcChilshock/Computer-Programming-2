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
namespace Pg347sum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int val = 0;
            string variable = Interaction.InputBox("Enter a positive integer value:", "title");
            MessageBox.Show(variable);
            for (int lcv = 0; lcv <= Int32.Parse(variable); lcv++)
            {
                val += lcv;
            }
            MessageBox.Show("The sum of numbers 1 through " + variable + " is " + val.ToString());
        }
    }
}
