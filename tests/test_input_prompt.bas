10 REM Test INPUT prompt behavior
20 PRINT "Test 1: INPUT with no prompt (should show '?')"
30 PRINT "Type: test1"
40 INPUT A$
50 PRINT "Got: "; A$
60 PRINT
70 PRINT "Test 2: INPUT with prompt and comma (should show 'prompt?')"
80 PRINT "Type: test2"
90 INPUT "Enter value", B$
100 PRINT "Got: "; B$
110 PRINT
120 PRINT "Test 3: INPUT with prompt and semicolon (should show 'prompt' - no ?)"
130 PRINT "Type: test3"
140 INPUT "Enter value"; C$
150 PRINT "Got: "; C$
160 END
