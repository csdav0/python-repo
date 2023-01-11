#!/usr/bin/env python3

print("This code will always execute.")

def main():
    print("This print statement is happening because first_module's main() function was called by another module.")

if __name__ == "__main__":
    print("Code is being run directly from Python.")
    main()

else:
    print("Code is being run indirectly from import & __name__ ==", __name__)
