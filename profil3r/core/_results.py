from distutils.log import error
import glob
from profil3r.core.colors import Colors
import instaloader
from deepface import DeepFace
import re
import cv2
import numpy as np

def print_results(self, element):
    ig = instaloader.Instaloader()
    username=''
    dp=''
    #static images
    # img1='../../thechiragsharmaa/2022-07-10_18-52-11_UTC_profile_pic.jpg'
    img1=cv2.imread('/home/darshan/Desktop/hackathon/Vidura/profil3r/core/chirag.jpg')
    print(img1,"imgggggggggggggggg111")
    img2=''
    result=''
    if element in self.result:
        element_results = self.result[element]

        # Section title

        # No results
        if not element_results["accounts"]:
            print("\n" + Colors.BOLD + "└──" + Colors.ENDC + Colors.OKGREEN + " {} ❌".format(
                element.upper()) + Colors.ENDC + Colors.FAIL + " (No results)" + Colors.ENDC)
            return
        # Results
        else:
            print("\n" + Colors.BOLD + "└──" + Colors.ENDC +
                  Colors.OKGREEN + " {} ✔️".format(element.upper()) + Colors.ENDC)
        accList = []
        # General case
        if element != "email":
        
            # Data scraped on the websites
            for account in element_results["accounts"]:

                print(Colors.BOLD + "   └── " + Colors.ENDC +
                      Colors.OKCYAN + account["value"] + Colors.ENDC)
                accList.append(account["value"])

                # print scraped element(s) (except value that was already printed)
                for index, element in list(account.items())[1:]:


                    if element["value"] is not None:

                        if not isinstance(element["value"], list):
                            print(Colors.BOLD + "   |   ├── " + Colors.ENDC + Colors.HEADER +
                                  element["name"] + " : " + element["value"] + Colors.ENDC)                    
                                  
                        else:
                            print(Colors.BOLD + "   |   ├── " + Colors.ENDC + Colors.HEADER +
                                  element["name"] + " : " + str(len(element["value"])) + " results" + Colors.ENDC)

            print(accList) 
        
            for acc in accList:
        
                try:
                    print("_________________in_________________")
                    username=re.search(r'https://instagram.com/([^/?]+)', acc+'/').group(1)
                    print(username)
                    dp = username
                    ig.download_profile(dp , profile_pic_only=True)

                    images = [cv2.imread(file) for file in glob.glob(f'{username}/*.jpg')]
                    
                    # print(images)
                    
                    result = DeepFace.verify(img1,images[0],enforce_detection=False)
                    print("Is same face: ",result["verified"])
                    

                except(e):
                    # print("fblink")
                    print(e)
        

            

        # Emails case
        else:
            possible_emails_list = [account["value"]
                                    for account in element_results["accounts"]]

            for account in element_results["accounts"]:
                # We pad the emails with spaces for better visibility
                longest_email_length = len(max(possible_emails_list))
                email = account["value"].ljust(longest_email_length + 5)

                # Breached account
                if account["breached"]:
                    print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.OKCYAN +
                          email + Colors.FAIL + "[BREACHED]" + Colors.ENDC)
                # Safe account
                else:
                    print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.OKCYAN +
                          email + Colors.OKGREEN + "[SAFE]" + Colors.ENDC)

         