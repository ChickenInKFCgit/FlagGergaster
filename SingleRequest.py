from playwright.sync_api import sync_playwright

def gethtml(websiteURL:str)->str:
    r = requests.get(websiteURL)
    f = open("res.html",mode="w+")

    texte = formater_html(str(r.text))

    f.write(texte)
    f.close()

def formater_html(texte:str, indentation_char="\t"):
    final = ""
    
    indentation_lvl = -1 #car le premier n'a pas besoin d'indentation
    indice = 0

    for char in texte:
        indice+=1

        match(char):
            case '<':
                final+="\n"
                if (texte[indice] == "/"): #si c'est "</"
                    final+=indentation_char*indentation_lvl
                    indentation_lvl-=1
                else:
                    indentation_lvl+=1
                    final+=indentation_char*indentation_lvl               
            case _:
                pass  
        final+=char
        
    return final

            
def plz(websiteURL:str):
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto(websiteUR)
            page.screenshot(path=f'example-{browser_type.name}.png')
            browser.close()
