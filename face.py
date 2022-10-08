from deepface import DeepFace
import cv2
import os
root_dir = "/home/darshan/Desktop/hackathon/Vidura/"
file_set = set()
img1=cv2.imread('image1.jpg')
print(img1.dtype)
img2=cv2.imread('elon.webp')
print(img2.dtype)

result = DeepFace.verify(img1,img2)
print("Is same face: ",result["verified"])



import instaloader
# # import recwd = os.getcwd()
# os.chdir(os.path.join(cwd, "images"))
# files = os.listdir()

# # ig = instaloader.Instaloader()
# # s = "https://www.instagram.com/thechiragsharmaa/"
# # # dp = input("Enter Insta username : ")
# # username=re.search(r'https://www.instagram.com/([^/?]+)', s).group(1)
# # print(username)
# # dp = username
# # ig.download_profile(dp , profile_pic_only=True)

# # #
# username = "thechiragsharmma"
# img2 = cv2.imread(f"../../{username}/")
# print(img2)
# # for dir_, _, files in os.walk(f"root_dir{username}"):
# #     for file_name in files:
# #         print(file_name)
# #         # rel_dir = os.path.relpath(dir_, root_dir)
# #         # rel_file = os.path.join(rel_dir, file_name)
# #         # file_set.add(rel_file)

