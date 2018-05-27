class Comment(object):
    def __init__(self, author, text):
        self.author = author
        self.text = text

def add_comment(advice):
    commentauthor = input("Author name: ")
    commenttext = input("Comment text: ")
    comm1 = Comment(commentauthor, commenttext)
    is_not_valid = True
    while is_not_valid:
        grade = input("Set rate (0-5):")
        if grade.isdigit():
            if -1 < int(grade) < 6:
                is_not_valid = False
                advice.rated(int(grade), comm1)
            else:
                print("Rate is not between 0-5")
        else:
            print("This isn't even number ...")

