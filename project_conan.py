import csv
import os
import sys

"""
This folder (ATM):
 1.takes an input file as an input in pycharm parameters.
 2.runs tesseract on the input
 3.prints a header indicating if the result the same or not
 4.if the result is Fail, an output file is created with the text identified from tesseract for 
   personal inspection.
 5.an overall report is present in the results file.
"""
DIR_PATH_INDEX = 1
IMAGE_NAME = 2
IMAGE_TEXT = 4
LANG_INDEX = 5
CONFIGS_INDEX = 6

_curr_dir = os.path.abspath(os.curdir)


def test_images(input_file, results_file):
    test_id = 1
    for file in input_file:
        try:
            file = list(filter(None, file))
            languages = file[LANG_INDEX]
            configs = file[CONFIGS_INDEX:]
            answer = file[IMAGE_TEXT]
            output_path = os.path.join(file[DIR_PATH_INDEX], file[IMAGE_NAME].replace(".png", ""))

            file_path = os.path.join(_curr_dir, file[DIR_PATH_INDEX], file[IMAGE_NAME])

            configs_input = ""
            if languages:
                configs_input += languages
            else:
                configs_input += "-l eng"

            if configs:
                for x in configs:
                    configs_input += " -c "
                    configs_input += x + " "

            tesseracts_inputs = ' '.join(
                ["tesseract", "\"" + file_path + "\"", "\"" + output_path + "\"", configs_input])
            os.system(tesseracts_inputs)
            out_file = open(output_path + ".txt", "r", encoding="utf-8")
            file_buffer = out_file.read().strip()
            answer = answer.replace("\\n", "\n")
            out_file.close()
            if file_buffer == answer:
                result = "PASS"
                # deleting output files for PASS results
                os.remove(output_path + ".txt")
            else:

                result = "FAIL"
                os.remove(output_path + ".txt")

            test_msg = format("{:>1}\t {:<50}\t {:>4}".format("Test#", "Command line", "Result"))
            out_line = format("{:>1}\t {:<50}\t {:>4}".format(test_id, tesseracts_inputs, result))
            print(test_msg)
            print(out_line)
            results_file.write(out_line)
            results_file.write("\n")
            test_id += 1
        except IndexError:
            pass
    results_file.close()


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage:\n1.CSV input file of the following format: "
              "path,filename,image text,optional:lang,optional:configurations 1-6")
        exit("Input parameter error")
    test_msg = format("{:>1}\t {:<50}\t {:>4}".format("Test#", "Command line", "Result"))
    results_file = open("test_results.txt", "w")
    results_file.write(test_msg)
    results_file.write("\n")
    print(test_msg)
    with open(sys.argv[1], 'r', newline='', encoding='utf-8') as csvfile:
        # opening the file
        csv_reader = csv.reader(csvfile, delimiter=",")
        # skipping the header
        next(csv_reader, None)
        test_images(csv_reader, results_file)
