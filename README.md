# Project_Connan
** The project is based on Tesseract, v5.0.0-alpha.20200328, running on Windows 10.**
This project which was built with a team, is goaled to debug a software called tesseract which is an open source OCR engine.

The files include:
* Project canan: the file which includes the code itself, in order for it to work, you have to:
  * download tesseract. v5.0.0-alpha.20200328
  * add it to your system path.
* The images folder, which contains multiple images used for testing purposes.
* The input CSV file, which has the path to all the images, plus the expected result for each image.
* The test results, which is a CSV file, that runs all images using the CMD, and compares the output of the program to the output of tesseract.
To run the program, simply clone the directory, give the input CSV as an argument and that is enough.

**The output is a file that has the testresults per image used (with the used CMD to create that test)**

