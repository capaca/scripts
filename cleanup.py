import sys

input_file=sys.argv[1]
separator_token=sys.argv[2]
separator_token=";"

cleaned_lines = []

with open(input_file, "r") as csv:
    # Writing data to a file
    for line in csv:
        cleaned_tokens = []
        tokens = line.split(";")
        for token in tokens:
            cleaned_tokens.append(token.strip())
        cleaned_lines.append(separator_token.join(cleaned_tokens))

for l in cleaned_lines:
    print(l)
