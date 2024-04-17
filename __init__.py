import json

def save(Data: any, FileName: str):
    """
    Save data to a file.

    Data
        the data you want to put in the save file.
        can be any data type.

    FileName
        sets the name of the file you want to write to.
        this file can be a file not yet created.
        requires file extention.
    """

    if not FileName:
        print("\nError: no file set\n")
    else:
        try:
            Name, FileType = FileName.split(".")

            if FileType == "json":
                with open(FileName, "w") as SF:
                    json.dump(Data, SF)
            else:
                with open(FileName, "w") as SF:
                    SF.write(Data)

        except ValueError:
            raise NameError("\nmissing file extention\n")

def load(FileName: str):
    """
    Load the data from the save file.

    FileName
        sets the name of the file you want to read from.
        this file has to have already been created.
        requires file extention.
    """
    if not FileName:
        print("Error: no file set")
    else:
        try:
            Name, FileType = FileName.split(".")

            if FileType == "json":
                with open(FileName, "r") as SF:
                    return json.load(SF)
            else:
                with open(FileName, "r") as SF:
                    return SF.read()

        except ValueError:
            raise NameError("missing file extention")
        except FileNotFoundError:
            raise NameError("no file exists under that name")
