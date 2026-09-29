import re

text = "Peter Piper picked a peck of pickled peppers"

words = re.findall(r"\b[pP]\w{2,}\b", text)

print(words)