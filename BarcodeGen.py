# imports
import os
def RawList_Make():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    cnt = 0
    for i in range(len(letters)):
        for j in range(len(letters)):
            if cnt == 5:
                print('\n')
                print(str('0')+str(i+1)+str(j+1)+str('00000000'))
                cnt = 0
            else:
                print(str('0')+str(i+1)+str(j+1)+str('00000000'))
            cnt += 1

def List_Process():
    # take processed barcode image files and reduce to just [letter][number]
    cwd = os.getcwd()+'/Codes'
    for file in os.listdir(cwd):
        os.renames(cwd+'/'+file, cwd+'/'+file[2:])

def ImageProcess():
    cwd = os.getcwd() + '/Resources/Pieces'
    print(cwd)
    for file in os.listdir(cwd):
        os.renames(cwd + '/' + file, cwd + '/' + file[:3] + '.gif')
        print(file)

if __name__ == '__main__':
    ImageProcess()

