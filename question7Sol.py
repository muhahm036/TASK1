class Charactercount:
    __ch=""
    def __init__(self):
        self.__ch=""

    def setString(self,value):
        status=True
        for x in value:
            if x >=  'a' and  x <= 'z' or x >=  'A' and  x <= 'Z':
                status=True
            else:
                status=False
                break

        if status==True:
            self.__ch=value
        else:
            print("invalid String")

    def getString(self):
         charCount=0
         for x in self.__ch:
             charCount=charCount+1

         return   charCount

obj=Charactercount()
ch=input("ENTER STRING:")
obj.setString(ch)
print("Count of Characters:",obj.getString())

