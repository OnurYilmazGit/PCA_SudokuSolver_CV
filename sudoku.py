import cv2
import sys,glob
import numpy as np 
import natsort
from time import time
import matplotlib.pyplot as plt
from SudokuExtractor import extract_sudoku
from NumberExtractor import extract_number
import logging, os
logging.disable(logging.WARNING)

def sudokuAcc(gt, out):
    return (gt == out).sum() / gt.size * 100

def output(a):
    sys.stdout.write(str(a))

def display_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            cell = sudoku[i][j]
            if cell == 0 or isinstance(cell, set):
                output('0')
            else:
                output(cell)

            if j != 8:
                output(' ')
        output('\n')


def show_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()

def main(image_path):
    image = extract_sudoku(image_path)
    # show_image(image)
    grid = extract_number(image)
    print('Sudoku:')
    display_sudoku(grid.tolist())
    num_array = np.array(grid.tolist())
    return num_array
        

if __name__ == '__main__':
    image_dirs = 'images/*.jpg'
    data_dirs = 'dat_files/*.dat'
    IMAGE_DIRS = natsort.natsorted(glob.glob(image_dirs))
    DATA_DIRS = natsort.natsorted(glob.glob(data_dirs))
    total_acc = 0
    for i, (img_dir, dta_dir) in enumerate(zip(IMAGE_DIRS, DATA_DIRS)):
            gt = np.genfromtxt(dta_dir, skip_header=2, dtype=int, delimiter=' ')
            output_ = main(image_path = img_dir)
            total_acc = total_acc + sudokuAcc(gt, output_)
            total_acc2 = sudokuAcc(gt, output_)
            print('Accuracy of ' + img_dir + ' is: ' + '%' + str(int(total_acc2)))
            print('Total of Accuracy: ' + str(int(total_acc)) + '\n')


