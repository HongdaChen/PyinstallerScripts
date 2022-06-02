import base64
import os 
mode = input("please input your mode: T for temp, L for writing to disk:\n")
while True:
    choice = input("please input your choice: E for encode,D for decode,BE for batch encode,BD for batch decode,Q for quit\n")
    if choice == 'E':
        if mode == 'L':
            path = input("please input the file path which you want to encode with base64:\n")
            with open(path,"r",encoding="utf-8") as f:
                content=f.read()
            en_code = base64.b64encode(content.encode(encoding="utf-8"))
            print("the result is: \n{0}".format(en_code))
            with open("./encode_result.md","w",encoding="utf-8") as f:
                f.write(en_code.decode("utf-8"))
        elif mode == 'T':
            content = input("please input the contents which you want to encode with base64:\n")
            en_code = base64.b64encode(content.encode(encoding="utf-8"))
            print("the result is: \n{0}".format(en_code))
    elif choice == 'D':
        if mode == 'L':
            path = input("please input the file path which you want to decode with base64:\n")
            with open(path,"r",encoding="utf-8") as f:
                content=f.read()
            de_code = base64.b64decode(content)
            print("the result is: \n{0}".format(de_code.decode(encoding="utf-8")))
            with open("./decode_result.md","w",encoding="utf-8") as f:
                f.write(de_code.decode("utf-8"))
        elif mode == 'T':
            content = input("please input the contents which you want to decode with base64:\n")
            de_code = base64.b64decode(content)
            print("the result is: \n{0}".format(de_code.decode(encoding="utf-8")))
    elif choice == 'BE':
        root = input("please input the markdown directory which you want to encode with base64:\n")
#         root = r"C:\Users\chenhongda\Desktop\Diary-main\2018"
        li = os.listdir(root)
        try:
            new_path = os.path.join(root,"encoded")
            os.makedirs(new_path)
        except:
            print("{0} already exists!".format(new_path))
        li = [i for i in li if i.endswith(".md")]
        for i in range(len(li)):
            path = os.path.join(root,li[i])
            with open(path,"r",encoding="utf-8") as f:
                content=f.read()
            en_code = base64.b64encode(content.encode(encoding="utf-8"))
        #     print("the result is: \n{0}".format(en_code))
            with open(os.path.join(new_path,li[i]),"w",encoding="utf-8") as f:
                f.write(en_code.decode("utf-8"))
        print("encode OK!")
    elif choice == 'BD':
        root = input("please input the markdown directory which you want to decode with base64:\n")
        li = os.listdir(root)
        try:
            new_path = os.path.join(root,"decoded")
            os.makedirs(new_path)
        except:
            print("{0} already exists!".format(new_path))
        li = [i for i in li if i.endswith(".md")]
        for i in range(len(li)):
            path = os.path.join(root,li[i])
            with open(path,"r",encoding="utf-8") as f:
                content=f.read()
            de_code = base64.b64decode(content)
            with open(os.path.join(new_path,li[i]),"w",encoding="utf-8") as f:
                f.write(de_code.decode("utf-8"))
        print("decode OK!")
    elif choice == 'Q':
        break
    else:
        continue