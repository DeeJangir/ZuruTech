import json
import argparse
import datetime


class PyLS:
    def __init__(self, arguments):
        self.arguments = arguments
        with open(arguments.file, "r") as fo:
            self.file_data = json.load(fo)

    def get_file_size(self, item) -> int | str:
        """
        returns human-readable file/directory size or int size
        """
        if self.arguments.H:
            size: int = item["size"]
            for unit in ["", "K", "M", "G"]:
                if size < 1024:
                    return f"{size:.1f}{unit}" if unit else size
                size /= 1024
            return size
        else:
            return item["size"]

    def mimic_ls(self) -> None:
        """
        parse command args to process file content to print on console
        """
        details: list = self.file_data["contents"]
        if self.arguments.path and self.arguments.path != "./":
            paths: list = self.arguments.path.strip("./").split("/")
            found_path: bool = False
            for path in paths:
                found_path = False
                for file_content in details:
                    if file_content["name"] != path:
                        continue
                    details = file_content["contents"] if file_content.get("contents") else [file_content]
                    found_path = True
            if not found_path:
                raise Exception(f'cannot access "{self.arguments.path}": No such file or directory')

        filter_type: str = self.arguments.filter
        if not self.arguments.A:
            details = [item for item in details if not item["name"].startswith(".")]

        if self.arguments.r:
            details = details[::-1]
        if self.arguments.t:
            details.sort(key=lambda x: x["time_modified"], reverse=True)
        if filter_type:
            if filter_type == "file":
                details = [x for x in details if x["permissions"].startswith("-")]
            elif filter_type == "dir":
                details = [x for x in details if x["permissions"].startswith("d")]
            else:
                raise Exception(
                    f'"{filter_type}" is not a valid filter criteria. Available filters are "dir" and "file"')

        for item in details:
            if self.arguments.l:
                timestamp = datetime.datetime.fromtimestamp(item["time_modified"]).strftime("%b %d %H:%M")
                size = self.get_file_size(item)
                print(f'{item["permissions"]} {size:>5} {timestamp} {item["name"]}')
            else:
                print(item["name"], end=" ")


parser = argparse.ArgumentParser(description="unix-ls like python program")
parser.add_argument("-A", action="store_true", help="Show all files including hidden files.")
parser.add_argument("-l", action="store_true", help="Show detailed file information.")
parser.add_argument("-r", action="store_true", help="Reverse the sorting order.")
parser.add_argument("-t", action="store_true", help="Sort files by time modified.")
parser.add_argument("--filter", help="Filter results by file or directory.")
parser.add_argument("-H", action="store_true", help="Show sizes in human readable format.")
parser.add_argument("path", nargs="?", default="./", help="Show given path's sub directory result")
parser.add_argument("--file", nargs="?", default="structure.json", help="To pass file path")
args = parser.parse_args()

if __name__ == "__main__":
    PyLS(args).mimic_ls()


def main():
    PyLS(args).mimic_ls()
