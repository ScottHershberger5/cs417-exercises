import argparse

# 1. Set up the parser
parser = argparse.ArgumentParser(description="A script that greets you!")

# 2. Add arguments
parser.add_argument("--name", type=str, default="Stranger", help="Your name")
parser.add_argument("--shout", action="store_true", help="Print in ALL CAPS")
parser.add_argument("--repeat", type=int, default=1, help="Repeats the greeting n number of times")

# 3. Parse the arguments
args = parser.parse_args()

# 4. Use the arguments in the program
message = f"Hello there, {args.name}!"
for i in range(args.repeat):
    
    if args.shout:
        print(message.upper())
    else:
        print(message)