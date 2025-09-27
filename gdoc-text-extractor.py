import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup


def download_public_google_doc(url):
    try:
        # Fetch the HTML content of the published document
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to access document. Status code: {response.status_code}")
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text content from the document
        # The main content is typically in elements with specific classes
        content_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
        
        # Extract text from each element
        text_content = []
        for element in content_elements:
            text = element.get_text().strip()
            if text:  # Only add non-empty text
                text_content.append(text)
        
        return '\n'.join(text_content)
    
    except Exception as e:
        raise Exception(f"Error processing document: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python import.py <Google_Doc_URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    try:
        content = download_public_google_doc(url)
    except Exception as e:
        print(f"Error: {e}")
    ContentList =[]
    ContentList = content.splitlines()
    # print(ContentList(5))
    Bigo =pd.DataFrame(columns=["X","char","Y"])

    for i in range(4,len(ContentList)-1,3):
        x=ContentList[i]
        char=ContentList[i+1]
        y=ContentList[i+2]
        Bigo
        Bigo.loc[(i-4)/3]=[x,char,y]
    Bigo = Bigo.astype({
    "X": "int64",
    "char": "string",
    "Y": "int64"
    })
    Bigo_sorted = Bigo.sort_values(by=["Y", "X"], ascending=[False, True ])
    Bigo_sorted = Bigo_sorted.reset_index(drop=True)

    max_Y = Bigo_sorted["Y"].max()
    Current_Y=max_Y
    Current_X=0
    line=""
    for i in range(0,len(Bigo_sorted),1):
        if Current_Y==Bigo_sorted.loc[i,"Y"]:               
            if Current_X == (Bigo_sorted.loc[i,"X"] ):
                Current_X+=1
                line+=Bigo_sorted.loc[i,"char"]

            else:
                X_Diff= Bigo_sorted.loc[i,"X"] - Current_X
                for i in range(0,X_Diff):
                    line+=" "
                    Current_X+=1
                line+=Bigo_sorted.loc[i,"char"]
                Current_X+=1
        else: 
            print(line)
            if Bigo_sorted.loc[i,"X"]== 0 :
                Current_X=1
                line=Bigo_sorted.loc[i,"char"]
            else:
                X_Diff= Bigo_sorted.loc[i,"X"] 
                line=""
                Current_X=0
                for i in range(0,X_Diff):
                    line+=" "
                    Current_X+=1
                line+=Bigo_sorted.loc[i,"char"]
                Current_X+=1
            Y_Diff= Bigo_sorted.loc[i,"Y"] - Current_Y
            Current_Y-=1
    print(line)
