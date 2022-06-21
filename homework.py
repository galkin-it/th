import pandas as pd

def main():
    #fileName = input("Enter csv filename: ")
    fileName = "CSV_File.csv"
    content = pd.read_csv(fileName, "rb")
    
    print(content)

if __name__ == "__main__":
    main()
