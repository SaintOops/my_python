#include "individual.h"
#include <Python.h>


static PyObject *init(PyObject *self, PyObject *args) {
	PyListObject* values;
		

	if(!PyArg_ParseTuple(args, "O", &values))
		return NULL;
	
	Py_ssize_t n = PyList_Size(values);
  
  	double s[n];
  	for(int i = 0; i < n; i++)
    		s[i] = PyLong_AsLong(PyList_GetItem(values, i));
	
	return Py_BuildValue("i", individual_func(s));
}


static PyMethodDef tgpAlghoritm_funcs[] = {
    {"classify", init, METH_VARARGS, "doc"},
    {NULL, NULL, 0, NULL}
};


static PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"tgpAlghoritm",
	"doc",
	-1,
	tgpAlghoritm_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};




PyMODINIT_FUNC PyInit_tgpAlghoritm(void) {
	PyObject *m;
	m = PyModule_Create(&module);
	if(m == NULL)
		return NULL;

	return m;
}
