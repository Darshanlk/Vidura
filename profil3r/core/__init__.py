from profil3r.modules.email import email
import json

class Core(object):

    from ._menu import menu
    from ._permutations import get_permutations
    from ._results import print_results
    from ._run import run
    from ._report import generate_report, generate_json_report, generate_HTML_report, generate_csv_report
    from ._modules import modules_update, get_report_modules
    from ._logo import print_logo
    from ._argparse import parse_arguments
    
    from .services._social import facebook, twitter, instagram, tiktok, pinterest, linktree, myspace, flickr
    # from .services._forum import zeroxzerozerosec, jeuxvideo, hackernews, crackedto, lesswrong
    # from .services._programming import github, pastebin, replit
    # from .services._tchat import skype
    # from .services._music import soundcloud, spotify, smule
    # from .services._entertainment import dailymotion, vimeo
    # from .services._email import email
    # # from .services._porn import pornhub, redtube, xvideos
    # from .services._money import buymeacoffee, patreon
    # from .services._hosting import aboutme
    # from .services._domain import domain

    def __init__(self, config_path):
        self.version = "1.3.11"

        with open(config_path, 'r') as f:
            self.CONFIG = json.load(f)

        self.separators = []
        self.result = {}
        self.permutations_list = []
        self.modules = {
         
            "facebook":          {"method" : self.facebook},
          
            "instagram":         {"method" : self.instagram},
          
        }