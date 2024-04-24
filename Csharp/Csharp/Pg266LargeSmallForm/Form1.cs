using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg266LargeSmallForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label4.Text = " ";
            textBox1.Text = " ";
            textBox2.Text = " ";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            string str = " ";
            if (num > num2)
                str = "Value A is greater than Value B";
            else if (num < num2)
                str = "Value A is lesser than Value B";
            else if (num = num2)
                str = "Value A is equal to Value B";
            else
                str = "Error";

            label4.Text = str;

        }
    }
}
