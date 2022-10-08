from profil3r.core.colors import Colors

def print_logo(self):
    print(Colors.OKGREEN + Colors.BOLD + '''

    
 \ \    / (_)   | |              
  \ \  / / _  __| |_   _ _ __    
   \ \/ / | |/ _` | | | | '__|  
    \  /  | | (_| | |_| | |      
     \/   |_|\__,_|\__,_|_|      
                           
                                       
''' + Colors.ENDC)

    print("Vidura OSINT".format(version=self.version))
    # print("You can buy me a coffee at : https://www.buymeacoffee.com/givocefo\n" + Colors.ENDC)