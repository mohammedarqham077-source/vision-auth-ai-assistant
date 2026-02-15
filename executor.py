import webbrowser
from datetime import datetime

def execute_command(action):
    if action == "OPEN_GOOGLE":
        print("🌐 Opening Google...")
        webbrowser.open("https://www.google.com")

    elif action == "OPEN_YOUTUBE":
        print("🎬 Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif action == "GET_TIME":
        now = datetime.now()
        print("⏰ Current Time:", now.strftime("%H:%M:%S"))

    else:
        print("🤖 Sorry, I didn’t understand that command.")
