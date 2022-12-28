import os.path
import time
from Command import Command


class Logger(object):
    def __init__(self, out_file: str, prog_path: str):
        self._out = out_file
        self._prog_path = prog_path
        self._indent_interval = 5 * ' '
        self._symbols = self.symbols()

    @staticmethod
    def comment_codeblock(cmd: Command, codeblock: str) -> str:
        """
        Append Comment on produces asm code block
        Args:
            cmd (Command) - the command object which asm code produced from
            codeblock (str) - the asm codeblock produced from the command
        Returns: (str) commented code block
        """
        return "\n".join(['', '// For VM Command {}', '//  Produce {} ASM CodeBlock',
                          codeblock]).format(cmd.__str__(), cmd.command_type)

    def log_session(self, vm_files: list, vm_parsed: int, asm_produced: int, is_dir: bool,
                    stdout: bool = True, header: bool = False) -> None:
        """
        Generate Log form translation session info.
        Args:
            vm_files (list): vm files detected in program path
            vm_parsed (int): number of parsed lines,
            asm_produced (int): number of asm code lines produced
            is_dir (bool): True if program path is dir, else False
            header (bool): if true append info header to the head of produced .asm file
            stdout (bool): if true print translation session info to stdout.
        Returns: None.
        :param is_dir:
        """
        file = 'vm files in {}'.format(os.path.basename(self._prog_path).replace('.asm', '')) if is_dir \
            else os.path.basename(self._prog_path).replace('.asm', '.vm')
        session_time = time.ctime()
        vm_files = ", ".join([os.path.basename(i) for i in vm_files])
        log_msg = "\n".join(['',
                             '{sep}  {s_time}  {sep}',
                             'VMTranslation Session - Translation of {file} to HackAssembly code.',
                             '{info} Detected .vm files - {files}',
                             '{main} Translation end successfully.',
                             '{good} {parsed} VM Code lines parsed.',
                             '{good} {produced} Assembly Code lines produced.',
                             '{good} Translation ration {ratio} has been reached.',
                             3 * '{sep}']).format(**self._symbols, file=file, s_time=session_time, parsed=vm_parsed,
                                        produced=asm_produced, ratio=asm_produced/vm_parsed, files=vm_files)

        if stdout: print(log_msg)
        if header:
            with open(self._out, 'r') as f:
                content = f.readlines()
            with open(self._out, 'w') as f:
                f.write(log_msg.replace("\n", "\n// ") + 2 * "\n")
                f.writelines(content)

    @staticmethod
    def symbols() -> dict:
        return {'info': '[>>] ',
                'good': '     [+] VMTranslator: ',
                'bad': '[-] VMTranslator: ',
                'main': '  [>] VMTranslator: ',
                'sep': 28 * '-',
                'indent': ' ',
                }
