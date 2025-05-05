class css:
    def __init__(self):
        self.css = {"*": ["margin: 0", "padding: 0", "border: 0", "font-size: 100%", "vertical_align: baseline", "background: transparent"]}

    def add_style_group(self, style: str):
        self.css[style] = []

    def remove_style_group(self, style: str):
        try:
            del self.css[style]
        except:
            pass


def build_html(name: str, ingredients_str: str, titles: list, steps: list, img_b64: dict, css: str = "") -> str:
    steps_copy = steps.copy()
    ingredients = []
    for ingredient in ingredients_str.split('\n'):
        ingredients.append(ingredient.strip())
    
    
    
    big_string = ""


    # head and metadata
    big_string += "<!DOCTYPE html>\n"
    big_string += "<html lang=\"en\">\n"
    big_string += "<head>\n"
    big_string += "\t<meta charset=\"UTF-8\">\n"
    big_string += "\t<title>" + name + "</title>\n"

    # styles
    big_string += "\t<style type=\"text/css\">\n"
    big_string += css
    big_string += "\t</style>\n"

    big_string += "</head>\n"

    # body
    big_string += "<body>\n"
    big_string += "\t<h1 class=title>" + name + "</h1>\n\n"

    # ingredients
    big_string += "\t<div class=\"ingredients\">\n"
    big_string += "\t\t<h2 class=\"section-title\">Ingredients</h2>\n"
    big_string += "\t\t<ul class=\"ingredients-list\">\n"
    for ingredient in ingredients:
        if ingredient[:3] == "<h>":
            big_string += "\t\t\t<li><h2>" + ingredient + "</h2></li>\n"
        elif ingredient[:3] == "<b>":
            big_string += "\t\t\t<li><b>" + ingredient + "</b></li>\n"
        elif ingredient[:3] == "<i>":
            big_string += "\t\t\t<li><i>" + ingredient + "</i></li>\n"
        elif ingredient[:3] == "<u>":
            big_string += "\t\t\t<li><u>" + ingredient + "</u></li>\n"
        else:
            big_string += "\t\t\t<li>" + ingredient + "</li>\n"
    big_string += "\t\t</ul>\n"
    big_string += "\t</div>\n\n"
    big_string += "\t<hr>\n\n"
    
    # add images to steps
    for i in range(len(steps_copy)):
        if steps_copy[i].count("<") > 0:
            for key in img_b64.keys():
                if not isinstance(img_b64[key][-1], str):
                    img_b64[key][-1] = str(img_b64[key][-1], 'utf-8')
                if not isinstance(img_b64[key][0], str):
                    img_b64[key][0] = str(img_b64[key][0], 'utf-8')
                
                steps_copy[i] = steps_copy[i].replace("<" + str(key) + ">", "<br><img src=\"data:image/" + img_b64[key][-1] + ";base64, " + img_b64[key][0] + "\"><br>")


    # instructions
    big_string += "\t<div class=\"instructions\">\n"
    big_string += "\t\t<h2 class=\"section-title\">Instructions</h2>\n"
    for title in range(len(titles)):
        big_string += "\t\t<h3 class='step-title'>" + titles[title] + "</h3>\n"
        big_string += "\t\t<p>" + steps_copy[title] + "</p>\n"
        big_string += "\t\t<br>\n"
    big_string += "\t</div>\n"
    
    # closing tags
    big_string += "</body>\n"
    big_string += "</html>"

    # return big_string.replace('’', '\'').replace('“', '"').replace('”', '"').replace('–', '-').replace('°', '&deg;').replace('—', '-')
    return big_string
    
def build_css(css: dict = {}, preset: int = 0, darkMode: bool = False) -> str:
    # returns a string that can be directly inputted into the css parameter of build_html()
    # the input should be a dictionary with the keys being the call such as .ingredients or #step-1
    # the values being a list of rules that should be added to the css file underneath the element call
    # example: css = {".ingredients": ["color: red", "border-style: solid"], ".instructions": ["color: blue"]}
    output = ""


    if preset == 1:
        if darkMode:
            css = {
                ".title":["font-size: 3em", 
                          "border-bottom-style: solid", 
                          "border-bottom-width: 2px", 
                          "border-color: white", 
                          "width: fit-content", 
                          "padding-right: 1em", 
                          "padding-left: 1rem"],

               "body": ["font:'Times New Roman' Times Serif",
                        "color:white", 
                        "background-color: #131313", 
                        "font-size: 1rem",
                        "padding-left: 1rem",
                        "width: 80%"],

                "img": ["width: 10rem"],
                        
                ".section-title": ["font-size: 2em",
                                   "text-decoration: underline", ],
                                   
                ".step-title": ["font-size: 1.5em",
                            "border-bottom-style: solid", 
                            "border-bottom-width: 2px", 
                            "border-color: white", 
                            "width: fit-content", 
                            "padding-right: 0.5em"]}
        else:
            css ={
                ".title":["font-size: 3em", 
                          "border-bottom-style: solid", 
                          "border-bottom-width: 2px", 
                          "border-color: black", 
                          "width: fit-content", 
                          "padding-right: 1em", 
                          "padding-left: 1rem"],

               "body": ["font:'Times New Roman' Times Serif",
                        "color:black", 
                        "background-color: #ffffff", 
                        "font-size: 1rem",
                        "padding-left: 1rem",
                        "width: 80%"],

                "img": ["width: 10rem"],
                        
                ".section-title": ["font-size: 2em",
                                   "text-decoration: underline", ],
                                   
                ".step-title": ["font-size: 1.5em",
                            "border-bottom-style: solid", 
                            "border-bottom-width: 2px", 
                            "border-color: black", 
                            "width: fit-content", 
                            "padding-right: 0.5em"]}


    for key in css.keys():
        output += key + " {"
        for rule in css[key]:
            output += rule + "; "
        output += "} "

    return output