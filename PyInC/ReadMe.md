https://www.youtube.com/watch?v=45TOazYbedI
https://www.youtube.com/watch?v=nHEF1epuuco

https://www.youtube.com/watch?v=a65JdvOaygM
https://www.youtube.com/watch?v=eEZOjojVgv4

# Extending Python With C
- On WIndows, use MingW

### What are C Extensions?
- Python Talking With The C Programming Language
- Creations of Wrapper Which Bind Python Objects to C Functions
- There is many sub-topic's of C Extensions
- Because of Python's high level abstractions some things can't be done w/o a lower level implementation first.
- Perhaps you already have a library of C functions that you want to turn into a python module to use.
### Python Header
- ***#include<Python.h>
- Everything in the Python header starts with the prefix Py or PY
- The **PyObject** type is always used as a pointer and is handles all the data parsing between python and C
- Example: **static PyObject* myFunc(PyObject* self)**
- **PyArg_ParseTuple(args, format, ...)**: Handles getting the arguments from python
- **Py_BuildValue(format, ...)**: Handles turning values into PyObject pointers
- **PyModule_Create(moduleDef)**: Initializes the module and wraps the method pointers using the module definitions.
- **Py_None**: If you want your function to return nothing, return **Py_None** value
- **PyMethodDef**: this structure is one of the most critcal parts because the compiler won't pickup any error inside.
  - It must always end with terminating **NULL** and 0 values. {NULL, NULL, 0, NULL}
  - Here we tell python if the function has argument, no arguments or arguments and keywords.
  
      static PyMethodDef myMethods[] {
        {"func1", func1, METH_NOARGS, "func1 doc"},
        {"func2", func2, METH_VARARGS, "func2 doc"},
        {NULL, NULL, 0, NULL}
      }
  - Pattern: pyMethodName, function, functionType, Docs
- **PyMethodDef**: This structure is what we use to tell the PyModule_Create() function what info to use to create the module.
  - We need to give it a name, documentation, tell python of we will control the module state and the structure of methods to include in the module.
- ****:
- ****:
- ****:
- ****:
- ****:
- ****:
