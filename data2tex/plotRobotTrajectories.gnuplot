set term postscript eps color size 8,5 fontfile 'sfss1200.pfa'
inFile="out_fks_20210512.csv"
outFile="output.eps"
set output outFile
nc = "`head -1 out_fks_20210512.csv | sed 's/[^;]//g' | wc -c`" - 1
dim = 5
nd = 8
nt = nc/nd
set yrange [-2.5:2.5]
set xrange [-1: 4]
set size ratio -1
set datafile separator ';'
set multiplot layout 2,4 \
              margins 0.1,0.98,0.1,0.88 \
              spacing 0.05,0.05

i = 0
lx = 1 + i*15+13
ly = lx+1
set title "Static fabric"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"selectedFk_start.csv" every ::i*dim::(i+1)*dim u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::i*dim::(i+1)*dim u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::i*dim::(i+1)*dim u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle

i = 6
lx = 1 + i*15+13
ly = lx+1
fkstart = 0+i*(dim+1)
fkend = fkstart + dim
set title "MPC (short)"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle, \
"selectedFk_start.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle

i = 4
lx = 1 + i*15+13
ly = lx+1
fkstart = 0+i*(dim+1)
fkend = fkstart + dim
set title "MPC (long)"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle, \
"selectedFk_start.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle

i = 2
lx = 1 + i*15+13
ly = lx+1
fkstart = 0+i*(dim+1)
fkend = fkstart + dim
set title "Dynamic fabric"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle, \
"selectedFk_start.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle

i = 1
lx = 1 + i*15+13
ly = lx+1
fkstart = 0+i*(dim+1)
fkend = fkstart + dim
set title "Static fabric"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"obst2.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle, \
"selectedFk_start.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle

i = 7
lx = 1 + i*15+13
ly = lx+1
fkstart = 0+i*(dim+1)
fkend = fkstart + dim
set title "MPC (short)"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"obst2.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle, \
"selectedFk_start.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle

i = 5
lx = 1 + i*15+13
ly = lx+1
fkstart = 0+i*(dim+1)
fkend = fkstart + dim
set title "MPC (long)"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"obst2.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle, \
"selectedFk_start.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle

i = 3
lx = 1 + i*15+13
ly = lx+1
fkstart = 0+i*(dim+1)
fkend = fkstart + dim
set title "Dynamic fabric"
plot "obst1.csv" w lines lc rgb "black" lw 10 notitle, \
"obst2.csv" w lines lc rgb "black" lw 10 notitle, \
"base.csv" w lines lc rgb "black" lw 5 notitle, \
"goal.csv" w lines lc rgb "green" lw 2 notitle, \
inFile u lx:ly with lines lw 2 lc rgb "red" notitle, \
"selectedFk_start.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "green" notitle, \
"selectedFk_140.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "gray" notitle, \
"selectedFk_end.csv" every ::fkstart::fkend u 1:2 w linespoints lt 1 pt 7 lc rgb "black" notitle

