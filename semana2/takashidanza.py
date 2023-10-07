class Dance:

    def __init__(self, string):
        self.string = string

    def is_easy_to_perform(self):
        for i, char in enumerate(self.string):
            if i == 0 and char not in "RUD":
                return False
            elif i % 2 == 0 and char not in "LUD":
                return False
            elif i % 2 == 1 and char not in "RUD":
                return False
        return True


def main():
    string = input()
    dance = Dance(string)
    print("Yes" if dance.is_easy_to_perform() else "No")


if __name__ == "__main__":
    main()
