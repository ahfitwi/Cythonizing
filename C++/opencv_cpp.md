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
    - Release
        - Mat src = imread("1.tif");
            src.release(); // free mem
        - Mfloat* data = new float[100 * 100];
            Mat src(100, 100, CV_32FC1, data);
            src.release(); // will not free memory
            delete [] data;
    - **reduce**:
        #include "iostream"
        #include "opencv2/core/core.hpp"
        #include "opencv2/core/core_c.h"
        cv::Mat gg;
        cv::reduce(testMat, gg, 0, CV_REDUCE_SUM, CV_64FC1);
        CV_REDUCE_SUM, CV_REDUCE_MAX and other are defined in "opencv2/core/core_c.h" file.
        CV_REDUCE_SUM = 0
        CV_REDUCE_AVG = 1
        CV_REDUCE_MAX = 2
        CV_REDUCE_MIN = 3
    
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
        - max_size(): v.max_size(), same as v.size()
        - capacity(): v.capacity(), occupiesd + empty slots
        - empty(): v.empty()
    ### Divide vector by Scalar
        - transform(v.begin(), v.end(), v.begin(), [k](int &c){ return c/k; });
            
            void DivideVectorByScalar(vector<int> &v, int k){
                 transform(v.begin(), v.end(), v.begin(), [k](int &c){ return c/k; });
              }
        - for_each(v.begin(), v.end(), [k](int &c){ c /= k; });
            
            void DivideVectorByScalar(vector<int> &v, int k){
                for_each(v.begin(), v.end(), [k](int &c){ c /= k; });
            }
        - Method 3: Loop

            for(int i=0;i<v.size();++i)
                v[i] = v[i] / k;
# Valarray
    - #include<valarray>
    - #include<vector>
    - It is designed to hold an array of values, and easily perform mathematical operations on them. 
    - It also allows special mechanisms to refer to subsets of elements in the arrays.
    - Declaration: ***template <class T> class valarray;***
    - Operators: apply, cshift, max, min, resize, shift(+/-), size, sum, swap, begin, end,
    - To create a valarray from a vector: std::valarray<double> corpX(corps_tmp[i].data(), corps_tmp[i].size());
    - Back into a vector:corps_tmp[i].assign(std::begin(corpX), std::end(corpX));
    
    
                    #include<iostream>
                    #include<valarray>
                    #include<vector>


                    using namespace std;

                    int main()
                    {
                        std::valarray<int> a { 1, 2, 3, 4, 5};
                        std::valarray<int> b = a;
                        std::valarray<int> c = a + b;

                        std::valarray<bool> a1 { true, false};
                        std::valarray<bool> b2 {false, true};
                        std::valarray<bool> c2 = a and b;

                        for(int i =0; i< c2.size();i++)
                        {
                            cout<<c2[i]<<endl;
                        }
                        //o create a valarray from a vector:
                        //std::valarray<int> varr(a.data(), a.size());
                        //To write the data back into a vector:
                        //b.assign(std::begin(varr), std::end(varr));

                        return 0;
                    }
    
    
                    // Valarray Operators
                    #include<iostream>
                    #include<valarray> // for valarray functions
                    using namespace std;
                    int main()
                    {
                        // Initializing valarray
                        valarray<int> varr = { 10, 2, 20, 1, 30 };

                        // Declaring new valarray
                        valarray<int> varr1 ;

                        // Using apply() to increment all elements by 5
                        varr1 = varr.apply([](int x){return x=x+5;});

                        // Displaying new elements value
                        cout << "The new valarray with manipulated values is : ";
                        for (int &x: varr1) cout << x << " ";
                        cout << endl;

                        // Displaying sum of both old and new valarray
                        cout << "The sum of old valarray is : ";
                        cout << varr.sum() << endl;
                        cout << "The sum of new valarray is : ";
                        cout << varr1.sum() << endl;

                        // Displaying largest element of valarray
                        cout << "The largest element of valarray is : ";
                        cout << varr.max() << endl;

                        // Displaying smallest element of valarray
                        cout << "The smallest element of valarray is : ";
                        cout << varr.min() << endl;

                        // using shift() to shift elements to left
                        // shifts valarray by 2 position
                        varr1 = varr.shift(2);

                        // Displaying elements of valarray after shifting
                        cout << "The new valarray after shifting is : ";
                        for ( int&x : varr1) cout << x << " ";
                        cout << endl;

                        // using cshift() to circularly shift elements to right
                        // rotates valarray by 3 position
                        varr1 = varr.cshift(-3);

                        // Displaying elements of valarray after circular shifting
                        cout << "The new valarray after circular shifting is : ";
                        for ( int&x : varr1) cout << x << " ";
                        cout << endl;


                        // Initializing 1st valarray
                        valarray<int> varr3 = {1, 2, 3, 4};

                        // Initializing 2nd valarray
                        valarray<int> varr4 = {2, 4, 6, 8};

                        // Displaying valarrays before swapping
                        cout << "The contents of 1st valarray "
                                "before swapping are : ";
                        for (int &x : varr3)
                            cout << x << " ";
                        cout << endl;
                        cout << "The contents of 2nd valarray "
                                "before swapping are : ";
                        for (int &x : varr4)
                            cout << x << " ";
                        cout << endl;

                        // Use of swap() to swap the valarrays
                        varr1.swap(varr4);

                        // Displaying valarrays after swapping
                        cout << "The contents of 1st valarray "
                                "after swapping are : ";
                        for (int &x : varr3)
                            cout << x << " ";
                        cout << endl;

                        cout << "The contents of 2nd valarray "
                                "after swapping are : ";
                        for (int &x : varr4)
                            cout << x << " ";
                        cout << endl;

                        return 0;

                    }

