from configparser import ConfigParser


def config(filename:str='config.ini', section:str='postgresql') -> dict:
    parser = ConfigParser()
    parser.read(filename)
    
    params = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            params[item[0]] = item[1]
    else:
        raise Exception(f'Section {section} is not found in the {filename}')
    return params


