
class Logger:
    """
    A helper class to redirect print statements to both console and,
    conditionally, to a log file based on the selected mode.
    """
    def __init__(self, filepath, original_stdout, mode='all'):
        self.terminal = original_stdout
        self.logfile = open(filepath, 'w', encoding='utf-8')
        self.mode = mode
        # This is the specific string the logger looks for to identify a conflict message.
        self.conflict_identifier = "⚠️ Conflict:"
        self.duplicate_identifier = "🚫 Duplicate:"

    def write(self, message):
        # Always write every message to the console terminal.
        self.terminal.write(message)

        # Conditionally write to the log file based on the mode.
        if self.mode == 'all':
            self.logfile.write(message)
        elif self.mode == 'conflicts_only':
            # NOTE: This logic is tied to the format of the conflict print statement.
            if message.strip().startswith(self.conflict_identifier):
                self.logfile.write(message+'\n')
        elif self.mode == 'duplicates_only':
            if message.strip().startswith(self.duplicate_identifier):
                self.logfile.write(message+'\n')

    def flush(self):
        self.terminal.flush()
        self.logfile.flush()

    def close(self):
        self.logfile.close()
