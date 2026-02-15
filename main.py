from auth.face_auth import authenticate_user
from dialog.rule_engine import process_command
from executor.command_executor import execute_command

def main():
    print("🔐 Starting Face Authentication...")

    if not authenticate_user():
        print("❌ Authentication Failed!")
        return

    print("✅ Authentication Successful!")
    print("🎤 Enter your command (type 'exit' to quit):")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("👋 Exiting system.")
            break

        action = process_command(user_input)
        execute_command(action)


if __name__ == "__main__":
    main()
