import os

for folder in os.listdir('test_directory'):
    print(folder)
    count = 0 
    for file in os.listdir('test_directory/' + folder):
        f_name = folder + str(count) + '.png'
        print('file is ' + str(file))
        print('new file name is ' + str(f_name))
        os.rename('test_directory/'+str(folder)+'/' + file, 'test_directory/'+str(folder)+'/'+f_name)

        count += 1
#[os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]
