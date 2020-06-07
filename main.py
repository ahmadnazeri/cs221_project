
import time

from os import listdir
from os.path import isfile, join

import chess

from data.data import Dataset
from engine.engine import Engine

def main(clean_directory="resources/clean_data"):
    initial_time = time.time()

    clean_files = [f for f in listdir(clean_directory) if isfile(join(clean_directory, f)) and "2" in f]

    for file in clean_files:
        results = []
        print(f"processing {file} file")
        dataset = Dataset(f"{clean_directory}/{file}")

        data_points = dataset.get_data()

        count = 1
        for data_point in data_points:
            start = time.time()
            print(f"\tlooking at {count}:{len(data_points)}")
            chess_engine = Engine(data_point.board, data_point.color, depth=data_point.mate_in*2, algorithm="alpha-beta")
            result_moves = chess_engine.find_next_move()

            moves_to_mate = len(result_moves) // 2 + 1

            duration = (time.time() - start)
            print(f"\t\tfound mate in {moves_to_mate} moves; expecting {data_point.mate_in} in {duration} seconds")

            result_moves_string = [str(move) for move in result_moves]

            results.append((data_point.board.fen(), "->".join(result_moves_string), moves_to_mate, data_point.mate_in, duration))

            count += 1
            # if count > 10:
            #     break

        output_name = file.split("/")[-1].split(".")[0]
        output_path = f"resources/results/{output_name}_results.csv"

        print(f"downloading results to {output_path}")
        with open(output_path, "w") as f:
            f.write("fen,sequence_of_moves,found_mate,best_mate,difference,compute_duration\n")

            for result in results:
                f.write(f"{result[0]},{result[1]},{result[2]},{result[3]},{int(result[3]) - result[2]},{result[4]}\n")


    print("_"*80)
    print(f"total time: {(time.time() - initial_time)/60} minutes")

if __name__ == '__main__':
    main()