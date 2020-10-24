from multiprocessing import Pool
import os

def square(x):
    # calculate the square of the value of x
    return x*x

def download_hd_videos_with_sequence(bash_command):
    os.system(bash_command)



if __name__ == '__main__':

    # Using readlines() 
    file1 = open('download_all_hd_videos.sh', 'r') 
    lines = file1.readlines() 

    print(f"Num of sequences: ", len(lines))


    # # Output the dataset
    # print ('Dataset: ' + str(dataset))

    # # Run this with a pool of 5 agents having a chunksize of 3 until finished
    # agents = 5
    # chunksize = 3
    # with Pool(processes=agents) as pool:
    #     result = pool.map(square, dataset, chunksize)

    agents = 10
    chunksize = 1
    with Pool(processes=agents) as pool:
        result = pool.map(download_hd_videos_with_sequence, lines[:10], chunksize)

    # # Output the result
    # print ('Result:  ' + str(result))