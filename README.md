# lawyerank for taiwan lawyer test result	
given the fact that the ranking became more and more important nowadays for lawyers in taiwan, while official only annouce if one get credential 		
for lawyer but not ranking. If one wish to know the ranking, they will have to count the ranking manually, I hope to provide a convinient tool here to lookup ranking quickly.		
First you will have to decrypt the pdf file downloaded from official website.
qpdf is what I used:
```bash	
qpdf --password="" --decrypt input.pdf output.pdf
```    
To run this code, you will have to provide the test id(准考證號碼) as well:	
```bash
python pdftestrank.py --id=your id  --path= pdf path
```
