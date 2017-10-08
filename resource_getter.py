def get_file(filename):
    try:
        filename = filename.replace("/", "")
        f = open(filename, 'r')
        contents = f.read()
        return contents
    except Exception as e:
        print("resource_getter: "+str(e))
        raise

