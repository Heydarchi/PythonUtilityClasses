from SystemUtility import *


class FileEnumeration:
    def __init__(self, path) -> None:
        self.path = path
        self.listContexts = list()
        self.listTeFiles = list()
        self.enumerate_policy_files(self.path)

    def enumerate_policy_files(self, path):
        self.listContexts = SystemUtility.get_list_of_files("./test",
                                                            "*_contexts")
        self.listTeFiles = SystemUtility.get_list_of_files("./test",
                                                           "*.te")


if __name__ == "__main__":
    flEnum = FileEnumeration('.')
    print('-- List of *_contexts files:')
    print(flEnum.listContexts)
    print('-- List of *.te files:')
    print(flEnum.listTeFiles)
