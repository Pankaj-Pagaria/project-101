import random

response = "y"
while response == "y":
    num = random.randint(1,6)
    if num == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        response = input("Enter y to continue and n to stop: ")

    elif num == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
        response = input("Enter y to continue and n to stop: ")

    elif num == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
        response = input("Enter y to continue and n to stop: ")

    elif num == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to continue and n to stop: ")

    elif num == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to continue and n to stop: ")

    if num == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to continue and n to stop: ")