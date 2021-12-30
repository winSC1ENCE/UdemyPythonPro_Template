# cython: language_level=3
import sys
sys.path.insert(0, '')

from test import getterDouble
from test import getterList


cdef public double call_getterDouble():
    return getterDouble()


cdef public void call_getterList(double[] array):
    l = getterList()
    array[0] = l[0]
    array[1] = l[1]
    array[2] = l[2]
