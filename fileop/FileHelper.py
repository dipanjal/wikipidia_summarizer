from pathlib import Path



class FileHelper:

    def write_in_file(self, content, file_name):
        try:
            file_dir = Path('~/projects/python/wikipidia_summarizer/output').expanduser()
            file_dir.mkdir(parents=True, exist_ok=True)

            # date = datetime.datetime.today().strftime("%B %d, %Y")
            file_name = file_name + '.txt'
            log_file_path = file_dir / Path(file_name)
            with open(log_file_path, 'w+') as file:
                file.write(content)
            return log_file_path
        except Exception as ex:
            print(ex)
            return ''

    def read_from_file(self,file_path):
        file = Path(file_path).expanduser()
        with open(file, 'r') as file:
            return file.read()
