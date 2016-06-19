#include <Python.h>

////////////////////////////////////////
// Methods
////////////////////////////////////////

static PyObject* hello(PyObject *self, PyObject *args) {
    return Py_BuildValue("s", "Hello World");
}

static PyObject* fib(PyObject *self, PyObject *args) {
    unsigned long number;

    // PyArg_ParseTuple is a little bit like sscanf with sepcial format
    PyArg_ParseTuple(args, "k", &number);   // k for unsigned long

    if (number < 2)
        return Py_BuildValue("k", number);

    PyObject* fib1 = fib(self, Py_BuildValue("(k)", number-1));
    PyObject* fib2 = fib(self, Py_BuildValue("(k)", number-2));

    return PyNumber_Add(fib1, fib2);
}

static PyObject* add42(PyObject *self, PyObject *args) {
    long int number;
    PyArg_ParseTuple(args, "l", &number);   // l for long int
    return Py_BuildValue("l", number+42);
}

////////////////////////////////////////
// Module Definition
////////////////////////////////////////

PyDoc_STRVAR(module_doc, "basic functions in C API");

PyDoc_STRVAR(pydoc_fib,
    "Simple Fibonacci function.\n"
    "\n"
    ">>> fib(10)\n"
    "55"
);

PyDoc_STRVAR(pydoc_hello,
    "Simple Hello World.\n"
    "\n"
    ">>> hello()\n"
    "'Hello World'"
);

PyDoc_STRVAR(pydoc_add42,
    "Add 42 to number.\n"
    "\n"
    ">>> add42(100)\n"
    "142"
);

static PyMethodDef methods[] = {
    { "fib", fib, METH_VARARGS, pydoc_fib },
    { "hello", hello, METH_VARARGS, pydoc_hello },
    { "add42", add42, METH_VARARGS, pydoc_add42 },
    {NULL, NULL},   // end of methods
};

static PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,  // PyModuleDef_HEAD_INIT
    "_base",    // module name
    module_doc, // docstring
    0,          // size of per-module area
    methods,    // methods (table of module-level functions)
    NULL,       // array of slot definitions
    NULL,       // traverse function for GC
    NULL,       // clear function for GC
    NULL        // deallocation function
};

PyMODINIT_FUNC PyInit__base(void) {
    return PyModule_Create(&moduledef);
}
