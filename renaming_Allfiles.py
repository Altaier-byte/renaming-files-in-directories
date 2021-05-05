
# importing os module
import os
#import datetime
#Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')
# Function to rename multiple files
def main():
 path = input("Input path to directory: ")
 f_Name = input("Enter the first part of the file name: ")
 f_extension = input("Enter the file extension: ")

 for count, filename in enumerate(os.listdir(path)):
        dst = f_Name + '_' + str(count) + '.' +f_extension
        src =path + filename
        dst =path + dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()

