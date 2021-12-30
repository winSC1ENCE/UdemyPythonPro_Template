from distutils.core import setup, Extension


def main() -> None:
    setup(name="math_cpython",
          version="1.0.0",
          description="CPython module in Python",
          ext_modules=[Extension("math_cpython", ["mathmodule.c"])])


if __name__ == "__main__":
    main()
