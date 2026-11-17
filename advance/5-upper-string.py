import re


text = input()

# Keep periods and commas as tokens so sentence boundaries remain reliable.
tokens = re.findall(r"[^\s.,]+|[.,]", text)
keywords = []
sentence_start = True
word_number = 0

for token in tokens:
    if token in {".", ","}:
        if token == ".":
            sentence_start = True
        continue

    word_number += 1
    if not sentence_start and token[0].isupper() and not token.isdigit():
        keywords.append(f"{word_number}:{token}")
    sentence_start = False

if keywords:
    print("\n".join(keywords))
else:
    print("None")
