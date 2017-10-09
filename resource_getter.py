MIME_types = {'ico': 'image/x-icon', 'css': 'text/css', 'html': 'text/html', 'txt': 'text/plain',
              'js': 'text/javascript'}


def get_file_bytes(filename):
    try:
        filename = filename.replace("/", "workspace/")
        f = open(filename, 'rb')
        contents = f.read()
        return contents
    except Exception as e:
        print("resource_getter: "+str(e))
        raise


def get_format(file_path):
        array = file_path.split(".")
        format_name = array[len(array) - 1]
        if format_name in MIME_types:
            return MIME_types[format_name]
        else:
            raise Exception("Unknown format: "+file_path)
