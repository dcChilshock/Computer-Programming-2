﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSalesCs
{
    public partial class Form2 : Form 
    {
        private Form myParent;

        public Form2()
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();

        }

        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }
        decimal decTAXRATE = 0.06m; // sales tax
        private decimal CalcTax(decimal cost)
        {
            // return the sales tax on ticket sales 
            return cost * decTAXRATE;
        }
    }
}
