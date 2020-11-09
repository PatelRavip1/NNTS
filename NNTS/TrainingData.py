

class TrainingData:
    def __init__(self):
        super().__init__()
        self.text_file = open("myTrainingDataFile.txt")

    def get_next_inputs(self):
        next_line = self.text_file.readline()
        if len(next_line.strip()) == 0:
            return [0, 0, 0]
        else:
            next_line_list = next_line.split(";")
            return [next_line_list[1], next_line_list[2], next_line_list[4]]

    def move_to_top_of_file(self):
        self.text_file.seek(0)

    def end_file_read(self):
        self.text_file.close()



















