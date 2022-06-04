#Log levels : DEBUG , INFO , WARNING, ERROR, CRITICAL


def log(msg, level):
    print("[", level, "]",  msg)

def debug(msg):
    log(msg, "DEBUG")

def info(msg):
    log(msg, "INFO")

def warning(msg):
    log(msg, "WARNING")

def error(msg):
    log(msg, "ERROR")

def critical(msg):
    log(msg, "CRITICAL")

# print(__name__)
if __name__ == "__main__":
    
    print("From MODULE ! ! !")


# log("Debug message", "DEBUG" )

# log("Warning message", "WARNING")

# log("Error message", "ERROR")

# log("Critical message !", "CRITICAL")



# def debug(msg):
#     print("[", level, "]" ,  msg)
