import json
import praw
import time
import pprint

# Variables used throughout the application
config = []
visited = []
signature = ''

r = None

# Loads the configuration values from the JSON file
def loadConfig():
    global config
    with open('config.json') as f:
        config = json.load(f)

    signature = """
    ^^Made ^^by ^^/u/orion_dave.
    ^^[[Github Source]](https://github.com/RSBDavid/OSRedditBot)
    """


# The main execution function for the app. Searches for reddit posts which meet the criteria
def run():
    # Authenticate with PRAW using the configuration values in our configuration file
    print('Authenticating with PRAW and reddit...')
    r = praw.Reddit(user_agent=config['general']['user_agent'])
    r.login(config['general']['username'], config['general']['password'])

    # Only continue with the loop if we are logged in
    if r.is_logged_in():
        print('Logged In Successfully!')
        print('Starting scan for posts....')

        while True:
            time.sleep(1800)

            try:
                subreddit = r.get_subreddit('2007scape')
                for submission in subreddit.get_new(limit=10):
                    op_text = submission.title
                    print(op_text)
            except Exception as e:
                print(e)

# The main method for the application. Calls the loading method and then a execution method
if __name__ == "__main__":
    loadConfig()
    run()
