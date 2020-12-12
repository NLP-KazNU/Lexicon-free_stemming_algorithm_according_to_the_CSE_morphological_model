# Lexicon-free stemming algorithm according to the CSE (Complete Set of Endings) morphological model

Main concept of lexicon-free stemming on CSE-model of morphology is described below. In first to find an assumed ending of maximum length for the given word, which will be two symbols less than the length of the word. It is assumed that the stem cannot contain less than two symbols. The assumed ending of given word is searched in a list of endings. If the assumed ending not found in the list of endings, then one decreases the length of the assumed ending.  Accordingly, the assumed ending of the word is decreased by one symbol on the left side, and this symbol is added to the assumed stem of the word. The received ending is searched again in the list of endings. Above steps doing until the assumed ending will found in the list of endings or the length of the assumed ending will equal to zero.
In the following, e(w) is the ending of analyzed word w, st(w) is the stem of w, L(w) is the length of w, L[e(w)] is the calculated length of the ending.
The steps of the lexicon-free stemming algorithm are follows:
1. Calculation L(w).
2. Calculation the maximum length of an ending of the analyzed word: L[e(w)] = L(w) – 2, where 2 is the minimum length of the word stem.
3. Selection of the ending e(w) of the length L[e(w)] for analyzed word w.
4. Search e(w) on matching with an ending from the list of endings. If it matches, then the stem of the word is determined: st(w) = w – e(w). Go to step 7.
5. Otherwise, the calculated length of the ending of the analyzed word is decreased by one: L[e(w)] = L[e(w)] - 1.
6. If L[e(w)] < 1, then word w is without the ending. Go to step 7. Otherwise, go to step 3.
7. End.
In the beginning of the algorithm, a given word is checked in a list of language’s stop-words. If given word matches in the list of stop-words, then process for current word go to the end of algorithm.
To ensure a higher quality of stemming algorithm, a version of the stemming algorithm has been developed using a list of language's stems (stems-lexicon).


Instructions for use

To run a python file (file with the .py extension) you need:
1) open command prompt (CMD)
2) enter the following command (path to the folder where the python file is located):
cd C: \ Users \ ASER \ Desktop \ myprogs \ stemming \ github
3) run the python file specifying the file name:
stemming-for-Turkic-languages.py
4) then enter the name of the files that are requested to run the program
4.1) the name of the excel (.xls) file where the affixes are saved
Name of the affix file: affixes.xls
4.2) the name of the text (.txt) file where the source text is saved
Name of the text file: text.txt
4.3) the name of the text (.txt) file where you will write the result (text after the stemming process)
Name of the output file (result): output_results.txt

After executing these commands, an inscription is displayed on the screen where it says that the process was successfully completed and the results were saved
'The results of the stemming process are written to a file output_results.txt and saved in the folder where this python file is located'
