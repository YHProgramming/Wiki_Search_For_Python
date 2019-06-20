import webbrowser
lib = raw_input("Search:")
url = "https://en.wikipedia.org/wiki/" +(str(lib))+ "_"
webbrowser.open_new(url)
