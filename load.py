    class load:
        def toCSV(self, file_path, dataset):
            import csv
            try:
                keys = dataset[0].keys()
                a_dict = open(file_path, "w", encoding="utf-8")
                dict_writer = csv.DictWriter(a_dict, keys)
                dict_writer.writeheader()
                dict_writer.writerows(dataset)
                a_dict.close()         
                return "Correctly converted."
            except FileNotFoundError:
                print("FileNotFoundError. Check that the input dataset exists.")
                return
            except NameError:
                print("NameError. Check if the input dataset is writen correctly.")
                return
            except IOError:
                print("I/O Error. This dataset does not exist.")
                return

        def toJSON(self, file_path, dataset):
            import json
            try:
                with open (file_path, "w") as final:
                    json.dump(dataset, final)
                return "Correctly converted."
            except FileNotFoundError:
                print("FileNotFoundError. Check that the input dataset exists.")
                return
            except NameError:
                print("NameError. Check if the input dataset is writen correctly.")
                return
            except IOError:
                print("I/O Error. This dataset does not exist.")
                return