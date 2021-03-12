from datetime import datetime

def log_state(f, x):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H:%M:%S")
        x_str = list_to_string(x)
        f.write(current_time + " " + x_str + '\n')


def list_to_string(x):
    str1 = ""
    for ele in x:
        str1 += format(ele, ".1f")
        str1 += " "

    return str1