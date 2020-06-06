
from collections import namedtuple
import csv

import chess

Data = namedtuple("Data", ["board", "color", "mate_in", "move_sequence"])


class Dataset:
    def __init__(self, file_name):
        self._file_name = file_name
        self._data = self._retrieve_data_from_file()

    def _retrieve_data_from_file(self):
        data = []

        with open(self._file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    data_point = Data(
                                    board=chess.Board(row["board"]), 
                                    color=row["color"], 
                                    mate_in=row["number_of_moves_to_mate"],
                                    move_sequence=row["move_sequence"]
                                )
                    data.append(data_point)
                line_count += 1

        return data


    def get_data(self):
        return self._data