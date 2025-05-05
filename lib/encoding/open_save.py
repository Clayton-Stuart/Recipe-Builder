"""
&& - &
&lt; - <;
&gt; - >;
&quot; - "
&apos; - '
&brace; - {
&brack; - }
&n; - \n
&r; - \r
"""

from tkinter import filedialog
import tkinter.messagebox as tkm
from lib.constants import *

VERSION = open(os.path.join(".", "lib", "VERSION"), "r").read().strip()

def openRecipe(save_path: str, name: str, ingredients_text: str, titles: list, steps: list, css: str, img_b64: dict) -> tuple:
    file = filedialog.askopenfile(mode='r', defaultextension='.rgfs')
    if file is None:
        return  save_path, name, ingredients_text, titles, steps, css, img_b64
    
    save_path = file.name
    try: 
        lines = file.readlines()
    except:
        tkm.showerror(title="Error", message="Please select a valid file")
        return save_path, name, ingredients_text, titles, steps, css, img_b64
        

    if len(lines) != 2:
        tkm.showerror(title="Error", message="Please select a valid file")
        return save_path, name, ingredients_text, titles, steps, css, img_b64
    
    if len(lines[0].strip().split('.')) != 3:
        tkm.showerror(title="Error", message="Please select a valid file")
        return save_path, name, ingredients_text, titles, steps, css, img_b64

    try:
        map(int, lines[0].strip().split('.'))
    except:
        tkm.showerror(title="Error", message="Please select a valid file")
        return save_path, name, ingredients_text, titles, steps, css, img_b64
    
    if lines[0].strip() != VERSION:
        tkm.showwarning(title="Warning", message="This version of Recipe HTML Generator may not be compatible with this version of Recipe HTML Generator")
    
    del lines[0]
    lines = lines[0]
    name_raw = ""
    ingredients_raw = ""
    
    lines = lines.replace('<', '')
    lines = lines.split('>')

    if len(lines) < 5:
        tkm.showerror(title="Error", message="Please select a valid file 5")
        return save_path, name, ingredients_text, titles, steps, css, img_b64
    

    name_raw = lines[0].strip()
    ingredients_raw = lines[1].strip()
    titles_raw = lines[2].strip()
    steps_raw = lines[3].strip()
    css_raw = lines[4].strip()
    img_b64_raw = lines[5].strip()

    name = name_raw.replace('&&', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'").replace('&brace;', '{').replace('&brack;', '}').replace('&n;', '\n').replace('&r;', '\r')
    ingredients_text = ingredients_raw.replace('&&', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'").replace('&brace;', '{').replace('&brack;', '}').replace('&n;', '\n').replace('&r;', '\r')
    
    while len(titles) > 0:
        del titles[0]


    titles_raw = titles_raw.replace('{', '')
    if titles_raw != "None":
        titles_raw = titles_raw.split('}')
        for i in titles_raw:
            titles.append(i.replace('&&', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'").replace('&brace;', '{').replace('&brack;', '}').replace('&n;', '\n').replace('&r;', '\r'))
    

    while len(steps) > 0:
        del steps[0]

    steps_raw = steps_raw.replace('{', '')
    if steps_raw!= "None":
        steps_raw = steps_raw.split('}')
        for i in steps_raw:
            steps.append(i.replace('&&', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'").replace('&brace;', '{').replace('&brack;', '}').replace('&n;', '\n').replace('&r;', '\r'))

    if css_raw != "None":
        css[0] = css_raw.replace('&&', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'").replace('&brace;', '{').replace('&brack;', '}').replace('&n;', '\n').replace('&r;', '\r')

    img_b64 = dict()

    if img_b64_raw!= "None":
        img_b64_raw = img_b64_raw.strip().replace('{', '').split('}')
        del img_b64_raw[-1]
        for i in img_b64_raw:
            mid = i.split(':')
            img_b64[int(mid[0].strip())] = mid[1].strip().replace('&&', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quote;', '"').replace('&apos;', "'").replace('&brace;', '{').replace('&brack;', '}').replace('&n;', '\n').replace('&r;', '\r').split('.')


    if len(titles) > 0:
        del titles[-1]
    if len(steps) > 0:
        del steps[-1]

    return save_path, name, ingredients_text, titles, steps, css, img_b64
    
"""
&& - &
&lt; - <;
&gt; - >;
&quot; - "
&apos; - '
&brace; - {
&brack; - }
&n; - \n
&r; - \r
"""