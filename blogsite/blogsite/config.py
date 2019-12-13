"""Configuration Utils Module"""

def envvar_setup(settings_file, var_list):
    """Function used for setting up environment variables """
    var_list = []
    file = open(settings_file, 'r')
    for line in file:
        if line.split(':')[0] == 'BLOG_DEBUG':
            var_list.append(line.split(':')[1])
        if line.split(':')[0] == 'BLOG_SECRETKEY':
            var_list.append(line.split(':')[1])
    file.close()
    return var_list
