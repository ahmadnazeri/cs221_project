import csv
from os import listdir
from os.path import isfile, join

import chess

from data.data import Dataset
from engine.engine import Engine

def main(clean_directory="resources/clean_data"):
    clean_files = [f"{clean_directory}/2_move_mate_puzzles.csv"]#[f for f in listdir(clean_directory) if isfile(join(clean_directory, f))]

    for file in clean_files:
        print(f"processing {file} file")
        dataset = Dataset(file)

        data_points = dataset.get_data()

        count = 1
        for data_point in data_points:
            print(f"\tlooking at {count}:{len(data_points)}")
            chess_engine = Engine(data_point.board, data_point.color, depth=5)
            result_moves = chess_engine.find_next_move()

            moves_to_mate = len(result_moves) // 2 + 1

            print(f"\t\tfound mate in {moves_to_mate} moves; expecting {data_point.mate_in}")

            count += 1

            if count > 3:
                return False


if __name__ == '__main__':
    main()