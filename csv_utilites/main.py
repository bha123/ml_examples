import csv
import utils_csv as us

file_list =  us.create_file( us.categorize_items(us.read_csv('test.csv', 'rb', ' '), 0))
us.copy_files_into_folders(file_list, "test.csv")
  

