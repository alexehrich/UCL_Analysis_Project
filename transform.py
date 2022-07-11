class transform:
    def head(self, dataset): #return the top N records from the dataset
        try:
            h = int(input("How many lines from the top of the dataset do you want to check? "))
            return dataset[:h]
        except (UnboundLocalError,ValueError, TypeError):
            print("Error. This number was not valid, check that the input number was in the length of the list and an int.")
            return dataset
    
    
    def tail(self, dataset): #return the last N records from the dataset
        try:
            t = int(input("How many lines from the bottom of the dataset do you want to check? "))
            return dataset[-t:]
        except (UnboundLocalError,ValueError, TypeError):
            print("Error. This number was not valid, check that the input number was in the length of the list and an int.")
            return
        
        
    def rename_attribute(self, dataset): #rename a column in the dataset
        try:
            remove = input("Which is the column name that you want to change? ")
            rename = input("How do you want to rename that column? ")
            for data in dataset:
                data[rename] = data[remove]
                del data[remove]
            return dataset
        except KeyError:
            print("KeyError. Check that the the name of the column to be renamed has been propperly input.")
            return
       
            
    def remove_attribute(self, dataset): #remove a column from the dataset
        try:
            remove = input("Which is the column name that you want to remove? ")
            for data in dataset:
                data.pop(remove)
            return dataset
        except KeyError:
            print("KeyError. Check that the the name of the column to be removed has been propperly input.")
            return


    def rename_attributes(self, dataset): #rename a list of columns in the dataset
        try:
            remove_lst = []
            rename_lst = []
            while True:
                remove = input("Which are the column names that you want to rename? (insert [stop] after adding all the columns)  ")
                if remove.lower() == "stop":
                    break
                else:
                    remove_lst.append(remove)
                    continue
            while True:
                rename = input("How do you want to rename those columns? (insert [stop] after adding all the columns)  ")
                if rename.lower() == "stop":
                    break
                else:
                    rename_lst.append(rename)
                    continue
            for data in dataset:
                for i,j in zip(rename_lst,remove_lst):
                    data[i] = data.pop(j)
            return dataset
        except KeyError:
            print("KeyError. Check that the the name of the column to be renamed has been propperly input.")
            return
        
        
    def remove_attributes(self, dataset): #remove a list of columns in the dataset
        try:
            remove_lst = []
            while True:
                remove = input("Which are the column names that you want to remove? (insert [stop] after adding all the columns) ")
                if remove.lower() == "stop":
                    break
                else:
                    remove_lst.append(remove)
                    continue
            for data in dataset:
                for i in remove_lst:
                    data.pop(i)
            return dataset
        except KeyError:
            print("KeyError. Check that the the name of the column to be removed has been propperly input.")
            return