namespace Prog122d
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
            textBox1.Text = " ";
            listBox1.Items.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double x = 0.0;
            double eq = 0;
            string y = " ";
            for (int lcv = -12; lcv <= 16; lcv++)
            {
                eq = (Math.Pow(x,6) + (-3*Math.Pow(x,50)) + (-93*Math.Pow(x, 4)) + (87*Math.Pow(x, 3)) + (1596*Math.Pow(x,2)) + (-1380*x) - 2800);
                listBox1.Items.Add(eq);
            }
                



        }
    }
}