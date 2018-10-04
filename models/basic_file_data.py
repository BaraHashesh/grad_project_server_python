import os
import time


class BasicFileData:
    """
    Class used to extract the data from file objects and
    save them in order to exchange them between the server and client
    """
    path = None
    size = None
    last_modified = None
    directory = None

    def __init__(self, file_path=None):
        """
        Initialize method for the BasicFileData object
        :param file_path: The path for the file
        """
        if file_path is not None:  # check if path was passed
            self.path = os.path.abspath(file_path)
            self.directory = os.path.isdir(self.path)

            stats = os.stat(self.path)

            if self.is_directory():  # check if file is a directory
                total_size = 0

                for dir_path, dir_names, file_names in os.walk(self.path):  # iterate through folder levels
                    for file in file_names:  # iterate through files at each level
                        fp = os.path.join(dir_path, file)  # join the paths of the parent folder and the child file
                        total_size += os.path.getsize(fp)

                self.size = total_size
            else:
                self.size = stats.st_size

            self.last_modified = time.strftime('%d/%m/%Y', time.gmtime(stats.st_mtime))

    def is_directory(self):
        """
        Check if the file is a directory or not
        :return: Whether the the file is a directory or not
        """
        return self.directory
