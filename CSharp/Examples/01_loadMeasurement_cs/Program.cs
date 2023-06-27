using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.Reflection;

namespace ConsoleApp1
{

    class Program
    {
        static void LogMethod(string message, cuvis_net.General.LogLevel level)
        {
            Console.WriteLine("Logged:  " + message);
        }

        static void Main(string[] args)
        {
            if (args.Length != 2)
            {
                throw new ArgumentException("Invalid number of cli arguments");
            }

            Console.WriteLine("loading user settings...");

            cuvis_net.General.Init(args[0]);
            cuvis_net.General.SetLogger(LogMethod, "de-DE.UTF-8", cuvis_net.General.LogLevel.info);

            Console.WriteLine("loading session... ");

            var sess = new cuvis_net.SessionFile(args[1]);

            Console.WriteLine("loading measurement... ");

            cuvis_net.Measurement mesu = sess.GetMeasurement(0);
            Debug.Assert(mesu.GetHashCode() != null, " No data found");


            Console.WriteLine("Data 1 " + mesu.Name + "; t=" + mesu.IntegrationTime.ToString() + " ms; mode=" + mesu.ProcessingMode);

            if (mesu.MeasurementFlags > 0) // the flag is just a uint should be list!
            {
                Console.WriteLine("  Flags:");
                foreach (var flags in new List<uint>() { mesu.MeasurementFlags })
                {
                    Console.WriteLine("  - " + flags.ToString());
                }
            }

            Debug.Assert((mesu.ProcessingMode is cuvis_net.ProcessingMode.Raw), " This example requires raw mode");

            var cube = (cuvis_net.ImageData<ushort>)(mesu.Data["cube"].Value);

            int x = 120;
            int y = 200;

            Debug.Assert(x < cube.Width, "x index exceeds cube width");
            Debug.Assert(y < cube.Height, "y index exceeds cube height");

            Console.WriteLine("lambda [nm]; raw counts [au] ");

            for (int chn = 0; chn < cube.Channels; chn++)
            {
                int Value = cube.arr[x, y, chn];

                var lambda = cube.wavelength[chn];
                Console.WriteLine(lambda + "; " + Value);
                
            }

            Console.WriteLine("finished.");

        }
    }
}
