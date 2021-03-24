FROM ubuntu
RUN apt-get update && apt-get install python3 -y
RUN mkdir ~/source_dir ~/target_dir
RUN  touch ~/source_dir/file1.txt ~/source_dir/file2.txt ~/source_dir/file3.txt
COPY copy_files_process.py root/
CMD ["python3", "copy_files_process.py"]
