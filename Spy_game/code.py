# --------------
##File path for the file 
file_path 

# function to read file
def read_file(path):
    file = open( path, 'r' )
    sentence = file.readline()
    file.close()
    return sentence

# Calling function read_file(path)
sample_message = read_file(file_path)


# --------------
#Code starts here

#paths of files
file_path_1
file_path_2

# calling read_file(path)
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

# printing message_1 and message_2
print(message_1, message_2)

# defining fuse_msg()
def fuse_msg(message_a , message_b):
    return str((int(message_b))//(int(message_a)))

# calling fuse_msg()
secret_msg_1 = fuse_msg(message_1, message_2)


# --------------
#Code starts here

# file path
file_path_3

# calling read_file()
message_3 = read_file(file_path_3)

# printing message
print(message_3)

# defining substitute_msg()
def substitute_msg(message_c):
    if ( message_c == 'Red'):
        sub = 'Army General'
    elif ( message_c == 'Green'):
        sub = 'Data Scientist'
    elif ( message_c == 'Blue'):
        sub = 'Marine Biologist'
    return sub

# calling substitute_msg()
secret_msg_2 = substitute_msg(message_3)



# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

#print(message_4, message_5)

def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [i for i in a_list if ( i not in b_list)]
    sep =' '
    final_msg=sep.join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4, message_5)




# --------------
# file path
file_path_6

# calling function read_file()
message_6 = read_file(file_path_6)

# printing message_6 
print(message_6)

# Creating function extract_msg()
def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x: (len(x)%2==0)
    b_list = filter(even_word,a_list)
    sep = ' '
    final_msg = sep.join(b_list)
    return final_msg

# calling extract_msg
secret_msg_4 = extract_msg(message_6)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

# preparing final path
final_path= user_data_dir + '/secret_message.txt'

# preparing secret message
secret_msg = ' '.join(message_parts)

# defining write_file()
def write_file(secret_msg, path):
    file_given = open(path, 'a+')
    file_given.write(secret_msg)
    file_given.close()

# calling write_file()
write_file(secret_msg,final_path)

# reading and displaying contents of final_path
read_file = open ( final_path,'r')
print(read_file.readline())




