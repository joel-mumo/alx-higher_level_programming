#include <stdio.h>
#include <Python.h>

/**
 *  print_python_list_info - shows info about Python lists
 *  @p: object
 *  Return: 0 on success
 */
void print_python_list_info(PyObject *p)
{
	long int list_size, x, y;

	y = 0;
	PyObject *obj;

	list_size = PyList_Size(p);
	x = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", x);
	while (i < list_size)
	{
		obj = PyList_GetItem(p, y);
		printf("Element %ld: %s\n", y, Py_TYPE(obj)->tp_name);
		y++;
	}
}
