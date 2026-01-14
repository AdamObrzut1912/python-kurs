def cleanText(text):
    text = text.replace("Javascript", "**********")
    text = text.replace("java", "****")
    text = text.replace("php", "***")
    text = text.replace("html", "****")
    text = text.replace("css", "***")
    print(text)

cleanText("Programowanie zaczłąłem od php, następnie poznałem html i css, ale obecnie skupiam się na Javascript")