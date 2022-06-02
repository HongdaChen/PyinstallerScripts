import os, shutil, time
import logging
############################################## log ##########################################################
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

# logger.addHandler(handler)
logger.addHandler(console)

############################################## do ##########################################################

root_dir = "F:/cache/"
target_dir = "F:/"
file_list = os.listdir(root_dir)
# tell user if there exists files in the given folder
flag = 0
today_total = 0
for i in file_list:
    # only move pdf
    if i.endswith(".pdf"):
        today_total+=1
        flag = 1
        file_path = os.path.join(root_dir,i)
        # get pdf's downloaded date 
        filemt = time.localtime(os.stat(file_path).st_mtime) # st_mtime: the last time which has been modified
        format_date = time.strftime("%Y-%m-%d", filemt)
        # create the date folder
        today_folder = os.path.join(target_dir,format_date)
        try:
            while not os.path.exists(today_folder):
                os.mkdir(today_folder)
        except:
            print("{0} failed to be created!".format(today_folder))
        # move .pdf from cach to coresponding date folder
        try:
            shutil.move(file_path,today_folder)
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            logger.error("Faild to move", exc_info=True)

if flag == 0:
    print("there are no files in the folder:{0}".format(root_dir))
    
print("work done!")
print("moved {0} files".format(today_total))
input("press <Enter> to quit")