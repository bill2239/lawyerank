# -*- coding: utf-8 -*- 
import io
import argparse
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    #retstr = io.StringIO()
    retstr = io.BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text



#print convert_pdf_to_txt("./decrypted_testresult.pdf")
def id2dict(path):
    #result=convert_pdf_to_txt("./decrypted_testresult.pdf")
    result=convert_pdf_to_txt(path)
    arr=result.split("\n")
    string=u"律師"
    pagestring=u"頁數"
    #string=u"類科"
    #u = unicode(string, "utf-8")
    rankarr=[]
    i=0
    for s in arr:
        if s.strip("\n") == "":
            pass
            #arr.pop(i)
        elif string in s.decode('utf-8'):
            pass
            #arr.pop(i)
        elif pagestring in s.decode('utf-8'):
            #arr.pop(i)
            pass
        else:
            if len(s.lstrip(" ").split("  ")) >1:
                for substr in s.lstrip(" ").split("  "):
                    rankarr.append(substr.decode('utf-8'))
            else:
                rankarr.append(s.decode('utf-8'))
        i=i+1
           

    #print len(arr)
    print 
    i=1
    rankdir= {}
    for s in rankarr:

        rankdir[s.lstrip(" ")[:8]]=i
        i=i+1
    return rankdir,len(rankarr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    rankdir,total=id2dict("./decrypted_testresult.pdf")
    #print rankdir[u"30630280"]
    parser.add_argument('--id', type=int, help='test id')
    args = parser.parse_args()
    print "id: %d rank %d out of %d in this test" %(args.id,rankdir[unicode(args.id)],total)
