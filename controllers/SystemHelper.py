import controllers.PageHelper as PageHelper


class SystemHelper:
    @staticmethod
    def yes_or_no(question):
        while "the answer is invalid":
            reply = str(input(question + ' (y/n): ')).lower().strip()
            if reply[:1] == 'y':
                return True
            elif reply[:1] == 'n':
                return False
            else:
                print("Only y/n allowed")


    @staticmethod
    def error(text):
        PageHelper.PageHelper.clear()
        print("---------------------------------------------------------------------------")
        print(text)
        input("Enter a key to continue")
