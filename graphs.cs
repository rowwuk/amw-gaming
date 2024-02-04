using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Windows.Forms.DataVisualization.Charting;
using System.Reflection;

namespace pprojekt2
{
    
    public partial class Form1 : Form
    {
        int[] CNT= new int[500];
        int reach = 0;
        private void buttonColor_Click(object sender, EventArgs e)
        {
            //Funkcja zmieniająca kolor histogramu
            string selected = colorSelector.Text;
            switch(selected)
            {
                case "Zielony":
                    histogram.Palette = ChartColorPalette.Bright;
                    break;
                case "Szary":
                    histogram.Palette = ChartColorPalette.Grayscale;
                    break;
                case "Fioletowy":
                    histogram.Palette = ChartColorPalette.Excel;
                    break;
                default:
                    histogram.Palette = ChartColorPalette.None;
                    break;
            }
        }

        private void buttonThickness_Click(object sender, EventArgs e)
        {
            //funkcja zmieniająca rodzaj wykresu
            string thickselected = ThickSelector.Text;

            switch(thickselected)
            {
                case "Wykres Poziomy":
                    histogram.Series["Ilosc ocen"].ChartType = SeriesChartType.StackedBar;
                    break;
                case "Wykres Punktowy":
                    histogram.Series["Ilosc ocen"].ChartType = SeriesChartType.Point;
                    break;
                case "Wykres Kolumnowy":
                    histogram.Series["Ilosc ocen"].ChartType = SeriesChartType.Column;
                    break;
                default:
                    histogram.Series["Ilosc ocen"].ChartType = SeriesChartType.Column;
                    break;
            }

        }

        private void BgButton_Click(object sender, EventArgs e)
        {
            string bgselected = BgSelector.Text;

            switch (bgselected)
            {
                case "Gradient Prawo do Lewo":
                    histogram.Series["Ilosc ocen"].BackGradientStyle = GradientStyle.LeftRight;
                    break;
                case "Gradient na środku":
                    histogram.Series["Ilosc ocen"].BackGradientStyle = GradientStyle.Center;
                    break;
                case "Wykres kreskowany":
                    histogram.Series["Ilosc ocen"].BackHatchStyle = ChartHatchStyle.Cross;
                    break;
                case "Wykres domyślny":
                    histogram.Series["Ilosc ocen"].BackHatchStyle = ChartHatchStyle.None;
                    histogram.Series["Ilosc ocen"].BackGradientStyle = GradientStyle.None;
                    break;
                default:
                    histogram.Series["Ilosc ocen"].BackHatchStyle = ChartHatchStyle.None;
                    histogram.Series["Ilosc ocen"].BackGradientStyle = GradientStyle.None;
                    break;
            }
        }

        private void hisbutton_Click(object sender, EventArgs e)
        {
            hisbutton.Enabled = false;
            for (int i = 0; i < reach; i++)
            {
                string pole = "ilosc ocen " + i + " - " + (i + 1) + " "; 

                this.histogram.Series["Ilosc ocen"].Points.AddXY(pole, CNT[i]);
            }
        }
        
        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            //Wyczyść histogram przed załadowaniem pliku
            foreach (var series in histogram.Series)
            {
                series.Points.Clear();
            }

            var fileStream = openFileDialog1.OpenFile();
            
            StreamReader reader = new StreamReader(fileStream);
            string t = reader.ReadToEnd().Trim();
            int[] Qiu = t.Split(',').Select(int.Parse).ToArray();
            // System.Windows.Forms.MessageBox.Show(t);
            richTextBox1.Text = t + "\n\n";
            int counter;
            
            for (int i = 0; i < Qiu.Length; i++)
            {
                if (Qiu[i] > reach)
                {
                    reach=Qiu[i];
                }
                counter=Qiu[i];
                CNT[counter]++;
                if (counter!=0)
                {
                    CNT[counter - 1]++;
                }
            }
            for (int i = 0; i < reach; i++)
            {
                richTextBox1.AppendText("ilosc ocen " + i + " - " + (i + 1) + " " + CNT[i] + "\n");
            }
            try
           {
                richTextBox1.SaveFile("../../../wyniki.txt", RichTextBoxStreamType.PlainText);
           }
           catch (IOException errorfile)
           {
                string bufor = errorfile.ToString();
                System.Windows.Forms.MessageBox.Show("Wykryto nastepujacy problem System.IO.IOException: Proces nie może uzyskac dostepu do pliku");
           }
            System.Windows.Forms.MessageBox.Show("Pomyślnie otworzono plik");

            //Włacz przyciski po otworzeiu pliku
            hisbutton.Enabled = true;
            buttonColor.Enabled = true;
            colorSelector.Enabled = true;
            buttonThickness.Enabled = true;
            ThickSelector.Enabled = true;
            BgButton.Enabled = true;
            BgSelector.Enabled = true;
        }
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
        }
    }
}
