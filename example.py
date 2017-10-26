from progress_bar import print_progress_bar
from time import sleep

items = list(range(0, 100))

for i, item in enumerate(items):
    sleep(0.1)
    print_progress_bar(i, len(items), length=50, show_balance=True)
print_progress_bar(completed=True, length=50)
