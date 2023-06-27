using System;
using System.Diagnostics;
using System.Drawing;

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

            Console.WriteLine("Example 04 change distance");

            Console.WriteLine("loading user settings...");
            cuvis_net.General.Init(args[0]);

            Console.WriteLine("loading session...");
            var sess = new cuvis_net.SessionFile(args[1]);

            Console.WriteLine("loading measurement...");
            cuvis_net.Measurement mesu = sess.GetMeasurement(0);
            Debug.Assert(mesu.GetHashCode() != null, " No data found");

            Console.WriteLine(" Data 1 {0} {1} ms mode={2}", mesu.Name, mesu.IntegrationTime, mesu.ProcessingMode);

            Console.WriteLine("Loading calibration and processing context...");
            var processingContext = new cuvis_net.ProcessingContext(sess);

            Console.WriteLine("setting distance..");
            processingContext.CalcDistance(int.Parse(args[2]));

            processingContext.ProcessingMode = cuvis_net.ProcessingMode.Raw;

            bool isCapable = processingContext.IsCapable(mesu, processingContext.ProcessingMode, false);

            Debug.Assert(isCapable);

            
            Console.WriteLine("changing distance...");
            processingContext.Apply(mesu);

            Console.WriteLine("saving...");
            var sa = cuvis_net.CubertSaveArgs.Default;
            sa.AllowSessionFile = true;
            sa.AllowOverride = true;
            mesu.Save(args[3], sa);
            Console.WriteLine("finished.");


        }
    }
}
