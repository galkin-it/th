import pandas as pd

def main():
    #fileName = input("Enter csv filename: ")
    fileName = "/Users/gas1lb/privat/gitlab/ukraine/tanja/homework/14005_EP2500A_Monat_02_18.csv"
    content = pd.read_csv(fileName, "rb")
    
    print(content)

if __name__ == "__main__":
    main()