using System;
using System.Diagnostics;
using System.IO;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 4)
            {
                throw new ArgumentException("Invalid number of cli arguments");
            }

            cuvis_net.General.Init(args[0]);


            var general_setting_envi = new cuvis_net.GeneralExportSettings(args[3] +"/envi", "all", 1.0, 0.0, cuvis_net.PanSharpeningInterpolationType.NearestNeighbour, cuvis_net.PanSharpeningAlgorithm.Noop, false, false, false, 1);

            var general_setting_single = new cuvis_net.GeneralExportSettings(args[3] + "/single", "all", 1.0, 0.0, cuvis_net.PanSharpeningInterpolationType.NearestNeighbour, cuvis_net.PanSharpeningAlgorithm.Noop, false, false, false, 1);

            var general_setting_multi = new cuvis_net.GeneralExportSettings(args[3] + "/multi", "all", 1.0, 0.0, cuvis_net.PanSharpeningInterpolationType.NearestNeighbour, cuvis_net.PanSharpeningAlgorithm.Noop, false, false, false, 1);

            var general_setting_view = new cuvis_net.GeneralExportSettings(args[3] + "/view", "all", 1.0, 0.0, cuvis_net.PanSharpeningInterpolationType.NearestNeighbour, cuvis_net.PanSharpeningAlgorithm.Noop, false, false, false, 1);

            Console.WriteLine("Example 03 export measurement");

            Console.WriteLine("loading user settings...");
            cuvis_net.General.Init(args[0]);

            Console.WriteLine("loading session...");
            var sess = new cuvis_net.SessionFile(args[1]);

            Console.WriteLine("loading measurement...");
            cuvis_net.Measurement mesu = sess.GetMeasurement(0);
            Debug.Assert(mesu.GetHashCode() != null, " No data found");

            Debug.Assert((mesu.ProcessingMode != cuvis_net.ProcessingMode.Preview));


            Console.WriteLine("Export to Envi");
            var enviExporter = new cuvis_net.EnviExporter(general_setting_envi);
            enviExporter.Apply(mesu);

            Console.WriteLine("Export to Multi-Channel Tiff");
            var multi_tiff_settings = new cuvis_net.TiffExportSettings(cuvis_net.TiffCompressionMode.None, cuvis_net.TiffFormat.MultiChannel);
            var multiTiffExporter = new cuvis_net.TiffExporter(general_setting_multi, multi_tiff_settings);
            multiTiffExporter.Apply(mesu);

            Console.WriteLine("Export to separate Tiffs");
            var single_tiff_settings = new cuvis_net.TiffExportSettings(cuvis_net.TiffCompressionMode.None, cuvis_net.TiffFormat.Single);
            var singleTiffExporter = new cuvis_net.TiffExporter(general_setting_single, single_tiff_settings);
            singleTiffExporter.Apply(mesu);

            Console.WriteLine("Export View to file");

            string userpluginCai = string.Empty;
            using (StreamReader sr = new StreamReader(args[2]))
            {
                string line;
                // Read and display lines from the file until the end of
                // the file is reached.
                while ((line = sr.ReadLine()) != null)
                {
                    userpluginCai += line;
                }
            }

            var view_export_settings = new cuvis_net.ViewExportSettings(userpluginCai);
            var viewExporter = new cuvis_net.ViewExporter(general_setting_view, view_export_settings);
            viewExporter.Apply(mesu);
            Console.WriteLine("finished.");

        }
    }
}
