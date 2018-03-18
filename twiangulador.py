import tweepy
import argparse
from datetime import datetime
import os
import logging

from secrets1 import consumer_key, consumer_secret, access_token, access_token_secret

__version__ = '0.1'

def main(): 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    myUsername = twitter_api.me().screen_name
    print("[-] hi %s!" % myUsername)
    logger.warning("[-] hi %s!" % myUsername)
    followers1 = []
    n = 0
    print("[+] retreiving " + args.user1 + "\'s followers")
    for page in tweepy.Cursor(twitter_api.followers_ids, screen_name=args.user1).pages():
        followers1.extend(page)
        if n==1:            print("-- %s has +5k followers. retreiving them in pages.." % args.user1)
        if n>0:             print("   [+] page " + str(n))
        if len(page)==5000: n += 1
            
    print(">> " + args.user1 + ": " + str(len(followers1)) + " followers")
    logger.warning(">> " + args.user1 + ": " + str(len(followers1)) + " followers")

    followers2 = []
    m = 0
    print("[+] retreiving " + args.user2 + "\'s followers")
    for page in tweepy.Cursor(twitter_api.followers_ids, screen_name=args.user2).pages():
        followers2.extend(page)
        if m==1:            print("-- %s has +5k followers. retreiving them in pages.." % args.user2)
        if m>0:             print("   [+] page " + str(m))
        if len(page)==5000: m += 1

    print(">> " + args.user2 + ": " + str(len(followers2)) + " followers")
    logger.warning(">> " + args.user2 + ": " + str(len(followers2)) + " followers")

    followers3 = []
    o = 0
    print("[+] retreiving " + args.user3 + "\'s followers")
    for page in tweepy.Cursor(twitter_api.followers_ids, screen_name=args.user3).pages():
        followers3.extend(page)
        if o==1:            print("-- %s has +5k followers. retreiving them in pages.." % args.user3)
        if o>0:             print("   [+] page " + str(o))
        if len(page)==5000: o += 1

    print(">> " + args.user3 + ": " + str(len(followers3)) + " followers")
    logger.warning(">> " + args.user3 + ": " + str(len(followers3)) + " followers")

    print("common followers:")
    common = 0
    for i in followers1:
        for j in followers2:
            if i==j:
                for k in followers3:
                    if j==k:
                        print(twitter_api.get_user(id=i).screen_name)
                        logger.warning(twitter_api.get_user(id=i).screen_name)
                        common += 1
    print("total: " + str(common) + " common followers")
    logger.warning("total: " + str(common) + " common followers")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=
        ">>\"dadme 3 puntos de apoyo y encontraré a cualquiera\" - herramienta para twitter, versión %s by @jartigag" % __version__,
        usage='%(prog)s <user1> <user2> <user3>')
    parser.add_argument('user1', help='target1 user')
    parser.add_argument('user2', help='target2 user')
    parser.add_argument('user3', help='target3 user')

    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.WARNING) #TODO: INFO level?
    #TODO: if file_dir doesn't exist
    file_dir = os.path.join(os.path.expanduser("~"), ".config/twiangulador")
    logFile = logging.FileHandler(os.path.join(file_dir, datetime.now().strftime('%y%m%d-%H:%M') + " - " + args.user1 + "-" + args.user2 + "-" + args.user3 + ".log"))
    logger.addHandler(logFile)

    try:
        main()
    except tweepy.error.TweepError as e:
        print("[\033[91m!\033[0m] twitter error: %s" % e)
    except Exception as e:
        print("[\033[91m!\033[0m] error: %s" % e)