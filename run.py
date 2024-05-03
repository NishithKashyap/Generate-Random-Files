from generate_random_files import create_file
import multiprocessing

if __name__ == '__main__':
    number_of_files = 2
    output_folder = 'random_files'

    min_file_size = 5 * 1024 * 1024 # 5 MB
    max_file_size = 1024 * 1024 * 1024 # 1 GB

    processes = []
    for i in range(number_of_files):
        process = multiprocessing.Process(target=create_file, args=(i,output_folder, min_file_size, max_file_size))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("File creation successful!")