import os

print("Current directory:", os.getcwd())

if not os.path.exists("Practice"):
    os.mkdir("Practice")

os.chdir("Practice")

print("New directory:", os.getcwd())
print("Files and directories:", os.listdir())
