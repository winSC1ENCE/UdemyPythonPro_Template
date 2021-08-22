# How to use CPython

## Creating Virtualenv based on Python Build

```bash
sudo apt-get install python3.8
sudo apt-get install python3.8-dev
python3.8 -m pip install -r requirements.txt
```

## Running Python in C

```bash
cd python_in_c
make compile && make run
```

## Running Cython in C

```bash
cd cython_in_c
make compile && make run
```

## Running C in Python

```bash
cd c_in_python
python setup.py install
python main.py
```

## Using Numba in Python

```bash
cd numba_jit
python setup.py install
python main.py
```
