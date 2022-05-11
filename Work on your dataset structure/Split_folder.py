import splitfolders
#### input dataset that want to split
input_folder = 'E:/data\\'
output_folder= 'E:/data\\'
splitfolders.ratio(input=input_folder, output= output_folder, seed=1337, ratio = (0.8, 0.1, 0.1))
"""در پوشه data اگر 3 پوشه با محتوی عکس های خودرو و اتوبوس و موتورسیکلت
داشته باشیم در E:/data سه پوشه train و test و valid ایجاد
خواهد شد که در هر کدام 3 کلاس گفته شده خودرو و اتوبوس و
موتور سیکلت خواهند بود """