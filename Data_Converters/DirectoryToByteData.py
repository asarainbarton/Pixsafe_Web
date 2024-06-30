import os, sys


def extractByteFileData(filePath):
    """
    Extracts the data from a given file and returns its contents in byte format.
    :param filePath: The path to the file, whose contents will be extracted.
    :return: The contents of the file in byte format.
    """
    try:
        with open(filePath, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print("Error - Specified path to data that you want copied and hidden does not exist. (Path Name: '" + str(filePath) + "')")
        sys.exit(1)

    return data


def getByteData(path):
    """
    Recursively gets the byte data of an entire directory's contents, stored as a dictionary.
    :param path: The path to the content(s) to be stored.
    :return: The dictionary, containing all contents of the specified directory. The keys are the file/folder names.
    If a file, the value is the contents of the file in byte format. If a folder, the value is another dictionary
    used to represent the contents of that subpath.
    """
    byte_data_list = {}

    # True if the path specified leads directly to a file
    if not os.path.isdir(path):
        fileName = os.path.basename(path)
        byte_data_list[bytes(fileName, 'utf-8')] = extractByteFileData(path)
        return byte_data_list

    # Otherwise, the path leads to a folder, which will be examined recursively
    folderName = os.path.basename(path)
    byte_data_list[bytes(folderName, 'utf-8')] = getByteData_Implementation(path)

    return byte_data_list


def getByteData_Implementation(folder_path):
    """
    Gets the byte data of the contents listed in the current given folder path, stored as a dictionary. (Part of getByteData)
    :param folder_path: The path to the current folder for processing.
    :return: The dictionary representation of all the contents inside the current folder.
    """
    byte_data_list = {}

    for sub_dir_name in sorted(os.listdir(folder_path)):
        sub_dir_path = os.path.join(folder_path, sub_dir_name)

        # True if the current item being looked at in the folder is itself another folder
        if os.path.isdir(sub_dir_path):
            byte_data_list[bytes(sub_dir_name, 'utf-8')] = getByteData_Implementation(sub_dir_path)
            continue
        
        # Otherwise, the current item is a file
        byte_data_list[bytes(sub_dir_name, 'utf-8')] = extractByteFileData(sub_dir_path)
    
    return byte_data_list