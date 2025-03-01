import sys, re

a = sys.argv

f_s = open("train.tags.en-zh.en", errors='ignore')
f_t = open("train.tags.en-zh.zh", errors='ignore')
f_s_o = open("corpus.en", "w", encoding='utf-8')
f_t_o = open("corpus.zh", "w", encoding='utf-8')
f_doc = open("corpus.doc", "w", encoding='utf-8')
f_s_doc = open("corpus.doc.en", "w", encoding='utf-8')
f_t_doc = open("corpus.doc.zh", "w", encoding='utf-8')

count = 0
for ls, lt in zip(f_s, f_t):
    if ls.startswith("<title>"):
        if not lt.startswith("<title>"):
            print("error " + str(count))
            break
        ls = re.sub("(^\<title\>)(.*)(\</title\>)", "\g<2>", ls).strip()
        lt = re.sub("(^\<title\>)(.*)(\</title\>)", "\g<2>", lt).strip()

        f_doc.write(str(count) + "\n")
        f_s_doc.write(ls + "\n")
        f_t_doc.write(lt + "\n")



    elif ls.startswith("<description>"):
        if not lt.startswith("<description>"):
            print("error " + str(count))
            break
        ls = re.sub("(^\<description\>)(.*)(\</description\>)", "\g<2>", ls).strip()
        lt = re.sub("(^\<description\>)(.*)(\</description\>)", "\g<2>", lt).strip()
        f_s_doc.write(ls + "\n")
        f_t_doc.write(lt + "\n")

    elif not ls.startswith("<"):
        if ls.strip() != "" and lt.strip() != "":
            f_s_o.write(ls.strip() + "\n")
            f_t_o.write(lt.strip() + "\n")
            count += 1

f_s.close()
f_t.close()
f_s_o.close()
f_t_o.close()
f_doc.close()
f_s_doc.close()
f_t_doc.close()

for test in ["dev2010", "tst2010", "tst2011", "tst2012", "tst2013"]:
    f_s = open("IWSLT15.TED." + test + ".en-zh.en.xml", encoding='utf-8')
    f_t = open("IWSLT15.TED." + test + ".en-zh.zh.xml", encoding='utf-8')

    count = 0

    f_s_o = open("IWSLT15.TED." + test + ".en-zh.en", "w", encoding='utf-8')
    f_t_o = open("IWSLT15.TED." + test + ".en-zh.zh", "w", encoding='utf-8')
    f_doc = open("IWSLT15.TED." + test + ".en-zh.doc", "w", encoding='utf-8')
    f_s_doc = open("IWSLT15.TED." + test + ".en-zh.doc.en", "w", encoding='utf-8')
    f_t_doc = open("IWSLT15.TED." + test + ".en-zh.doc.zh", "w", encoding='utf-8')

    for ls, lt in zip(f_s, f_t):
        if ls.startswith("<talkid>"):
            if not lt.startswith("<talkid>"):
                print("error " + str(count))
                break
            s = re.sub("(^\<talkid\>)(.*)(\</talkid\>)", "\g<2>", ls).strip()
            t = re.sub("(^\<talkid\>)(.*)(\</talkid\>)", "\g<2>", lt).strip()

            if s != t:
                print("error " + str(count) + " " + test)
                break

            f_s_doc.write(ls.strip() + "\n")
            f_t_doc.write(lt.strip() + "\n")
            f_doc.write(str(count) + "\n")


        elif ls.startswith("<seg"):
            if not lt.startswith("<seg"):
                print("error " + str(count) + " " + test)
                break

            ls = re.sub("(^\<seg.*\>)(.*)(\</seg\>)", "\g<2>", ls).strip()
            lt = re.sub("(^\<seg.*\>)(.*)(\</seg\>)", "\g<2>", lt).strip()

            if ls.strip() != "" and lt.strip() != "":
                f_s_o.write(ls + "\n")
                f_t_o.write(lt + "\n")
                count += 1
        else:

            f_s_doc.write(ls.strip() + "\n")
            f_t_doc.write(lt.strip() + "\n")

    f_s.close()
    f_t.close()
    f_s_o.close()
    f_t_o.close()
    f_doc.close()
    f_s_doc.close()
    f_t_doc.close()
