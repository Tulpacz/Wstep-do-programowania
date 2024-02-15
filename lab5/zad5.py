import keyword
for i in ["for",
    "print",
    "break",
    "done",
    "bad"]:
    print(keyword.iskeyword(str(i)))