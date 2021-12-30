CC = gcc
PY_BIN = /usr/bin/python3
PY_LIB = /usr/lib/python3.8/config-3.8-x86_64-linux-gnu
PY_INC = /usr/include/python3.8
COMPILE_FLAGS = -std=c99 -I$(PY_INC) -Wno-unused-result -Wsign-compare -Wformat -DNDEBUG -g -O3 -Wall
LINKER_FLAGS =  -Xlinker -export-dynamic -L$(PY_LIB) -lpython3.8 -lcrypt -lpthread -ldl -lutil -lm -lm

compile:
	$(CC) $(COMPILE_FLAGS) -c test_capi.c -o test_capi.o
	$(CC) test_capi.o $(LINKER_FLAGS) -o test_capi.out

run:
	./test_capi.out
