def copy_image_file(image_file):
    with open(image_file,'rb') as f_read:
        data = f_read.read()
        name_list = image_file.split('.')
    with open(f'{name_list[0]}_copy.{name_list[1]}','wb') as f_write:
        f_write.write(data)

image_file = 'Python26/Lenna.png'

copy_image_file(image_file)