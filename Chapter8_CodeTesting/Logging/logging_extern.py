from pathlib import Path

from loguru import logger  # https://github.com/Delgan/loguru


# Setup the logger
filepath = Path(__file__).parent.joinpath("log_loguru.log")
logger.add(filepath, rotation="1 Week")


@logger.catch
def divide_integers(a: int, b: int) -> float:
    logger.debug(f"a={a}, b={b}")
    result = a / b
    return result


def main():
    for _ in range(3):
        print(divide_integers(10, 0))


if __name__ == "__main__":
    main()
