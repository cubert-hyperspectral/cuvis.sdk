using System;
using System.Drawing;

namespace ConsoleApp1
{
    class Program
    {
        static int keepRunning = 1;
        static void Main(string[] args)
        {
            if (args.Length != 6)
            {
                throw new ArgumentException("Invalid number of cli arguments");
            }

            Console.WriteLine("Example 07 video from session file");

            Console.WriteLine("loading user settings...");
            cuvis_net.General.Init(args[0]);

            Console.WriteLine("loading session...");
            var sess = new cuvis_net.SessionFile(args[1]);

            Console.WriteLine("Loading calibration...");
            var calib = new cuvis_net.Calibration(sess);

            Console.WriteLine("Loading acquisition context...");
            var acquistionContext = new cuvis_net.AcquistionContext(sess, true);

            Console.WriteLine("Prepare saving of measurements...");
            var general_settings = new cuvis_net.GeneralExportSettings(args[2], "all", 1.0, 0.0, cuvis_net.PanSharpeningInterpolationType.NearestNeighbour, cuvis_net.PanSharpeningAlgorithm.Noop, false, false, false, 1);
            var sa = cuvis_net.CubertSaveArgs.Default;
            sa.AllowDrop = true;
            sa.AllowOverride = true;
            sa.AllowSessionFile = true;

            Console.WriteLine("Writing files to:");


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

            Console.WriteLine("components:");
            int count = acquistionContext.ComponentCount;
            for (int i = 0; i < count; i++)
            {
                cuvis_net.ComponentInfo info = acquistionContext.GetComponentInfo(i);
                bool isOnline = acquistionContext.GetOnline(i);

                Console.WriteLine(" {0} is {1}", info.DisplayName, (isOnline ? "online" : "offline"));
            }

            Console.WriteLine("initializing hardware...");
            acquistionContext.SessionData = new cuvis_net.SessionData("video", 0, 0);
            acquistionContext.FPS = int.Parse(args[5]);
            acquistionContext.IntegrationTime = int.Parse(args[3]);
            acquistionContext.OperationMode = cuvis_net.OperationMode.Internal;
            acquistionContext.AutoExposure = int.Parse(args[4]) == 0;
            acquistionContext.Continuous = true;


            while (keepRunning != 0)
            {
                do
                {
                    if (acquistionContext.HasNextMeasurement)
                    {
                        break;

                    }
                    System.Threading.Thread.Sleep(1);
                } while (keepRunning != 0);

                cuvis_net.Measurement mesu = acquistionContext.GetNextMeasurement(1);

                if (mesu != null)
                {
                    cubeExporter.Apply(mesu);
                    mesu.Dispose();
                }
            }
            Console.WriteLine("finished.");
        }

    }
}
