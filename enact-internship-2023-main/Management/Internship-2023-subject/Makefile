SHELL   = /bin/bash

BASE	= main
SOURCES = $(wildcard *.tex)
BIBS	= $(wildcard *.bib)
FIGDIR 	= Figures
FIGURES	= $(wildcard $(FIGDIR)/*.fig)
AUTRESFIG = $(wildcard $(FIGDIR)/*.JPG) $(wildcard $(FIGDIR)/*.jpg) $(wildcard $(FIGDIR)/*.jpeg)
PS	= $(BASE:.tex=.ps)
PDF	= $(BASE:.tex=.pdf)

pdf:	$(SOURCES) $(BIBS) $(FIGURES:%.fig=%.pdf) $(AUTRESFIG:%.jpg=%.pdf) $(ECLIPSEFIG:%.gif=%.eps)
	pdflatex -output-format pdf ${BASE}
	- bibtex $(BASE)
	pdflatex -output-format pdf  ${BASE}
	pdflatex -output-format pdf  ${BASE}
	pdflatex -output-format pdf  ${BASE}


cleanall: clean
	rm -f *.ps *.pdf *.tgz

clean:
	rm -f *.log *.aux *.bbl *.blg *~ *.bak *.dvi *.out *.eps *.png \
	*.toc *.lof *.lot

gnuplot::
	gnuplot *.input

epsfig:	$(FIGURES:%.fig=%.eps)


pdf_sans:	$(SOURCES) $(BIBS) $(FIGURES:%.fig=%.pdf) $(AUTRESFIG) $(ECLIPSEFIG:%.gif=%.eps)
	pdflatex -output-format pdf ${BASE}-SANS-ANNEXES
	- bibtex $(BASE)-SANS-ANNEXES
	pdflatex -output-format pdf  ${BASE}-SANS-ANNEXES
	pdflatex -output-format pdf  ${BASE}-SANS-ANNEXES
	rm ${BASE}-SANS-ANNEXES.bbl
	pdflatex -output-format pdf  ${BASE}-SANS-ANNEXES

pdf_anx:	$(SOURCES) $(BIBS) $(FIGURES:%.fig=%.pdf) $(AUTRESFIG) $(ECLIPSEFIG:%.gif=%.eps)
	pdflatex -output-format pdf ${BASE}-ANNEXES
	- bibtex $(BASE)-ANNEXES
	pdflatex -output-format pdf  ${BASE}-ANNEXES
	pdflatex -output-format pdf  ${BASE}-ANNEXES
	pdflatex -output-format pdf  ${BASE}-ANNEXES


%.eps: %.fig
	fig2dev -L eps $< $@
%.pdf: %.gif
	convert $< $@
%.jpg: %.fig
	convert $< $@
%.pdf: %.jpg
	convert $< $@
%.pdf: %.jpeg
	convert $< $@
%.pdf: %.fig
	-fig2dev -L pdf $< $@
%.png: %.fig
	fig2dev -L png $< $@

tgz:	$(BASE:%.tex=%.tgz)

%.tgz : $(SOURCES) %.tex clean
	 tar zcvf $*.tgz * --exclude Inputs --exclude *.tgz
