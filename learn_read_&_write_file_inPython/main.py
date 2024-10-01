# open()
# 'x' = create file
# f = open('examp4.txt', 'x')
f = None
try:
    f= open('examp4.txt', 'x')
except Exception as e:
    print(e)
finally:
    if f:
        f.close()

# 'w' = write data file
# 'a' = append data file
# try:
#     with open('examp4.txt', 'w') as f:
#         f.write('Welcome to every one !\n')
#         f.close()
# except Exception as e:
#     print(e)

try:
    with open('examp4.txt', 'a') as f:
        f.write('Welcome to every one !\n')
        f.close()
except Exception as e:
    print(e)

# 'r' = read file
try:
    with open('examp4.txt', 'r') as f:
        content = f.read()
        print(content)
except Exception as e:
    print(e)

try:
    with open('examp4.txt', 'r') as f:
        list_content = f.readlines()
        i = 1
        for content in list_content:
            print(str(i) + ' : ' + content)
            i+=1
except Exception as e:
    print(e) 

# FIX CODE :
# 'r' = read file and count lines
# try:
#     with open('examp4.txt', 'r', encoding='utf-8') as f:
#         list_content = f.readlines()  # Read all lines into a list
#         i = 1
#         for content in list_content:
#             print(f"{i} : {content.strip()}")  # Print the line number and content, strip to remove extra newline
#             i += 1
# except Exception as e:
#     print(e)
