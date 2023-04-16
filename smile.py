#!/usr/bin/env python3

import time
import random

faces = [":)", "^_^", "-_-", ":P", ";)", "-_-;", "^_^;", "(>^_^)>", "<(^_^<)"]
bye_falicia = "): | D: | ); | D; | :$ |"

random.seed()

while (True):
    try:
        random.shuffle(faces)

        for face in faces:
            print(face, end=' | ')

        print()

        time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n", bye_falicia)
        break

