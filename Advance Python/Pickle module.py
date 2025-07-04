''' pickle module :- It is used to serialize and de-serialize objects. '''

import pickle

# Pickling : It is used to store data in a file by using pickle dump() function.

my_dict = {'Name': 'Gaurav', 
           'Age': '20', 
           'Gender': 'male', 
           'Village': 'pipola'}

# creating a file
my_file = "pickle.txt"

# Opening a file in write-binary(wb) mode
pickle_write = open(my_file, 'wb')

# dumping the data into a file
pickle.dump(my_dict, pickle_write)

# closing the file
pickle_write.close()


# Unpickling : It is used to retrieve data from a file by using pickle load() function.

# Opening a file in read-binary(rb) mode
pickle_read = open(my_file, 'rb')

# loading the data from the file
loaded_data = pickle.load(pickle_read)

# Printing the data
print(loaded_data)