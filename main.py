import os

def main():
    print("--- Secure Supply Chain Demo ---")
    print(f"User: {os.environ.get('USER', 'unknown')}")
    print("Application is running...")

if __name__ == "__main__":
    main()
