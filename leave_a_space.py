text = """your text here"""
text = text.split(".")
text = ". ".join(map(str, text))
text = text.split(",")
text = ", ".join(map(str, text))
print(text)
