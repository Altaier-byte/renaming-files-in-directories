
# importing os module
import os
import datetime
Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')
# Function to rename multiple files
def main():
  
    for count, filename in enumerate(os.listdir("docs/")):
        dst ="Ali" + str(count) + '_' + str((Current_Date)) + ".txt"
        src ='docs/'+ filename
        dst ='docs/'+ dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
