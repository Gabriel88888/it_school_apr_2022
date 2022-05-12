#Log levels : DEBUG , INFO , WARNING, ERROR, CRITICAL


def log(msg, level):
    print("[", level, "]",  msg)


log("start script", "INFO")

def debug(msg):
    log(msg, "DEBUG")

def warning(msg):
    log(msg, "WARNING")

def error(msg):
    log(msg, "ERROR")

def critical(msg):
    log(msg, "CRITICAL")




# log("Debug message", "DEBUG" )

# log("Warning message", "WARNING")

# log("Error message", "ERROR")

# log("Critical message !", "CRITICAL")



# def debug(msg):
#     print("[", level, "]" ,  msg)
