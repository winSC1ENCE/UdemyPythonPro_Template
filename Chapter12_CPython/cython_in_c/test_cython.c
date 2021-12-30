#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdlib.h>

#include "caller.h"

void Initialize(void)
{
    Py_Initialize();
}

void Finalize(void)
{
    Py_Finalize();
}

void PrepareImport(void)
{
    PyObject *sys  = PyImport_ImportModule("sys");
    PyObject *path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyUnicode_FromString("."));
}

void DoubleTest(void)
{
    double result = call_getterDouble();
    printf("%lf\n", result);
}

void ListTest(void)
{
    double* array = (double *)malloc(3 * sizeof(double));

    call_getterList(array);
    for (int i = 0; i < 3; i++)
    {
        printf("%lf\n", array[i]);
    }

    free(array);
    array = NULL;
}

int main(void)
{
    PyImport_AppendInittab("caller", PyInit_caller);
    Initialize();
    atexit(Finalize);
    PrepareImport();

    PyImport_ImportModule("caller");
    PyErr_Print();

    DoubleTest();
    ListTest();

    return 0;
}
