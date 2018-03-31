
LaTeX->XHTML with latexml

Container
---------
```
docker image build -t texml .
docker container run -it -v "$(pwd)":/oo texml bash
```

Build
-----
```
cd oo
latexml --dest test.xml test.tex
latexmlpost --dest=test.xhtml test.xml
```
