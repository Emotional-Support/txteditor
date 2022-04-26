import os
from .errors import InvalidFilePathError, InvalidFileTypeError


class Txt:

    """
    Processes .txt files into lists for convinience.

    First instantiate the class with the path of the .txt file,

    Then use methods on it. Duh...

    # Attributes
    ---------

    ``path``: The Path Of The File

    ``id``: The File Name
    """

    files = 0

    def __init__(self, path: str):
        self.path = path
        self.id = self.path.split("/")[-1]
        Txt.files += 1

    def unpack(self, list: list, gen=False):

        """
        # Usage Example
        ---------

        Unpacking jokes into a list: ::

                import scripting as SC
                import random

                jokes_list = []

                file = SC.Script("jokes.txt")
                file.unpack(jokes_list)

                print(random.choice(jokes_list))
        """
        if os.path.exists(self.path):
            if ".txt" in self.path:
                if gen == False:
                    with open(self.path, encoding="UTF8") as txt:
                        list_data = txt.readlines()
                    for item in list_data:
                        list.append(item)
                else:
                    with open(self.path, encoding="UTF8") as txt:
                        list_data = txt.readlines()
                    for item in list_data:
                        list.append(item)
                    list = (i for i in list)

            else:
                raise InvalidFileTypeError
        else:
            raise InvalidFilePathError
