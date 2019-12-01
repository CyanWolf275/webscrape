#After running the first file, please save the webpage to an html file.
#This program extracts all the question links from the html file and fetches question and answer from them.
#Then, it will output a csv file.

import codecs, re, requests
html_path = #html file of the extended peing page
f = codecs.open(html_path, "r", "utf-8")
txt = f.read()
filt = re.compile(r'\/ja\/q\/(.*?)\"')
q_pattern = re.compile(r'<title>(.*?)\|')
a_pattern = re.compile(r'<meta name=\"description\" content=\"(.*?)\">')

lst = set(filt.findall(txt))
f.close()
with open("url.txt", "w") as file:
    for i in lst:
        file.write(i + " ")
length = str(len(lst))
i = 1
with codecs.open("qa.csv", "w", "utf-8") as f2:
    for url in lst:
        try:
            html = requests.get("https://peing.net/ja/q/" + url).text
            q = q_pattern.findall(html)[0][:-1]
            a = a_pattern.findall(html)[0]
            f2.write(q + "," + a + "\n")
            print(str(i) + "/" + length + " " + str(i / int(length) * 100)[:5] + "%")
        except:
            print(str(i) + "/" + length + " omitted " + url)
        i += 1
