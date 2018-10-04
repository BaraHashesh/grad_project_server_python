DOWNLOAD_MESSAGE = 0
UPLOAD_MESSAGE = 1
DELETE_MESSAGE = 2
BROWSE_MESSAGE = 3
ERROR_MESSAGE = 4
SUCCESS_MESSAGE = 5
FILE_INFO_MESSAGE = 6
STREAM_END_MESSAGE = 7


class Message:
    """
    Class used to create communication messages which
    will be used between the server and the client
    """
    type = None
    info = None

    def __init__(self):
        """
        Empty constructor for Message
        """
        pass

    def make_download_message(self, info):
        """
        Method used to convert the message into a download msg
        :param info: Is the extra info attached to the message
        """

        self.type = DOWNLOAD_MESSAGE
        self.info = info

    def make_upload_message(self, info):
        """
        Method used to convert the message into an upload msg
        :param info: Is the extra info attached to the message
        """

        self.type = UPLOAD_MESSAGE
        self.info = info

    def make_delete_message(self, info):
        """
        Method used to convert the message into a delete msg
        :param info: Is the extra info attached to the message
        """

        self.type = DELETE_MESSAGE
        self.info = info

    def make_browse_message(self, info):
        """
        Method used to convert the message into a browse msg
        :param info: Is the extra info attached to the message
        """

        self.type = BROWSE_MESSAGE
        self.info = info

    def make_error_message(self, info):
        """
        Method used to convert the message into an error msg
        :param info: Is the extra info attached to the message
        """

        self.type = ERROR_MESSAGE
        self.info = info

    def make_success_message(self, info):
        """
        Method used to convert the message into a success msg
        :param info: Is the extra info attached to the message
        """

        self.type = SUCCESS_MESSAGE
        self.info = info

    def make_file_info_message(self, info):
        """
        Method used to convert the message into a file info msg
        :param info: Is the extra info attached to the message
        """

        self.type = FILE_INFO_MESSAGE
        self.info = info

    def make_stream_end_message(self, info):
        """
        Method used to convert the message into a stream end msg
        :param info: Is the extra info attached to the message
        """

        self.type = STREAM_END_MESSAGE
        self.info = info

    def is_download_message(self):
        """
        Method used to check if the message is a download message
        :return: Whether the message is a download message or not
        """
        return self.type == DOWNLOAD_MESSAGE

    def is_upload_message(self):
        """
        Method used to check if the message is an upload message
        :return: Whether the message is an upload message or not
        """
        return self.type == UPLOAD_MESSAGE

    def is_delete_message(self):
        """
        Method used to check if the message is a delete message
        :return: Whether the message is a delete message or not
        """
        return self.type == DELETE_MESSAGE

    def is_browse_message(self):
        """
        Method used to check if the message is a browse message
        :return: Whether the message is a browse message or not
        """
        return self.type == BROWSE_MESSAGE

    def is_error_message(self):
        """
        Method used to check if the message is an error message
        :return: Whether the message is an error message or not
        """
        return self.type == ERROR_MESSAGE

    def is_success_message(self):
        """
        Method used to check if the message is a success message
        :return: Whether the message is a success message or not
        """
        return self.type == SUCCESS_MESSAGE

    def is_file_info_message(self):
        """
        Method used to check if the message is a file info message
        :return: Whether the message is a file info message or not
        """
        return self.type == FILE_INFO_MESSAGE

    def is_stream_end_message(self):
        """
        Method used to check if the message is a stream end message
        :return: Whether the message is a stream end message or not
        """
        return self.type == STREAM_END_MESSAGE