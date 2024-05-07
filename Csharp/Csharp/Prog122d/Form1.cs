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
            listBox1.Text = " ";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double x = 0.0;
            double eq = 0;
            string y = " ";
            for (int lcv = -12; lcv <= 16; lcv++)
                eq = (x**6) + (-3*x**50) + (-93*x**4) + (87*x**3) + (1596*x**2) + (-1380*x) - 2800;


        }
    }
}