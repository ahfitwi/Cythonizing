# Installation
1. Go to https://opencv.org
2. Click On Releases
3. Click on opencv version appropriate for your platform (Windows, Linux, Mac, ...) to download it
4. Downloading OpenCV for Windows: opencv-4.7.0-windows.exe and save at folder of your interest
5. Extract it into a location of your choice (C:\ in my case).
6. Add to the system path (env vars, path var, edit, ..): C:\opencv\build\x64\vc16\bin --> dll files
    - Put at the top of the list for highest priority
# Adding it to Visual Studio Community 2022
1. Open Visual Studio 2022
2. Create An Empty Project (C++)
3. Give A Name To Your Project; select location; and Give it a solution name
4. Create A New cpp file: opencv1.cpp
5. Go to project properties
6. Set Configuration: Release
7. Set Platform: x64 (depends on your platform)
8. Under configuration Properties, expand C/C++
9. Select General --> Add Include Directories --> C:\opencv\build\include --> select folder --> ok
10. Go to Linker --> General --> Additional Library directories --> C:\opencv\build\x64\vc16\lib --> select folder --> ok
11. Select Input --> Additional Dependencies -->opencv_world470.lib from C:\opencv\build\x64\vc16\lib --> paste --> ok
      - Release Version: opencv_world470.lib (on menu bar: select Release)
      - Debug Version: opencv_world470d.lib (on menu bar: select Debug)
13. Restart VS Community 2022
14. Build your app
15. Run your app

# Example code:
  1. Write C++ Code
    //Libraries
    #include<opencv2/core.hpp>
    #include<opencv2/imgcodecs.hpp>
    #include<opencv2/highgui.hpp>
    #include<iostream>
    #include<math.h>
    #include<cmath>
    #include<algorithm>
    
    //Namespaces
    using namespace std;
    using namespace cv;
  
    //Driver Code
    int main()
    {
        cv::Mat img = cv::imread("C:\Users\fitwialem2022\Documents\GitHub\alemcpp\alemcpp\imgs\img1.tiff", 1)
        namedWindow("Image", WINDOW_AUTOSIZE);
        cv::imshow("Img1", img);
        cv::moveWindow("Img1", 0, 45);
        cv::waitKey(0); //key press terminates the windwo
        cv::destroyAllWindows();
        retturn 0
    }
  
2. 
