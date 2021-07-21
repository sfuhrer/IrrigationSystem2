from datetime import datetime

def log_state(f, x):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H:%M:%S")
        x_str = list_to_string(x)
        f.write(current_time + " " + x_str + '\n')

def log_message(f, message):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H:%M:%S")
        f.write(current_time + message + '\n')


def list_to_string(x):
    str1 = ""
    for idx, val in enumerate(x):
        if(idx==2):
            str1 += format(val, ".0f")
        elif (idx==4):
            str1 += format(val, ".2f")
        else:
            str1 += format(val, ".1f")
        str1 += " "

    return str1 