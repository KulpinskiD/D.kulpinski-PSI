class FileManager():
    dodaj=''
    text=''
    def update_file(self):

        if self.text=='':
            self.text=self.dodaj
        else:
            self.text=self.text+str(self.dodaj)
    def read_file(self):
        print("text= "+str(self.text))
