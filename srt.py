#birinchi belgini katta harfga ozgartiradi
txt = "salom, dunyoga hush kelibsan."
cap = txt.capitalize()
print(cap)


#satrni kichik harfga aylantiradi
txt = "Salom, DunYoga hush kelibsan!"
cas = txt.casefold()
print(cas)


#matnga px qoshish
txt = "banana"
cen = txt.center(6)
print(cen)

txt = "Muhammadsodiq "
cou = txt.count("Muhammadsodiq")
print(cou)

txt = "My name is "
enc = txt.encode()
print(enc)


txt = "salom dunyoga hush kelibsan,"
end =txt.endswith(",")
print(end)

txt = "s\ta\tl\to\tm"
exp = txt.expandtabs(2)
print(exp)

txt = "salom, dunyoga hush kelibsan."
fin = txt.find("dunyoga")
print(fin)

srt = "faqat {molish:.2f} dollar,uchun!"
form = (srt.format(molish=49))
print(form)

txt ="ofis 25"
isa = txt.isalnum()
print(isa)

txt = "companiyaX2"
isal = txt.isalpha()
print(isal)

txt = "aaaaaaaaaaaaaaaaaaaaaaaaa"
isac = txt.isascii()
print(isac)

txt = "54saa" #bu codim 3
isd = txt.isdecimal()
print(isd)

txt = "0123a5"
isdi = txt.isdigit()
print(isdi)

txt = "mana 4"
isid = txt.isidentifier()
print(isid)

txt = "salom Dunyo"
isl = txt.islower()
print(isl)

#matinda raqam qidirish 
txt = "123456 "
isn = txt.isnumeric()
print(isn)

txt = "salom! nima gap "
isp = txt.isprintable()
print(isp)


#ozgvaruvchinda bo'shliqni qidirish
txt = ""
iss = txt.isspace()
print(iss)


#matn bosh harf bilan boshlanganini tekshirish
txt = "Salom, Hush Kelibsiz Mani Dunyoyimga!"
ist = txt.istitle()
print(ist)


#matn xammasi bosh harf bn yozilganini tekshirish
txt = "NIMA SABAB"
isu = txt.isupper()
print(isu)


#matnga simvol qoshish
txt = ("Sariq", "Qora", "Oq")
joi = "#".join(txt)
print(joi)


#matn oraligini berish
txt = "banan"
x = txt.ljust(0)
print(x,"man yoqtirgan meva")


#textni xammasini kishik xarf qilish
txt = "Salom mani dostlarim"
low = txt.lower()
print(low)


#matnga matn qoshish
txt = "gilos"
x = txt.lstrip()
print("hamma mevalar ichida",x,"man uchun sevimlisi")


#harf almashtirish
txt = "Salom AAyubAxon!"
mytable = str.maketrans("A","d")
print(txt.translate(mytable))


#so'zga qoshtirnoq qoshish
txt = "Man kuni boyi banan yeyishim mumkin edi"
par = txt.partition("banan")
print(par)


#satrdagi sozni almashtirish
txt = "Menga banan yoqadi"
rep = txt.replace("banan","olma")
print(rep)

txt = "Mening uyim sizning uyingiz"
x = txt.rfind("uyingiz")
print(x)


#satr boshiga px qoshish
txt = "banan"
x = txt.rjust(1)
print(x, "mening sevimli mevam.")


txt = "Man kun, boyi banan  yeyishim mumkin edi banan sevimli mevam"
rpa = txt.rpartition("boyi")
print(rpa)


txt = "Olma banan qulupnay"
rsp = txt.rsplit(":")
print(rsp)


#Удалите все пробелы в конце строки
txt = "banan"
x = txt.rstrip()
print("hamma mevalar ichida",x,"man uchun sevimlisi")


txt = "salom o'rmon"
x = txt.split()
print(x)

txt = "raxmat musiqa uchun\nSalom o'rmon"
x = txt.splitlines()
print(x)