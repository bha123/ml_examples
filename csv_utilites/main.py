import csv
import utils_csv as us

categorie_item = us.categorize_items(us.read_csv('test.csv', 'rb', ' '),0)
file_list =  us.create_file(categorie_item)
us.copy_files_into_folders(file_list, "test.csv")
us.split_dataset(categorie_item, file_list)
  

