using System;
using System.Drawing;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 5)
            {
                throw new ArgumentException("Invalid number of cli arguments");
            }

            Console.WriteLine("Example 05 record single images");

            Console.WriteLine("loading user settings...");
            cuvis_net.General.Init(args[0]);

            Console.WriteLine("loading Calibration and processing context...");
            var calibration = new cuvis_net.Calibration(args[1]);
            var processingContext = new cuvis_net.ProcessingContext(calibration);
            var acquistionContext = new cuvis_net.AcquistionContext(calibration);

            var general_settings = new cuvis_net.GeneralExportSettings(args[3], "all", 1.0, 0.0, cuvis_net.PanSharpeningInterpolationType.NearestNeighbour, cuvis_net.PanSharpeningAlgorithm.Noop, false, false, false, 1);

            var sa = cuvis_net.CubertSaveArgs.Default;
            sa.AllowDrop= true;
            sa.AllowOverride = true;
            sa.AllowSessionFile = true;

            var cubeExporter = new cuvis_net.CubeExporter(general_settings, sa);

            Console.WriteLine("Waiting for camera to become online");
            for (; ; )
            {
                var state = acquistionContext.State;
                if (state == cuvis_net.HardwareState.Online)
                {
                    Console.WriteLine("Camera online");
                    break;
                }
                if (state == cuvis_net.HardwareState.PartiallyOnline)
                {
                    Console.WriteLine("Camera partially online");
                    break;
                }

                System.Threading.Thread.Sleep(1000);
                Console.Write(".");
                
            }


            acquistionContext.IntegrationTime = int.Parse(args[3]);
            acquistionContext.OperationMode = cuvis_net.OperationMode.Software;

            Console.WriteLine("Start recording now");

            for (int i = 0; i < int.Parse(args[4]); i++)
            {
                Console.WriteLine("Record image # {0}/" + args[4] + " (async)", i + 1);
                cuvis_net.AsyncMesu am = acquistionContext.Capture();
                var res = am.Get(TimeSpan.FromSeconds(5));
                if (res.Item2 != null)
                {
                    cuvis_net.Measurement mesu = res.Item2;

                    processingContext.Apply(mesu);

                    cubeExporter.Apply(mesu);
                    Console.WriteLine("done");

                    mesu.Dispose();
                }
                else 
                {
                    Console.WriteLine("failed");
                }
            }
            Console.WriteLine("done. cleaning up");


        }
    }
}
