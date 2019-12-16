import webbrowser
lib = input("Search:")
url = "https://en.wikipedia.org/wiki/" +(str(lib))+ "_"
webbrowser.open_new(url)
