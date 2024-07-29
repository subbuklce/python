#from tqdm.notebook import tqdm_notebook
from tqdm import tqdm
import time

# Example: a process with 100 steps
total_steps = 100

# Using tqdm with a specified total number of steps
for i in tqdm(range(total_steps), desc = "Moving files"):
    time.sleep(0.005)  # Replace this with your actual processing code