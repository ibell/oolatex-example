
Configuration
=============

* Ubuntu running in VirtualBox image, running from a shared folder on the windows host
* Texlive installed from TUG (NOT the ``apt-get`` one)
* See the caveats section below
* ImageMagick is needed for the PDF->PNG conversion
* ALL(!) images are exported at 300 dpi, in this way we can uniformly reduce them to 96 dpi and return to the original dimensions.  All images coming from matplotlib should be explicitly dimensioned!

To execute
==========

* If desired, run the ``make_fig.py`` script to generate the figures again
* At the command prompt on the ubuntu guest, do::

```
xelatex -shell-escape test.tex
xelatex -shell-escape test.tex
mk4ht oolatex test.tex
```
    
* Run the python script ``image_resizer.py`` which will resize the images in the ODT document (paths are hard coded for now) from 300 DPI to 96 dpi.
* Open the ``test_smaller.odt`` file in LibreOffice and save as Microsoft Word format
* See also: http://ask.libreoffice.org/en/question/2641/convert-to-command-line-parameter/
    
Caveats
=======

TexLive pgfsys
--------------

There is a bug in the TexLive 2014 installation on ubuntu, see this thread: http://tex.stackexchange.com/questions/185349/error-using-pgfsysdriver-with-tex4ht-only-shows-up-with-texlive-2014-ok-with-t

Basically, do the substitution::

    \def\pgfsys@svg@newline{\Hnewline} --> \def\pgfsys@svg@newline{{?nl}} 

in the file ``/usr/local/texlive/2014/texmf-dist/tex/generic/pgf/systemlayer``
