import requests
from profil3r.colors import Colors
import time

class Twitter:

    def __init__(self, config, permutations_list):
        # 500 ms
        self.delay = 500 / 1000
        # https://twitter.com/{username}
        self.format = config['plateform']['twitter']['format']
        self.permutations_list = permutations_list

        # You can find more at https://github.com/zedeus/nitter/wiki/Instances
        self.nitter_URL = [
            "https://nitter.42l.fr/{}",
            "nitter.pussthecat.org/{}",
            "nitter.nixnet.services/{}",
            "nitter.tedomum.net/{}",
            "nitter.fdn.fr/{}",
            "nitter.kavin.rocks/{}",
            "tweet.lambda.dance/{}"
        ]

    # Generate all potential twitter usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    # Return a working nitter instance
    def get_nitter_instance(self):
        for nitter_instance in self.nitter_URL:
            # Test every nitter instance until we find a working one
            if requests.get(nitter_instance.format("pewdiepie")).status_code == 200:
                return nitter_instance

    def search(self):
        twitter_usernames = {
            "accounts" : []
        }

        nitter_URL = self.get_nitter_instance()

        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                nitter_formatted_URL = nitter_URL.format(username.replace("https://twitter.com/", ""))
                r = requests.get(nitter_formatted_URL)
            except requests.ConnectionError:
                print("failed to connect to twitter")
            
            # If the account exists
            if r.status_code == 200:
                twitter_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        print("\n" + Colors.BOLD + "└──" + Colors.ENDC + Colors.OKGREEN + " Twitter ✔️" + Colors.ENDC)

        for account in twitter_usernames["accounts"]:
            print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.HEADER + account["value"] + Colors.ENDC)

        return twitter_usernames