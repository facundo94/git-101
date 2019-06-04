import yaml

def read_yaml(f):
    with open(f, 'r') as file:
        return yaml.safe_load(file.read())

CREDENTIALS = read_yaml('credentials.yaml')
print(CREDENTIALS)

SQLITE_DB = CREDENTIALS['sqlite']['db']
print(SQLITE_DB) 