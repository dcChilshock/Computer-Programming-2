using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prog88a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Sum 
            label8.Text = " ";
            //differnce 
            label9.Text = " ";
            // average 
            label10.Text = " ";
            //abs distance
            label11.Text = " ";
            //max
            label12.Text = " ";
            //min
            label13.Text = " ";
            // product 
            label15.Text = " ";
            // text boxs 
            textBox1.Text = " ";
            textBox2.Text = " ";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int sum = num1 + num2;
            int diff = num1 - num2;
            double avg = (double)sum / 2.0;
            int product = num1 * num2;
            int abs = Math.Abs(diff);
            // math . max and math.min
            int max = 0;
            int min = 0;

            if (num1 > num2)
            {
                max = num1;
            } else {
                max = num2;
            }

            if (num1 <= num2)
                min = num1;
            else min = num2;
            //else if 

            label8.Text = sum.ToString();
            label9.Text = diff.ToString();
            label10.Text = avg.ToString();
            label11.Text = abs.ToString();
            label12.Text = max.ToString();
            label13.Text = min.ToString();
            label15.Text = product.ToString();

        }
    }
}
