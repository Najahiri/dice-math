#!/bin/bash
echo "## Dice Math"

cd "Tex"

echo "### Pass 1"
pdflatex -interaction=nonstopmode "Dice-Math.tex" > ../Logs/en_run1.log
echo "### Pass 2"
pdflatex -interaction=nonstopmode "Dice-Math.tex" > ../Logs/en_run2.log
echo "### Pass 3"
pdflatex -interaction=nonstopmode "Dice-Math.tex" > ../Logs/en_run3.log

echo "### PDF written to Tex/Dice-Math.pdf"