10 REM Test Ctrl+C during INPUT
20 PRINT "Press Ctrl+C at the INPUT prompt"
30 INPUT "Enter something"; A$
40 PRINT "You entered: "; A$
50 PRINT "This shouldn't print if you pressed Ctrl+C"
60 END
