txt = "salom, dunyoga hush kelibsan."
x = txt.capitalize()
print(x)

txt = "salom, dunyoga hush kelibsan!"
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(40)
print(x)

txt = "man olmani, sevaman mevalar ichidan eng sevgan mevam bu olma"
x = txt.count("olma")
print(x)

txt = "bu mani sti`lim"
x = txt.encode()
print(x)

txt = "salom dunyoga hush kelibsan."
x =txt.endswith(".")
print(x)

txt = "s\ta\tl\to\tm"
x = txt.expandtabs(2)
print(x)

txt = "salom, dunyoga hush kelibsan."
x = txt.find("dunyoga")
print(x)

txt = "faqat {narxi:.1f} dollar,uchun!"
x = (txt.format(narxi=49))
print(x)

txt ="ofis12"
x = txt.isalnum()
print(x)

txt = "companiyaM"
x = txt.isalpha()
print(x)

txt = "companiyam123"
x = txt.isascii()
print(x)

txt = "\u0033" #bu codim 3
x = txt.isdecimal()
print(x)

txt = "01234"
x = txt.isdigit()
print(x)

txt = "mana"
x = txt.isidentifier()
print(x)

txt = "salom dunyo"
x = txt.islower()
print(x)

txt = "123456"
x = txt.isnumeric()
print(x)

txt = "salom! nima gap #1?"
x = txt.isprintable()
print(x)

txt = "  "
x = txt.isspace()
print(x)

txt = "Salom, Hush Kelibsiz Mani Dunyoyimga!"
x = txt.istitle()
print(x)

txt = "NIMA SABAB"
x = txt.isupper()
print(x)

myTupple = ("Sariq", "Qora", "Oq")
x = "#".join(myTupple)
print(x)

txt = "banan"
x = txt.ljust(20)
print(x,"man yoqtirgan meva")

txt = "Salom mani dostlarim"
x = txt.lower()
print(x)

txt = "banan"
x = txt. lstrip()
print("hamma mevalar ichida",x,"man uchun sevimlisi")

txt = "Salom Ayubxon!"
mytable = str.maketrans("A","p")
print(txt.translate(mytable))

txt = "Man kuni boyi banan yeyishim mumkin edi"
x = txt.partition("banan")
print(x)

txt = "Menga banan yoqadi"
x = txt.replace("banan","olma")
print(x)

txt = "Mening uyim sizning uyingiz"
x = txt.rfind("uyim")
print(x)

txt = "banan"
x = txt.rjust(20)
print(x, "mening sevimli mevam.")

txt = "Man kun, boyi banan  yeyishim mumkin edi banan sevimli mevam"
x = txt.rpartition("banan")
print(x)

txt = "Olma banan qulupnay"
x = txt.rsplit(",")
print(x)

txt = "banan"
x = txt.rstrip()
print("hamma mevalar ichida",x,"man uchun sevimlisi")

txt = "salom o'rmon"
x = txt.split()
print(x)

txt = "raxmat musiqa uchun\nSalom o'rmon"
x = txt.splitlines()
print(x)

txt = "Salom hush kelibsan dunyoga"
x = txt.startswith("Salom")
print(x)

txt = "Salom Mani Ismim MUHAMMADSODIQ"
x = txt.swapcase()
print(x)

txt = "hush kelibsan dunyoga"
x = txt.title()
print(x)

#Almashtirish uchun kod kiriting 83 (S) bilan 80 (P):
mydict = {83:  80}

txt = "salom Salox!"

print(txt.translate(mydict))

txt = "Salom mani do'stlarim"
x = txt.upper()
print(x)

txt = "70"
x = txt.zfill(10)
print(x)





