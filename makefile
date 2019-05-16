run: scripts/face.mdl lex.py main.py matrix.py mdl.py display.py draw.py transform.py yacc.py
	python main.py scripts/face.mdl

test: scripts/test.mdl lex.py main.py matrix.py mdl.py display.py draw.py transform.py yacc.py
	python main.py scripts/test.mdl

good: scripts/art.mdl lex.py main.py matrix.py mdl.py display.py draw.py transform.py yacc.py
	python main.py scripts/art.mdl

oof: scripts/oof.mdl lex.py main.py matrix.py mdl.py display.py draw.py transform.py yacc.py
	python main.py scripts/oof.mdl

clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
