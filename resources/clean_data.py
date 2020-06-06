
import csv

def main():
    files_to_clean = [
        "raw_data/2_move_mate_puzzles.txt",
        "raw_data/3_move_mate_puzzles.txt",
        "raw_data/4_move_mate_puzzles.txt"
    ]


    for file in files_to_clean:
        print(f"cleaning the {file} raw file")
        cleaned_data = [["board","color","number_of_moves_to_mate","move_sequence"]]
        
        with open(file, "r") as f:
            file_data = f.readlines()

            line_number = 0
            moves_to_mate = int(file.split("/")[-1].split("_")[0])

            while line_number < len(file_data):
                line = file_data[line_number]

                if line.count("/") > 2:
                    color = "white" if line.split(" ")[1]=="w" else "black"

                    new_line = [line.strip(), 
                                color,
                                moves_to_mate,
                                file_data[line_number+1].strip()]

                    cleaned_data.append(new_line)

                    line_number += 2
                else:
                    line_number += 1

        original_name = file.split('/')[-1].split(".")[0]
        clean_file_name = f"clean_data/{original_name}.csv"

        with open(clean_file_name, "w") as clean_file:
            wr = csv.writer(clean_file, dialect='excel')
            wr.writerows(cleaned_data)

        print(f"raw file cleaned and outputed to {clean_file_name}")


if __name__ == '__main__':
    main()