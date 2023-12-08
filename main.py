import statzcw
from statzcw import zcount, zmean, zcorr, zmode, zstdev, zmedian, zstderr, zvariance
import csv
import glob
import math
from statistics import mean, median, mode, stdev, variance, correlation


# Function to get the list of csv_files to calculate stats for
def read_data_file(file: str):
    path = file
    csv_files = glob.glob(path + "/*.csv")

    for num in range(0, len(csv_files)):
        new_file = csv_files[num].replace("/Users/mike/projects/zcw_python/pandas_labs/Py-BasicStats/", "")
        csv_files[num] = new_file

    return csv_files


# Function to get the lists or stats calculated, need to decide, for each csv file in the list
def read_data_sets(files: list):

    for file in files:
        with open(file, 'rt') as f:
            data = csv.reader(f)
            print(f'For {file} the lists are:')
            line_count = 0
            x_list = []
            y_list = []
            for row in data:
                if line_count == 0:
                    line_count += 1
                else:
                    x_list.append(int(row[0]))
                    y_list.append(float(row[1]))
                    line_count += 1
        run_my_stats(x_list, y_list)
        run_py_stats(x_list, y_list)


# Helper function to print statistics on each list from the files
def run_my_stats(listx: list, listy: list):

    print("Calculating my statistics...")
    xcount = statzcw.zcount.zcount(listx)
    xmean = statzcw.zmean.zmean(listx)
    xmedian = statzcw.zmedian.zmedian(listx)
    xmode = statzcw.zmode.zmode(listx)
    xstdev = statzcw.zstdev.zstdev(listx)
    xstderr = statzcw.zstderr.zstderr(listx)
    xvar = statzcw.zvariance.zvariance(listx)
    print(f'X: Count = {xcount}, Mean = {xmean}, Median = {xmedian}, Mode = {xmode},'
          f'Std Dev = {xstdev}, Std Err = {xstderr}, Var = {xvar}')

    ycount = statzcw.zcount.zcount(listy)
    ymean = statzcw.zmean.zmean(listy)
    ymedian = statzcw.zmedian.zmedian(listy)
    ymode = statzcw.zmode.zmode(listy)
    ystdev = statzcw.zstdev.zstdev(listy)
    ystderr = statzcw.zstderr.zstderr(listy)
    yvar = statzcw.zvariance.zvariance(listy)
    print(f'Y: Count = {ycount}, Mean = {ymean}, Median = {ymedian}, Mode = {ymode},'
          f'Std Dev = {ystdev}, Std Err = {ystderr}, Var = {yvar}')

    xycorr = statzcw.zcorr.zcorr(listx, listy)
    print(f'X, Y Correlation: {xycorr}')


# Helper functions to print the stats package method results
def run_py_stats(listx: list, listy: list):

    print("\n Calculating python statistics...")
    x_count = len(listx)
    x_mean = mean(listx)
    x_median = median(listx)
    x_mode = mode(listx)
    x_stdev = stdev(listx)
    x_stderr = stdev(listx) / math.sqrt(len(listx))
    x_var = variance(listx)
    print(f'X: Count = {x_count}, Mean = {x_mean}, Median = {x_median}, Mode = {x_mode},'
          f'Std Dev = {x_stdev}, Std Err = {x_stderr}, Var = {x_var}')

    y_count = len(listy)
    y_mean = mean(listy)
    y_median = median(listy)
    y_mode = mode(listy)
    y_stdev = stdev(listy)
    y_stderr = stdev(listy) / math.sqrt(len(listy))
    y_var = variance(listy)
    print(f'Y: Count = {y_count}, Mean = {y_mean}, Median = {y_median}, Mode = {y_mode},'
          f'Std Dev = {y_stdev}, Std Err = {y_stderr}, Var = {y_var}')

    x_y_corr = correlation(listx, listy)
    print(f'X, Y Correlation: {x_y_corr} \n')


# Control flow to run this program in its own directory
file_list = read_data_file("/Users/mike/projects/zcw_python/pandas_labs/Py-BasicStats")
# print(file_list)
read_data_sets(file_list)
