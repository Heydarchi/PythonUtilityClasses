import os
import sys
import subprocess


class FileWriter:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def write_file(filePath, content):
        return open(filePath, "w+").write(content)

    @staticmethod
    def write_file_append(filePath, content):
        return open(filePath, "a+").write(content)

    @staticmethod
    def write_list_to_file(filePath, list_of_str):
        return open(filePath, "w+").write("\n".join(list_of_str))


if __name__ == "__main__":
    print(sys.argv)
    fileWriter = FileWriter
    print(fileWriter.write_file(sys.argv[1], "Yohoooooooooooo"))
    listOfStr = list()
    listOfStr.append("Haha")
    listOfStr.append("Hehe")
    listOfStr.append("Hoho")
    print(fileWriter.write_list_to_file(sys.argv[1] + "_1", listOfStr))
