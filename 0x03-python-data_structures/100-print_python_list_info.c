#include <Python.h>
void print_python_list_info(PyObject *p)
{
	int length_list;
	
	length_list = PyList_size(list);
	printf("This sixe of the list is %d", length_list);

	for (i = 0; i < length_list, i++)
	{
		PyObject *item = PyList_GetItem(list, i);
		printf("The element at index %i is %s\n", i, PyString_AsString(item));
	}
