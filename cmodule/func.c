#include "simplefunc.h"
#include <Python.h>


void matrix_multiplication(int A[3][3], int B[3][3], int C[3][3]) {

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			C[i][j] = 0;
			for (int k = 0; k < 3; k++) {
				C[i][j] += A[i][k] * B[k][j];
			}
		}
	}
}


/*static PyObject *mm(PyObject *self, PyObject *args) {
	PyListObject* a[3][3];
	PyListObject* b[3][3];
	int c[3][3];	

	if(!PyArg_ParseTuple(args, "OO", &a,&b))
		return NULL;
	
	
	matrix_multiplication(a[3][3],b[3][3],c[3][3]);
	return Py_BuildValue("O", c[3][3]);
}
*/
	



static PyObject *fib(PyObject *self, PyObject *args) {
	double n;

	if(!PyArg_ParseTuple(args, "d", &n))
		return NULL;
	
	return Py_BuildValue("i", fibonacci(n));

}

static PyObject *cat(PyObject *self, PyObject *args) {
	double n;

	if(!PyArg_ParseTuple(args, "d", &n))
		return NULL;
	
	return Py_BuildValue("i", Catalan_numbers(n));

}

static PyObject *fac(PyObject *self, PyObject *args) {
	double n;

	if(!PyArg_ParseTuple(args, "d", &n))
		return NULL;
	
	return Py_BuildValue("i", factorial(n));

}

static PyObject *duobfac(PyObject *self, PyObject *args) {
	double n;

	if(!PyArg_ParseTuple(args, "d", &n))
		return NULL;
	
	return Py_BuildValue("i", doubfactorial(n));

}

	static PyObject *bin(PyObject *self, PyObject *args) {
	double n;
	double k;


	if(!PyArg_ParseTuple(args, "dd", &n, &k))
		return NULL;
	
	return Py_BuildValue("i", binomial(n,k));

}

static PyObject *n_len(PyObject *self, PyObject *args) {
	int n;
	double r;
	double a;

	if(!PyArg_ParseTuple(args, "idd", &n,&r,&a))
		return NULL;
	
	return Py_BuildValue("d", n_length(n,r,a));

}

static PyObject *binomi(PyObject *self, PyObject *args) {
	double a;
	double b;
	int n;

	if(!PyArg_ParseTuple(args, "ddi", &a,&b,&n))
		return NULL;
	
	return Py_BuildValue("d", binom(a,b,n));
}

static PyObject *subfac(PyObject *self, PyObject *args) {
	double n;

	if(!PyArg_ParseTuple(args, "d", &n))
		return NULL;
	
	return Py_BuildValue("I", subfactorial(n));
}


static PyMethodDef someSimpleFunc_funcs[] = {
    {"fibonacci", fib, METH_VARARGS, "doc"},
	{"catalan", cat, METH_VARARGS, "doc"},
	{"factorial", fac, METH_VARARGS, "doc"},
	{"twice_n", n_len, METH_VARARGS, "doc"},
	{"binomial", bin, METH_VARARGS, "doc"},
	{"binom", binomi, METH_VARARGS, "doc"},
	{"subfactorial", subfac, METH_VARARGS, "fukin' doc"},
	{"double_factorial", duobfac, METH_VARARGS, "fukin' doc"},
	//§{"matrix_multiplication", mm, METH_VARARGS, "fukin' doc"},
    {NULL, NULL, 0, NULL}
};


static PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"someSimpleFunc",
	"doc",
	-1,
	someSimpleFunc_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};




PyMODINIT_FUNC PyInit_someSimpleFunc(void) {
	PyObject *m;
	m = PyModule_Create(&module);
	if(m == NULL)
		return NULL;

	return m;
}
