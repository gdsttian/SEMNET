import os

def XML_to_article_data(file_name):
    with open(file_name, 'r') as content_file:
        content = content_file.read()
        
    date_start=content.find('<dc:date>')+len('<dc:date>')
    date_end=content.find('</dc:date>')
    date=content[date_start:date_end]

    title_start=content.find('<dc:title>')+len('<dc:title>')
    title_end=content.find('</dc:title>')
    title=content[title_start:title_end]
        
    abstract_start=content.find('<dc:description>')+len('<dc:description>')
    abstract_end=content.find('</dc:description>')
    abstract=content[abstract_start:abstract_end]   
    
    return date, title, abstract
        

def create_full_data_arxiv():
    full_article_data_arxiv=[]
    for file in os.listdir("1aCreateFullArticleData\\arxivAbstractsXML"):
        if file.endswith(".xml"):
            new_file=os.path.join("1aCreateFullArticleData\\arxivAbstractsXML\\", file)
    
            date, title, abstract=XML_to_article_data(new_file)
            
            full_article_data_arxiv.append([date, title, abstract])
            
    return full_article_data_arxiv
