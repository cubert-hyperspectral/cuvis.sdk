using System;
using System.Diagnostics;
using System.Drawing;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 6)
            {
                throw new ArgumentException("Invalid number of cli arguments");
            }

            Console.WriteLine("Example 02 reprocess measurement");

            Console.WriteLine("loading user settings...");
            cuvis_net.General.Init(args[0]);

            Console.WriteLine("loading measurement...");
            var sessMesu = new cuvis_net.SessionFile(args[1]);
            cuvis_net.Measurement mesu = sessMesu.GetMeasurement(0);
            Debug.Assert(mesu.GetHashCode() != null, " No data found");
            

            Console.WriteLine("loading dark...");
            var sessDark = new cuvis_net.SessionFile(args[2]);
            cuvis_net.Measurement dark = sessDark.GetMeasurement(0);
            Debug.Assert(dark.GetHashCode() != null, " No data found");

            Console.WriteLine("loading white...");
            var sessWhite = new cuvis_net.SessionFile(args[3]);
            cuvis_net.Measurement white = sessWhite.GetMeasurement(0);
            Debug.Assert(white.GetHashCode() != null, " No data found");

            Console.WriteLine("loading distance...");
            var sessDistance = new cuvis_net.SessionFile(args[4]);
            cuvis_net.Measurement distance = sessDistance.GetMeasurement(0);
            Debug.Assert(distance.GetHashCode() != null, " No data found");

            Console.WriteLine(" Data 1 {0} {1} ms mode={2} flags={3}", mesu.Name, mesu.IntegrationTime, mesu.ProcessingMode, mesu.MeasurementFlags);

            Console.WriteLine("Loading processing context...");
            var processingContext = new cuvis_net.ProcessingContext(sessMesu);

            Console.WriteLine("Set references...");

            processingContext.SetReference(dark, cuvis_net.ReferenceType.Dark);
            processingContext.SetReference(white, cuvis_net.ReferenceType.White);
            processingContext.SetReference(distance, cuvis_net.ReferenceType.Distance);

            var sa = cuvis_net.CubertSaveArgs.Default;
            sa.AllowSessionFile = true;
            sa.AllowOverride = true;
            sa.AllowInfoFile = false;

            cuvis_net.ProcessingMode[] target_modes = { cuvis_net.ProcessingMode.Raw, cuvis_net.ProcessingMode.DarkSubtract, cuvis_net.ProcessingMode.Reflectance, cuvis_net.ProcessingMode.SpectralRadiance };
            string[] paths = { args[5] + "/Raw", args[5] + "/DS", args[5] + "/Ref", args[5] + "/RAD" };
            for (int i = 0; i < target_modes.Length; i++)
            {
                processingContext.ProcessingMode = target_modes[i];

                bool isCapable = processingContext.IsCapable(mesu, target_modes[i], false);

                if (isCapable)
                {
                    Console.WriteLine("processing to mode {0}", target_modes[i]);
                    processingContext.Apply(mesu);
                    //should use exporter with save args!
                    mesu.Save(paths[i], sa);
                }
                else
                {
                    Console.WriteLine("Cannot process to mode {0}", target_modes[i]);
                }

            }

            Console.WriteLine("finished.");
        }
    }
}
