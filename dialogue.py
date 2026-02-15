def process_command(command):
    command = command.lower()

    if "open google" in command:
        return "OPEN_GOOGLE"
    elif "open youtube" in command:
        return "OPEN_YOUTUBE"
    elif "time" in command:
        return "GET_TIME"
    else:
        return "UNKNOWN"
