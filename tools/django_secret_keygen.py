#!/usr/bin/python3

import random

ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'


def main():
    return ''.join([random.SystemRandom().choice(ALLOWED_CHARS) for _ in range(50)])


if __name__ == '__main__':
    key = main()
    print(key)
