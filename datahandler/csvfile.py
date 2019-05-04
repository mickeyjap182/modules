import os
import csv

class Formatter():
    DEL_COM = ','
    LINE_LF = '\n'
    UTF_8 = 'utf-8'
    DBL_QUOTE = '"'

    def __init__(self, *args, **kwargs):
        """
        delimiter: delimiter of column
        line_sep: separater of line as record
        """
        self.delimiter = kwargs['delimiter'] if 'delimiter' in kwargs else Formatter.DEL_COM
        self.quotechar = kwargs['quotechar'] if 'quotechar' in kwargs else Formatter.DBL_QUOTE
        self.line_sep = kwargs['line_sep'] if 'line_sep' in kwargs else Formatter.LINE_LF
        self.charset = kwargs['charset'] if 'charset' in kwargs else Formatter.UTF_8

class Writer():
    def __init__(self):
        """
        Not Implements
        """
        pass
    def write(self, formatter):
        pass

class Reader():
    def __init__(self):
        """
        Not Implements
        """
        pass


class Csv():
    def __init__(self, formatter=None):
        """
        delimiter: delimiter of column
        line_sep: separater of line as record
        """
        if formatter is None:
            self.form = Formatter()
        else:
            self.form = formatter


    def write(self, file_path, contents, headers=None):
        """ write file """
        is_addtional = os.path.isfile(file_path)
        with open(file_path, 'a', newline=self.form.line_sep) as csv_file:
            writer = csv.writer(
                csv_file,
                delimiter=self.form.delimiter,
                quotechar=self.form.quotechar,
                quoting=csv.QUOTE_MINIMAL
            )
            if headers is not None and not is_addtional:
                writer.writerow(headers)
            for content in contents:
                writer.writerow(content)
        return True

    def read(self, file_path, headers=None):
        """ read file """
        contents = []
        with open(file_path, "r", newline=self.form.line_sep) as csv_file:
            reader = csv.reader(
                csv_file,
                delimiter=self.form.delimiter,
                quotechar=self.form.quotechar,
                quoting=csv.QUOTE_MINIMAL
            )
            for n, row in enumerate(reader):
                if headers is not None and n == 0 :
                     continue
                contents.append(row)

        return contents
