class Keybook:
    def __init__(self,file):
        self.file = file
        self.dict = {}
        self.keybook = "Keybook.txt"

    def read(self):
        with open(self.keybook) as f:
            for line in f:
                key, value = line.strip().split(':', 1)
                dict[key.strip()] = value.strip()

    def add(self, newFile, key, iv):
        self.dict[newFile] = [key , iv]
        for key, value in self.dict:
            new_passwords += key + ": " + value + "\n"
        with open(self.file, 'w') as f:
            f.write(new_passwords)

    def get(self, fileName):
        return self.dict[fileName]