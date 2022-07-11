class extract:
    def fromCSV(self,file_path):
        import csv
        try:
            with open(file_path, encoding="utf-8") as file:
                final_data = [{k:v for k, v in row.items()}
                              for row in csv.DictReader(file, skipinitialspace=True)]
            return final_data
        except (FileNotFoundError, UnboundLocalError):
            print("Error! This file does not exist, please check the path or filename again.")
            return
            
        
    def fromJSON(self, file_path):
        import json
        try:
            final_data = []
            with open(file_path,"r") as file:
                for line in file:
                    final_data.append(json.loads(line))
            return final_data
        except (FileNotFoundError, UnboundLocalError):
            print("Error! This file does not exist, please check the path or filename again.")
            return