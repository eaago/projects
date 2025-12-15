import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
        print("======================================================")
        print("=                                                    =")
        print("=     SLAY THE SPIRE CLONE CONSOLE BASED PROJECT     =")
        print("=                                                    =")
        print("======================================================")