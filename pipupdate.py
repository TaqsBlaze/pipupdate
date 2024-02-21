import os
import sys


class Updater:

    def __init__(self):
        self.WORKING_DIR = "~"
        self.CACHE = []
        self.CACHE_INSTALL = []
        self.CACHE_FILE = "pack-list.list"
        self.PACKAGE_FILE = "packages.pack"

    def packages(self) -> bool:

        try:
            os.system(f"cd {self.WORKING_DIR}")
            os.system(f"pip freeze > {self.CACHE_FILE}")

            with open(self.CACHE_FILE,"r") as paks:
                packlist = paks.read().strip("\n").split("==")

                for pack in packlist:
                    cache_list = pack.split("\n")
                    for pack in cache_list:
                        self.CACHE.append(pack)

            for item in self.CACHE:
                if "." not in item:
                    self.CACHE_INSTALL.append(self.CACHE.pop(self.CACHE.index(item)))

            with open(self.PACKAGE_FILE,"w") as package_file:
                for package in self.CACHE_INSTALL:
                    package_file.write(package + "\n")

            return True
        except Exception as error:
            print(error)
            return False

    def update(self) -> bool:

        try:
            os.system(f"pip install -U -r {self.PACKAGE_FILE}")
            return True
        except Exception as error:
            return False
        



package_updator = Updater()

if package_updator.packages():
    package_updator.update()
else:
    print("Something went wrong")