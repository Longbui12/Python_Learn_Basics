# ///////////////////////////////////////////
# CODE : lấy tất cả ảnh từ file gốc rồi copy sang file khác 
# import os
# import shutil

# # Đường dẫn tới thư mục chứa các ảnh cần sao chép
# source_dir = 'D:\Image 1'  # Thay thế bằng đường dẫn thực tế
# destination_dir = 'D:\Image 2'  # Thay thế bằng đường dẫn thực tế

# try:
#     # Kiểm tra xem thư mục đích có tồn tại hay không, nếu không thì tạo mới
#     if not os.path.exists(destination_dir):
#         os.makedirs(destination_dir)
    
#     # Lặp qua tất cả các tập tin trong thư mục nguồn
#     for filename in os.listdir(source_dir):
#         # Kiểm tra xem tập tin có phải là ảnh hay không (ví dụ như .jpg, .png, .jpeg, .svg, .webp, .JPG)
#         # Ta có thể bổ sung thêm ảnh có đuôi file là gì ở file bên dưới để function có thể thực hiện .
#         if filename.endswith(('.jpg', '.png', '.jpeg', '.svg', '.webp', '.JPG')):
#             # Tạo đường dẫn đầy đủ tới tập tin nguồn và tập tin đích
#             source_path = os.path.join(source_dir, filename)
#             destination_path = os.path.join(destination_dir, filename)
            
#             # Sao chép tập tin từ thư mục nguồn sang thư mục đích
#             shutil.copy(source_path, destination_path)
#             print(f"Sao chép {filename} tới {destination_dir}")

#     print("Đã sao chép tất cả các ảnh từ thư mục nguồn tới thư mục đích.")

# except Exception as e:
#     print(f"Đã xảy ra lỗi: {e}")

# ==================================================================
# Code : lọc ra các ảnh giống nhau và đưa qua file mới  
# import os
# import shutil
# import hashlib

# def hash_file(file_path):
#     """Tính toán hàm băm của một tệp."""
#     hasher = hashlib.md5()
#     with open(file_path, 'rb') as f:
#         buf = f.read()
#         hasher.update(buf)
#     return hasher.hexdigest()

# # Đường dẫn tới thư mục chứa các ảnh cần sao chép
# source_dir = 'D:\Image 1'  # Thay thế bằng đường dẫn thực tế (đường dẫn file cần sao chép)
# destination_dir = 'D:\Image 2'  # Thay thế bằng đường dẫn thực tế (đường dẫn file được sao chép)

# try:
#     # Kiểm tra xem thư mục đích có tồn tại hay không, nếu không thì tạo mới
#     if not os.path.exists(destination_dir):
#         os.makedirs(destination_dir)

#     # Tạo một bộ để theo dõi các hàm băm của các tệp đã được sao chép
#     copied_hashes = set()

#     # Biến đếm số lượng ảnh đã sao chép
#     copied_count = 0

#     # Lặp qua tất cả các tập tin trong thư mục nguồn
#     for filename in os.listdir(source_dir):
#         # Kiểm tra xem tập tin có phải là ảnh hay không (ví dụ như .jpg, .png, .jpeg)
#         if filename.endswith(('.jpg', '.png', '.jpeg', '.svg', '.webp', '.JPG')):
#             # Tạo đường dẫn đầy đủ tới tập tin nguồn
#             source_path = os.path.join(source_dir, filename)

#             # Tính toán hàm băm của tập tin
#             file_hash = hash_file(source_path)

#             if file_hash not in copied_hashes:
#                 # Thêm hàm băm vào bộ
#                 copied_hashes.add(file_hash)
                
#                 # Tạo đường dẫn đầy đủ tới tập tin đích
#                 destination_path = os.path.join(destination_dir, filename)
                
#                 # Sao chép tập tin từ thư mục nguồn sang thư mục đích
#                 shutil.copy(source_path, destination_path)
#                 print(f"Sao chép ảnh từ file gốc : {filename} ==> Đi tới file mới ==> {destination_dir}")

#                  # Tăng biến đếm lên sau khi sao chép thành công
#                 copied_count += 1

#     print("Đã sao chép được {copied_count} tất cả các ảnh từ thư mục nguồn tới thư mục đích, không có tệp trùng lặp.")

# except Exception as e:
#     print(f"Đã xảy ra lỗi: {e}")

# ==================================================>>
# Code_Final : lọc ra các ảnh giống nhau và đưa qua file mới , đồng thời có đưa ra số lượng ảnh được lọc .
# import os
# import shutil
# import hashlib
# import time

# def hash_file(file_path):
#     """Tính toán hàm băm của một tệp."""
#     hasher = hashlib.md5()
#     with open(file_path, 'rb') as f:
#         buf = f.read()
#         hasher.update(buf)
#     return hasher.hexdigest()

# # Đường dẫn tới thư mục chứa các ảnh cần sao chép : (đường dẫn sẽ dùng dấu / or \\ )
# source_dir = '....'  # Thay thế bằng đường dẫn thực tế (đường dẫn file cần sao chép)
# destination_dir = '....'  # Thay thế bằng đường dẫn thực tế (đường dẫn file được sao chép)

# try:
#     # Kiểm tra xem thư mục đích có tồn tại hay không, nếu không thì tạo mới :
#     if not os.path.exists(destination_dir):
#         os.makedirs(destination_dir)

#     # Tạo một bộ để theo dõi các hàm băm của các tệp đã được sao chép :
#     copied_hashes = set()

#     # Biến đếm số lượng ảnh đã sao chép :                         
#     copied_count = 0

#     # Bắt đầu đếm thời gian :
#     start_time = time.time()

   
#     # Lặp qua tất cả các tập tin trong thư mục nguồn :
#     for filename in os.listdir(source_dir):
#         # Kiểm tra xem tập tin có phải là ảnh hay không (ví dụ như .jpg, .png, .jpeg) :
#         # Có thể thêm các định dạng ảnh khác vào hàm ở đưới đây :
#         if filename.endswith(('.jpg', '.png', '.jpeg', '.svg', '.webp', '.JPG')):
#             # Tạo đường dẫn đầy đủ tới tập tin nguồn
#             source_path = os.path.join(source_dir, filename)

#             # Tính toán hàm băm của tập tin :
#             file_hash = hash_file(source_path)

#             if file_hash not in copied_hashes:
#                 # Thêm hàm băm vào bộ :
#                 copied_hashes.add(file_hash)
                
#                 # Tạo đường dẫn đầy đủ tới tập tin đích :
#                 destination_path = os.path.join(destination_dir, filename)
                
#                 # Sao chép tập tin từ thư mục nguồn sang thư mục đích :
#                 shutil.copy(source_path, destination_path)
#                 print(f"Sao chép từ file gốc : {filename} ==> Đi tới File ==> {destination_dir}")
                
#                 # Tăng biến đếm lên sau khi sao chép thành công :
#                 copied_count += 1

#                 # Kết thúc đếm thời gian
#                 end_time = time.time()
#                 elapsed_time = end_time - start_time
               
#     print(f"Đã sao chép được : {copied_count} ảnh từ thư mục gốc tới thư mục đích, không có tệp trùng lặp.")
#     print(f'Thời gian để sao chép các ảnh: {elapsed_time:.2f} giây')
    
# except Exception as e:
#     print(f"Đã xảy ra lỗi: {e}")
