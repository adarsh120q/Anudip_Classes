#A function that logs events keeps appending to old logs unexpectedly.

def log_events(event):
    with open("log_file.log","a") as f:
        f.write(event+"\n")

file1 = log_events("Hello1")
