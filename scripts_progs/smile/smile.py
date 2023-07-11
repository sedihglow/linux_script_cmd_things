#!/usr/bin/env python3

import time
import random
import sys
import signal
import os

bye_falicia = "): | D: | ); | D; | :$ |"
def sigint_handler(signum, handler):
    print("\n\n Camera and Recording has initiated. HI\n\n")
    sys.exit(0)

if __name__ == "__main__":
    faces = [":)", "^_^", "-_-", ":P", ";)", "-_-;", "^_^;", "(>^_^)>", "<(^_^<)"]

    #signal.signal(signal.SIGINT, sigint_handler)

    random.seed()

    try:
        while (True):
            random.shuffle(faces)

            for face in faces:
                print(face, end=' | ')
            print()

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n", bye_falicia)
