import os
import sys
import subprocess
from dataclasses import dataclass, field


@dataclass
class FileInfo:
    name: str = ""
    size: int = 0
    lastModifies: str = ""
    created: str = ""
    md5: str = ""


class SystemUtility:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def getListOfFiles(path, pattern):
        result = subprocess.Popen(
            ['find', path, '-name', pattern], stdout=subprocess.PIPE).communicate()[0]
        result = str(result, encoding='utf-8').split('\n')
        result = [item for item in result if item]
        return result

    @staticmethod
    def getFileInfo(path):
        file_info = FileInfo()
        file_info.name = path
        file_info.size = os.path.getsize(path)
        file_info.lastModifies = os.path.getmtime(path)
        file_info.created = os.path.getctime(path)
        return file_info

    @staticmethod
    def deleteFiles(path):
        os.remove(path)


if __name__ == "__main__":
    sysUtil = SystemUtility()
    print(sysUtil.getListOfFiles("./test", "*_contexts"))
    print(sysUtil.getListOfFiles("./test", "*.te"))
