namespace Pg435TicketSalesCs
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

        private void button1_Click(object sender, EventArgs e)
        {
            // Form frm = new Form2(this); (very high level)
            Form2 frm = new Form2(this);
            frm.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            studentForm frm = new studentForm(this);
            frm.Show();
            this.Hide();
        }
    }
}