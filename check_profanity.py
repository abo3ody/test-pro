import urllib

def read_text():
    quotes = open(r"C:\Users\nour kablo\Desktop\aslan photo\New Text Document (2).txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print (output)
    connection.close()
read_text()    
