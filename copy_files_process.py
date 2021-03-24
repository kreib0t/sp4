from multiprocessing import Process
from os import listdir, getpid, getppid
from os.path import join, isfile
from shutil import copy2


def copy_file_to_dir(source_file_path: str, target_dir_name: str):
    process_pid = getpid()
    print("Child process. Pid: {}. PPid: {}.".format(process_pid, getppid()))
    print("Start to copy: {} to {}".format(source_file_path, target_dir_name))
    copy2(source_file_path, target_dir_name)
    print("Process with {} done.".format(process_pid))


def copy_directory_in_process():
    source_dir = "./source_dir"
    target_dir = "./target_dir"
    print("Main process. Pid: {}.".format(getpid()))
    files = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]

    for file in files:
        child_process = Process(target=copy_file_to_dir, args=(join(source_dir, file),
                                                               target_dir))
        child_process.start()
        child_process.join()
    print("Main process done.")


if __name__ == '__main__':
    copy_directory_in_process()
