import praw
import tkinter.filedialog
import webbrowser

file_path = 'x'  #Declared in order to check (line 19) if a new value for file_path (optional argument) was given (line 7)

def get_posts(subreddit_name, number_of_posts, file_path='x'):
    '''(str, int, str) -> NoneType

        Creates an HTML document (with name = subreddit_name, in Python directory by default
        unless an existing filepath is specified in parameter file_path) containing a number
        (number_of_posts) of hot posts in a given subreddit (subreddit_name).
        Formatted with clickable links.
    '''
    
    ### Variable Initialization ###
    number = 1   #Accumulator (line 29)
    skeleton = "#{} | {} |</br> <a href=\"{}\">{}</a> </br></br>"   #Formatting structure for posts
    source = subreddit_name + '.html'
    if file_path != 'x':
        source = file_path
    file = open(source, 'w')   #Opening empty HTML document with writing privileges
    url = 'file://' + source
    r = praw.Reddit('Subreddit Post Scrapper in Python')    #Declaring user_agent, required by reddit bot guidelines
    posts = r.get_subreddit(subreddit_name).get_hot(limit=number_of_posts)    #Retrieving reddit content based on function parameters

    ### Populating HTML Document ###
    for item in posts:
        file.write(str(skeleton.format(number, item.ups, item.url, item.title)))
        number += 1
        
    ### Displaying HTML Document & Clearing Memory ###
    file.close()
    webbrowser.open(source,new=2)
