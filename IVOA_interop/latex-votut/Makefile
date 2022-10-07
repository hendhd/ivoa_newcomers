PDFLATEX = pdflatex
export TEXINPUTS=.:../res:../latex-votut:

.PHONY: twoup

%.twoup.pdf: %.pdf
	pdf2ps $< $*.ps
	pstops -pa4 "2:0R@0.9(-20mm,310mm)+1R@0.9(-20mm,180mm)" $*.ps $*.twoup.ps
	ps2pdf -sPAPERSIZE=a4 -dAutoRotatePages=3 $*.twoup.ps
	rm $*.twoup.ps

%.pdf: %.ps
	ps2pdf $<

$(DOCNAME).pdf: $(SOURCES) $(FIGURES)
	$(PDFLATEX) $(DOCNAME)

twoup: $(DOCNAME).twoup.pdf

forcetex:
	$(PDFLATEX) $(DOCNAME)

biblio:
	$(PDFLATEX) $(DOCNAME)
	bibtex $(DOCNAME)
	$(PDFLATEX) $(DOCNAME)

clean:
	rm -f $(DOCNAME).pdf $(DOCNAME).twoup.pdf  $(DOCNAME).twoup.ps  $(DOCNAME).aux $(DOCNAME).log $(DOCNAME).toc texput.log
	rm -f *.bbl *.blg *.out
