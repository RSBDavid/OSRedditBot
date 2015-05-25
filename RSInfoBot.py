import json
import praw
import time
import pprint
import importlib
import CommentManager

# Variables used throughout the application
config = []
modules = []
visited = set()
postedOn = []
r = None

manager = CommentManager.CommentManager()

signature = """
%s

^^Made ^^by ^^/u/orion_dave.
^^[Github Source](https://github.com/RSBDavid/OSRedditBot)
"""

# Loads the configuration values from the JSON file
def loadConfig():
    global config
    with open('config.json') as f:
        config = json.load(f)


def loadModules():
    for e in config['modules']:
        name = e + "Module"
        mod = __import__(name)
        cls = getattr(mod, name)
        modules.append(cls())
        print("Loaded " + name)


def checkComments():
    for comment in manager.get():
        print(comment)


# The main execution function for the app. Searches for reddit posts which meet the criteria
def execute():
    # Authenticate with PRAW using the configuration values in our configuration file
    print('Authenticating with PRAW and reddit...')
    # r = praw.Reddit(user_agent=config['general']['user_agent'])
    r = praw.Reddit(user_agent='TestAgent/1.0')
    r.login(config['general']['username'], config['general']['password'])

    # Only continue with the loop if we are logged in
    if r.is_logged_in():
        print('Logged In Successfully!')
        print('Starting scan for posts....')

        while True:
            checkComments()

            time.sleep(3)

            try:
                comments = r.get_comments('osrs_development')
                for comment in comments:
                    if comment.id not in visited:
                        for m in modules:
                            if m.validate(r, comment):
                                print('handling comment')
                                if m.handle(r, comment):
                                    print("Replied to " + comment.id)
                                else:
                                    print("Failed to replied to " + comment.id)
                                visited.add(comment.id)
            except Exception as e:
                print(e.read())
                break

# The main method for the application. Calls the loading method and then a execution method
if __name__ == "__main__":
    loadConfig()
    loadModules()
    execute()
