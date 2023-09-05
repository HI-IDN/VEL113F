# The LaTeX compiler
LATEX_COMPILER = xelatex
BIB_COMPILER = bibtex

# The directory to store auxiliary files
AUX_DIR = ./.aux_files

# The name of the main .tex file (without extension)
# Example: MAIN_FILE = ClassicalMethods/LinearOptimization

.PHONY: all clean

# Rule to build any .pdf from a corresponding .tex file
%.pdf: %.tex
	# Ensure the auxiliary directory exists
	mkdir -p $(AUX_DIR)

	# First pass of xelatex
	$(LATEX_COMPILER) -output-directory=$(AUX_DIR) $<

	# Move the PDF to the directory of the .tex file
	mv -f $(AUX_DIR)/$(notdir $@) $@

clean:
	rm -rf $(AUX_DIR)
