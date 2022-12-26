
# TODO: [OPTIONAL] Implement logger and move responsibility from CodeWriter, VMTranslator and Parser to Logger.
class Logger(object):
    def __init__(self, root_file: str):
        self.root_file = root_file.split('/')[-1].split('.')[0]
        self._indent_interval = 5

    def log_session(self, stdout: bool=True, header: bool=False) -> None:
        pass

    def comment_codeblock(self, is_labeled=False) -> str:
        pass