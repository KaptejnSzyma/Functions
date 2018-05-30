def python_food():
    width = 90
    text = "Span and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return  " " * left_margin + text


# with open("centered", mode='w') as centered_file:
# call the function
# s1 = centre_text("spam and eggs")
# s2 = centre_text(12)
# s3 = centre_text("spam, spam and eggs")
# s4 = centre_text("spam, spam, spam and spam")
# s5 = centre_text("first", "second", 3, 4, "spam", sep=':')
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)

with open("menu", "w") as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    print(centre_text(12), file=menu)
    s3 = centre_text("spam, spam and eggs")
    print(s3, file=menu)
    print(centre_text("spam, spam, spam and spam"), file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=':')
    print(s5, file=menu)
