
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

Miktex pgfsys
-------------

There is the same bug on windows in Mixtex 2.9 as well, open the file ``C:\Users\USER\AppData\Roaming\MiKTeX\2.9\tex\generic\pgf\systemlayer`` and make the same substitution::

    \def\pgfsys@svg@newline{\Hnewline} --> \def\pgfsys@svg@newline{{?nl}} 

http://sourceforge.net/p/miktex/bugs/2350/

Miktex "Illegal storage address"
--------------------------------

See http://sourceforge.net/p/miktex/bugs/2350/::

    tex4ht.c (2012-07-25-19:36 Windows MiKTeX)
    tex4ht mtest
      -i/tex4ht/ht-fonts/
      -cunihtf
      -ewin32/tex4ht.env
    (D:/MiKTeX2.9/tex4ht/base/win32/tex4ht.env)
    (D:/MiKTeX2.9/fonts/tfm/public/cm/cmr10.tfm)
    (D:/MiKTeX2.9/tex4ht/ht-fonts/alias/lm/lm-rep-cmrm/cmr.htf)
    Searching `lm-rep-cmrm.htf' for `cmr10.htf'
    (D:/MiKTeX2.9/tex4ht/ht-fonts/unicode/lm/lm-rep-cmrm.htf)
    --- error --- Illegal storage address

Now move (or copy) the file ..\MiKTeX2.9\tex4ht\ht-fonts\unicode\charset\unicode.4hf one folder up to ..\MiKTeX2.9\tex4ht\ht-fonts\unicode\unicode.4hf or one folder down to ..\MiKTeX2.9\tex4ht\ht-fonts\unicode\charset\uni\unicode.4hf

Miktex xtpipes problem
----------------------

In the file ``C:\Users\USER\AppData\Roaming\MiKTeX\2.9\tex4ht\base\win32``, in the block that reads::

    <ooxtpipes>
    .4oo move %%0.4oo %%0.tmp
    .4oo java -classpath c:/texlive/2010/texmf-dist/tex4ht/bin/tex4ht.jar xtpipes -i c:/texlive/2010/texmf-dist/tex4ht/xtpipes/ -o %%0.4oo %%0.tmp
    .4om move %%1.4om %%1.tmp
    .4om java -classpath c:/texlive/2010/texmf-dist/tex4ht/bin/tex4ht.jar xtpipes -i c:/texlive/2010/texmf-dist/tex4ht/xtpipes/ -o %%1.4om %%1.tmp
    </ooxtpipes>
    
Change the paths to the correct paths, mine looks something like this with Miktex::

    <ooxtpipes>
    .4oo move %%0.4oo %%0.tmp
    .4oo java -classpath C:/Users/ihb/AppData/Roaming/MiKTeX/2.9/tex4ht/bin/tex4ht.jar xtpipes -i C:/Users/ihb/AppData/Roaming/MiKTeX/2.9/tex4ht/xtpipes/ -o %%0.4oo %%0.tmp
    .4om move %%1.4om %%1.tmp
    .4om java -classpath C:/Users/ihb/AppData/Roaming/MiKTeX/2.9/tex4ht/bin/tex4ht.jar xtpipes -i C:/Users/ihb/AppData/Roaming/MiKTeX/2.9/tex4ht/xtpipes/ -o %%1.4om %%1.tmp
    </ooxtpipes>
