import time
from datetime import datetime

import click


def sleep_and_print(seconds):
    print(f"starting {seconds} sleep "+	"u\U0001F634")
    time.sleep(seconds)
    print(f"finished {seconds} sleep"+ "u\u23F0")
    return seconds


start = datetime.now()
print([sleep_and_print(3), sleep_and_print(6)])
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
