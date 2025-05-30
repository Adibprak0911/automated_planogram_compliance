// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from px4:msg/UnregisterExtComponent.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "px4/msg/detail/unregister_ext_component__struct.h"
#include "px4/msg/detail/unregister_ext_component__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool px4__msg__unregister_ext_component__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[57];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("px4.msg._unregister_ext_component.UnregisterExtComponent", full_classname_dest, 56) == 0);
  }
  px4__msg__UnregisterExtComponent * ros_message = _ros_message;
  {  // timestamp
    PyObject * field = PyObject_GetAttrString(_pymsg, "timestamp");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->timestamp = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // name
    PyObject * field = PyObject_GetAttrString(_pymsg, "name");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_UINT8);
      Py_ssize_t size = 25;
      uint8_t * dest = ros_message->name;
      for (Py_ssize_t i = 0; i < size; ++i) {
        uint8_t tmp = *(npy_uint8 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(uint8_t));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // arming_check_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "arming_check_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->arming_check_id = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // mode_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "mode_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->mode_id = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // mode_executor_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "mode_executor_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->mode_executor_id = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * px4__msg__unregister_ext_component__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of UnregisterExtComponent */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("px4.msg._unregister_ext_component");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "UnregisterExtComponent");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  px4__msg__UnregisterExtComponent * ros_message = (px4__msg__UnregisterExtComponent *)raw_ros_message;
  {  // timestamp
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->timestamp);
    {
      int rc = PyObject_SetAttrString(_pymessage, "timestamp", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // name
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "name");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_UINT8);
    assert(sizeof(npy_uint8) == sizeof(uint8_t));
    npy_uint8 * dst = (npy_uint8 *)PyArray_GETPTR1(seq_field, 0);
    uint8_t * src = &(ros_message->name[0]);
    memcpy(dst, src, 25 * sizeof(uint8_t));
    Py_DECREF(field);
  }
  {  // arming_check_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->arming_check_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "arming_check_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // mode_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->mode_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mode_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // mode_executor_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->mode_executor_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mode_executor_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
