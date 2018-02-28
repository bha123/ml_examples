import csv
import os
import shutil

# Function to read csv file and return the elements 
# in list
def read_csv(filename, file_permission ,delimiter):
    
    read_list = []
    
    with open(filename, file_permission ) as csvfile:
         file_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in file_reader:
        
             read_list.append(row[0].split(",")) 
    return read_list


# extract the filenames and id category
def categorize_items(list_of_elements , id_of_category):
    categories = []
    for item in list_of_elements:
        print item
	if item[id_of_category] in categories:
	    print (" Item is present" )
        else:
            categories.append(item[id_of_category])
    return categories 


# If file exist if not create it
def create_folder(path_dir):
    file_path = []
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
        file_path.append(path_dir)
    return file_path
  


# Create file names for a given list:
# Input file_list and output directory
def create_file(file_list, output_dir=os.getcwd(), output_dir_name="output"):

    file_dir = {}
    path_dir = os.path.join(output_dir,output_dir_name)
    file_path = []
    # Create output folder if not exists
    create_folder(path_dir)
    for file_name in file_list:
	path_var_folder = os.path.join(path_dir,file_name)
        file_path = create_folder(path_var_folder)
        file_dir[file_name] = path_var_folder
    return file_dir


# Copy files into the folders present in the list
def copy_files_into_folders(file_dir_dict, input_file, input_file_dir = os.getcwd()+'/train', category_id = 0, item_id = 1,input_dir = 'train',output_dir = os.getcwd(), output_dir_name="output", file_permission = 'rb', delimiter = ' '):
    # Extract filenames from file
    print file_dir_dict
    list_items =  read_csv(input_file, file_permission, delimiter)
    
    for item in list_items:
        # extract filepath for given category
        output_path = file_dir_dict[item[0]]
        input_file_path = os.path.join(input_file_dir,item[1])
        
        #copying file from source to destination
        shutil.copy2(input_file_path, output_path)


    
    




        
