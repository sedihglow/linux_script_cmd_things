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

def print_sigs():
    valid = signal.valid_signals()

    print("Valid Signals:")
    for sig in valid:
        cell_type = type(sig)

        #if (cell_type ==
        """
        print(f"-- valid_signals() list element values and type --\n"
              f"data element type: {cell_type}\n"
              f"sig_name: {}\n"
              f"sig_num : {}")
        """

def print_sig_sigs_enum():
    print("Members of signal.Signals:")
    for member in signal.Signals:
        print(f"{member.name} = {member.value}")

def print_sigs_meta_enum():
    meta = signal.Signals.__class__

def print_valid_sigs(pretty: bool) -> None:
    print(type(signal.valid_signals()))

if __name__ == "__main__":
    faces = [":)", "^_^", "-_-", ":P", ";)", "-_-;", "^_^;", "(>^_^)>", "<(^_^<)"]

    print("\n\n------------\n\n")
    print_sigs()

    #print_sig_sigs_enum()
    signal.signal(signal.SIGINT, sigint_handler)

    """

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

    """
