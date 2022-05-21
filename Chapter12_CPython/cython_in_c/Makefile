CFLAGS += $(shell python3-config --cflags)
LDFLAGS += $(shell python3-config --ldflags)

compile:
	python3.8 -m cython caller.pyx -3
	gcc $(CFLAGS) -fPIC -c caller.c -o caller.o
	gcc $(CFLAGS) -fPIC -c test_cython.c -o test_cython.o
	gcc test_cython.o caller.o -Xlinker -export-dynamic  $(LDFLAGS) -lpython3.8 -o test_cython.out

run: compile
	./test_cython.out

clean:
	rm -rf caller.o
	rm -rf test_cython.o
	rm -rf test_cython.out

.phony:
	clean
