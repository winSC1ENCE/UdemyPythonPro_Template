CC = gcc
PY_BIN = /usr/bin/python3
PY_LIB = /usr/lib/python3.8/config-3.8-x86_64-linux-gnu
PY_INC = /usr/include/python3.8
COMPILE_FLAGS = -std=c99 -I$(PY_INC) -Wno-unused-result -Wsign-compare -Wformat -DNDEBUG -g -O3 -Wall
LINKER_FLAGS =  -Xlinker -export-dynamic -L$(PY_LIB) -lpython3.8 -lcrypt -lpthread -ldl -lutil -lm -lm

compile:
	python3.8 -m cython caller.pyx -3
	$(CC) $(COMPILE_FLAGS) -c caller.c -o caller.o
	$(CC) $(COMPILE_FLAGS) -c test_cython.c -o test_cython.o
	$(CC) test_cython.o caller.o $(LINKER_FLAGS) -o test_cython.out

run:
	./test_cython.out
