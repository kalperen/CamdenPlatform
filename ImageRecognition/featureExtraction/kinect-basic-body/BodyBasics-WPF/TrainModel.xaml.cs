

namespace Microsoft.Samples.Kinect.BodyBasics
{

    using Microsoft.Kinect;
    using System;
    using System.Collections.Generic;
    using System.Windows;
    using System.ComponentModel;
    using System.IO;
    using System.Text;

    public partial class MainWindow : Window
    {

        /// Constant for clamping Z values of camera space points from being negative
        /// </summary>
        private const float InferredZPositionClamp = 0.1f;

        /// Active Kinect sensor
        private KinectSensor kinectSensor = null;

        /// Coordinate mapper to map one type of point to another
        private CoordinateMapper coordinateMapper = null;

        // Reader for body frames
        private BodyFrameReader bodyFrameReader = null;

        // Array for the bodies
        private Body[] bodies = null;

        /// Current status text to display
        private string statusText = null;

        public MainWindow()
        {
            this.kinectSensor = KinectSensor.GetDefault();

            // get the coordinate mapper
            this.coordinateMapper = this.kinectSensor.CoordinateMapper;

            // open the reader for the body frames
            this.bodyFrameReader = this.kinectSensor.BodyFrameSource.OpenReader();

            // open the sensor
            this.kinectSensor.Open();

            // set the status text
            if (this.kinectSensor.IsAvailable)
            {
                this.statusText = Properties.Resources.RunningStatusText;
            }
            else
            {
                this.statusText = Properties.Resources.NoSensorStatusText;
            }

            this.InitializeComponent();
        }

        // INotifyPropertyChangedPropertyChanged event to allow window controls to bind to changeable data
        //public event PropertyChangedEventHandler PropertyChanged;


        /// Execute start up tasks
        private void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            if (this.bodyFrameReader != null)
            {
                this.bodyFrameReader.FrameArrived += this.Reader_FrameArrived;
            }
        }


        /// Execute shutdown tasks
        private void MainWindow_Closing(object sender, CancelEventArgs e)
        {
            if (this.bodyFrameReader != null)
            {
                // BodyFrameReader is IDisposable
                this.bodyFrameReader.Dispose();
                this.bodyFrameReader = null;
            }

            if (this.kinectSensor != null)
            {
                this.kinectSensor.Close();
                this.kinectSensor = null;
            }
        }


        /// Handles the body frame data arriving from the sensor
        private void Reader_FrameArrived(object sender, BodyFrameArrivedEventArgs e)
        {
            bool dataReceived = false;

            using (BodyFrame bodyFrame = e.FrameReference.AcquireFrame())
            {
                if (bodyFrame != null)
                {
                    if (this.bodies == null)
                    {
                        this.bodies = new Body[bodyFrame.BodyCount];
                    }

                    // The first time GetAndRefreshBodyData is called, Kinect will allocate each Body in the array.
                    // As long as those body objects are not disposed and not set to null in the array,
                    // those body objects will be re-used.
                    bodyFrame.GetAndRefreshBodyData(this.bodies);
                    dataReceived = true;
                }
            }

            if (dataReceived)
            {

                int humanCounter = 0;

                foreach (Body body in this.bodies)
                {

                    if (body.IsTracked)
                    {
                        humanCounter++;
                        IReadOnlyDictionary<JointType, Joint> joints = body.Joints;

                        // convert the joint points to depth (display) space
                        Dictionary<JointType, Point> jointPoints = new Dictionary<JointType, Point>();

                        var csvcontent = new StringBuilder();

                        string csvpath = @"C:\Users\Desktop\standing.csv";

                        /*
                        foreach (JointType jointType in joints.Keys)
                        {
                            Console.WriteLine("About to write to file:");
                            csvcontent.Append(jointType + ",");

                        } */

                        if(!File.Exists(csvpath))
                        {
                            Console.WriteLine("About to write to file:");
                            csvcontent.Append("Position,SpineBaseX,SpineBaseY,SpineBaseZ,SpineMidX,SpineMidY,SpineMidZ,NeckX,NeckY,NeckZ,HeadX,HeadY,HeadZ,ShoulderLeftX," +
                                "ShoulderLeftY,ShoulderLeftZ,ElbowLeftX,ElbowLeftY,ElbowLeftZ,WristLeftX,WristLeftY,WristLeftZ,HandLeftX,HandLeftY,HandLeftZ," +
                                "ShoulderRightX,ShoulderRightY,ShoulderRightZ,ElbowRightX,ElbowRightY,ElbowRightZ,WristRightX,WristRightY,WristRightZ,HandRightX," +
                                "HandRightY,HandRightZ,HipLeftX,HipLeftY,HipLeftZ,KneeLeftX,KneeLeftY,KneeLeftZ,AnkleLeftX,AnkleLeftY,AnkleLeftZ,FootLeftX," +
                                "FootLeftY,FootLeftZ,HipRightX,HipRightY,HipRightZ,KneeRightX,KneeRightY,KneeRightZ,AnkleRightX,AnkleRightY,AnkleRightZ,FootRightX," +
                                "FootRightY,FootRightZ,SpineShoulderX,SpineShoulderY,SpineShoulderZ,HandTipLeftX,HandTipLeftY,HandTipLeftZ,ThumbLeftX,ThumbLeftY," +
                                "ThumbLeftZ,HandTipRightX,HandTipRightY,HandTipRightZ,ThumbRightX,ThumbRightY,ThumbRightZ," + Environment.NewLine);
                        }

                        string human = "";
                        foreach (JointType jointType in joints.Keys)
                        {

                            // sometimes the depth(Z) of an inferred joint may show as negative
                            // clamp down to 0.1f to prevent coordinatemapper from returning (-Infinity, -Infinity)
                            CameraSpacePoint position = joints[jointType].Position;

                            human += position.X + "," + position.Y + "," + position.Z + ",";

                        }

                        Console.WriteLine("NA," + human);


                        csvcontent.Append("NA," + human + Environment.NewLine);

                        File.AppendAllText(csvpath, csvcontent.ToString());

                    }
                }

                Console.WriteLine("Number of human found: " + humanCounter);
                humanCounter = 0;

                Console.WriteLine("  ");
            }
        }

    }


}