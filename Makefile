.PHONY : all clean settings 
DATA=$(wildcard results/*.csv)
DATA_TXT=$(wildcard data/*.txt)
RESULTS=$(patsubst results/%.csv, results/%.png, $(DATA)) $(DATA_TXT)

COUNT=bin/plotcounts.py
RUN_COUNT = python $(COUNT)

#all : results/jane_eyre.png results/moby_dick.png
# this is target hence the need to update it, but how, of course by running
# recipe
all : $(RESULTS)


results/%.png : results/%.csv data/%.txt $(COUNT)
#	python $(COUNT) $< --outfile $@
	python $(COUNT) $(word 1,$^)  --outfile $@
	@bash bin/book_summary.sh $(word 2, $^) Author

all : 
	@for i in $(RESULTS) ; do bash bin/book_summary.sh $$i Author ; done

# results/moby_dick.png : results/moby_dick.csv $(COUNT)
# 	$(RUN_COUNT) $< --outfile $@ 


# results/jane_eyre.png : results/jane_eyre.csv $(COUNT)
# 	$(RUN_COUNT) \
		results/jane_eyre.csv --outfile results/jane_eyre.png

settings : 
	@echo RESULTS : $(RESULTS)
	@echo DATA : $(DATA)

help : 
	@grep '^##' ./Makefile

clean : 
	rm -f results/*.png
