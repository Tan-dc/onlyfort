import os
with open(os.environ['GITHUB_ENV'], "a") as env_file:
    env_file.write(f"RESULT=HelloWorld\n")
