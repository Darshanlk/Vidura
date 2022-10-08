from profil3r.core.colors import Colors

def print_logo(self):
    print(Colors.OKGREEN + Colors.BOLD + '''

    ____________________Vidura OSINT_________________________
                                       
''' + Colors.ENDC)

    print("Vidura OSINT".format(version=self.version))
    # print("You can buy me a coffee at : https://www.buymeacoffee.com/givocefo\n" + Colors.ENDC)