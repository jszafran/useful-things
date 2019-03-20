import os
import csv


class SuperSizeMe:
    def __init__(self):
        self.data = []
        self.header = []
        self._input_file_path = None
        self._input_file_size = None
        self._output_size = None

    def read_csv(self, path, header=True):
        try:
            with open(path, 'r') as input:
                data = csv.reader(input)
                self._input_file_path = path
                self._input_file_size = os.path.getsize(self._input_file_path) / 1024 / 1024  # get size in MBs
                if header:
                    self.header = next(data)
                for line in data:
                    self.data.append(line)
        except FileNotFoundError:
            print(f'File does not exist at: {path}')
        except:
            print('Cannot load the file :(.')
        return self

    def expand_to(self, size):
        if not self._input_file_size:
            print('Please ensure you have used method \'read_csv\' to load input data.')
            return self
        if not isinstance(size, int) and size < self._input_file_size:
            print(f'Request output size: {size}mb, is smaller than input size: {self._input_file_size}mb.')
            return self

        self._output_size = size
        return self

    def save_at(self, output_path):
        if os.path.exists(output_path):
            print('File already exists. Please choose another path.')
            return self
        if not self._input_file_path:
            print('Please ensure you have used method \'read_csv\' to load input data.')
            return self

        iterations = int(round(self._output_size / self._input_file_size, 0) * 1.1)
        with open(output_path, 'w') as output:
            writer = csv.writer(output)

            if self.header:
                writer.writerow(self.header)

            for i in range(iterations):
                writer.writerows(self.data)
        print('Success!')

