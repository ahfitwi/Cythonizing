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
  
# Basic Image Container In OPenCV C++
    - https://www.youtube.com/watch?v=1tibU7vGWpk
    - #include<opencv2/core/cre.hpp>
    - cv::Mat M(2,2, CV_8UC(2): using constructor
    - M.creat(3,3, CU_8UC(2))
    - int sz[2] = {2,2,2};
        Mat L(3,lz, _8UC(1), Scalar::all(0)); cannot be printed by cc<<
    - Mat E = Nat::eye(4,4, CV_64F);
    - Mat O = Mat:: O4,4, CV_64F);
    - Mat Z = Mat::zeros(3,3, CV_8UC1);
    - Mat C = (Mat_<double>(3,3)<<0,1,2,3,4,5,6,7,8);
    - Mat RowClone = C.row(1).clone();
    - Mat R = Mat(3,2,CV_8UC3);
        randu(R, Scalar::all(0), Scalar::all(255));
    - Printing:
        - cout<<"R default"<<endl<<R<<endl;
        - cout<<"R python "<<endl<<format(R, "python")<<endl<<endl;
        - cout<<"R numpy "<<endl<<format(R, "numpy")<<endl<<endl;
        - cout<<"R csv"<<endl<<format(R, "csv")<<endl<<endl;
        - cout<<"R c"<<endl<<format(R, "c")<<endl<<endl;
# Vector Methods:
    ### Modifiers:
        - push_back(val) --> add e/t
        - pop_back() --> pop last e/t
        - insert(idx, val)
        - erase(): v.erase(), remove every e/t, v={}
        - clear() --> vector.clear(), deletes all e/ts, --> vector = {}
        - swap()
        - assign() --> vector.assign(val1, val2, ...
    ### Iterators:
        - begin(): for(auto a=begin(); a!=end();a++){...}
        - end():
    ### Capacity:
        - size(): v.size()
        - max_size(): v.max_size()
        - capacity(): v.capacity()
        - empty(): v.empty()
    
