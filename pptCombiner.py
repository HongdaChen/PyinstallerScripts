from win32com.client import Dispatch
import os
import re

directory=input("please input the ppt direcotry:\n")
output_dir=input("please input the output ppt direcotry:\n")

file_list=os.listdir(directory)
ppt_list=[i for i in file_list if i[-5:]=='.pptx'or i[-4:]=='.ppt']
print("\n*********找到的所有ppt文件*********\n")
print(ppt_list)

print("每个文件名中必须含有数字")
dic={int(re.findall(r'([0-9]{1,})',ppt)[0]):ppt for ppt in ppt_list}
sort_list=sorted(dic.items(),key=lambda k:k[0])
list_dir=[sort_list[i][1] for i in range(len(sort_list))]
print("\n*********排序所有ppt文件*********\n")
print(list_dir)

list_ab_dir=[directory+"\\"+item for item in list_dir]


def join_ppt(alldirs,output_dir):
    ppt = Dispatch('PowerPoint.Application')
    ppt.Visible = 1 
    ppt.DisplayAlerts = 0  
    pptA = ppt.Presentations.Open(alldirs[0])
    total_num=len(pptA.Slides)
    test_num=len(pptA.Slides)
    error_pages=["这里记录总页面和合并后的页面"]
    for dir in alldirs[1:len(alldirs)]:
        pptB = ppt.Presentations.Open(dir)
        numB=len(pptB.Slides)
        test_num+=numB
        count = 1
        while count<=numB:
            pptB.Slides(count).Copy()
            count+=1
            total_num+=1
            try:
                pptA.Slides.Paste()
            except:
                print("\n"+dir+"；第"+str(count)+"页失败\n")
                if count!=1:
                    print("重新copy本页，如果程序顺利执行，那么本页可以包含在结果文件中")
                    count-=1
                    total_num-=1
                else:
                    print("\n第一页出错，需要手动复制\n")
                    error_pages.append(dir+"；第"+str(count)+"页失败,在总文档中的位置是第"+total_num+"页")
        pptB.Close()
           
    #设置合并后ppt的路径！
    pptA.SaveAs(output_dir+"\\merge_result.pptx") 
    pptA.Close()
    ppt.Quit()
    
    error_pages.append("\n\n合并了的总页面数："+str(total_num)+";但合并之前总页面数："+str(test_num))
    for i in error_pages:
        print(i)
    

    
join_ppt(list_ab_dir,output_dir)


input("press <Enter> to quit")