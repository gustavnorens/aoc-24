
def read_words(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split()

def read_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split('\n')