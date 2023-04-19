### Steps To Install:
- https://www.tutorialspoint.com/how-to-install-opencv-for-cplusplus-in-windows
- Opencv for C++
- cmake

# 1. Introduction to C++ PL
- Mid-level PL
- Source Code --> Compile --> Machine Code
- C++ Supports LL Programming
- OOP
- Templates: STL (Standard Template Library) --> provide wide range of containers
- Exception Handling
- Hello World:

        #include <iostream>
        int main() {
            std::cout << "Hello, World!" << std::endl;
            return 0;
        }
        
        #include <iostream>
        using namespace std;

        int main()
        {
          cout << "Hello World";
          return 0;
        }

- Setting up your environment: Install
  - C++ Compiler
    - Linux:
    
          sudo apt-get update
          sudo apt-get install gcc
          sudo apt-get install g++
          sudo apt-get install build-essential
          g++ --version
          g++ filename.cpp -o any-name (program name and exe name)
          g++ helloworld.cpp -o hello
          ./hello
          
    - Windows:
  - Text Editor (create your program and save as *.cpp)
    - codeblocks
-
