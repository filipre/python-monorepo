import os
import sys

from abc_random_name import generate_name


def serve():
    print("Serving...", generate_name())
    print(sys.path)


if __name__ == "__main__":
    serve()
