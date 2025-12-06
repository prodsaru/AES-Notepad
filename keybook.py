class keybook:
    def __init__(self, file):
        self.file = file

    dict = {}
    def dict_read():
        with open(self.file) as f:
            for line in f:
                key, value = line.strip().split(':', 1)
                dict[key.strip()] = value.strip()
        

    def dict_write():
        new_passwords = ''
        lines = self.file.readlines()
        for key, value in dict:
            new_passwords += key + ": " + value + "\n"
        with open(self.file, 'w') as f:
            f.write(new_passwords)

    def access_key(n):
        return dict[n]