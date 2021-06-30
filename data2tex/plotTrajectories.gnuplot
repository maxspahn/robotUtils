set term postscript eps color size 7,5 fontfile 'sfss1200.pfa'
inFile="trajectories_20210510.csv"
outFile="output.eps"
set output outFile
nc = "`head -1 trajectories_20210510.csv | sed 's/[^;]//g' | wc -c`" - 1
print nc
nd = 6
nt = nc/nd
set yrange [-2.5:4.0]
set xrange [-3: 4]
set size ratio -1
set datafile separator ';'
set multiplot layout 2,3 \
              margins 0.1,0.98,0.1,0.88 \
              spacing 0.1,0.05

set title "Static fabric"
plot for [i=2:nt:2] inFile u i:i+1 with lines lw 2 notitle, \
"obst1.csv" w lines lc rgb "black" lw 10 notitle

set title "MPC"
plot for [i=2+4*nt:5*nt:2] inFile using i:i+1 with lines lw 2 notitle, \
"obst1.csv" w lines lc rgb "black" lw 10 notitle

set title "Dynamic fabric"
plot for [i=2+2*nt:3*nt:2] inFile using i:i+1 with lines lw 2 notitle, \
"obst1.csv" w lines lc rgb "black" lw 10 notitle

set title "Static fabric"
plot for [i=2+1*nt:2*nt:2] inFile using i:i+1 with lines lw 2 notitle, \
"obst1.csv" w lines lc rgb "black" lw 10 notitle , \
"obst2.csv" w lines lc rgb "black" lw 10 notitle

set title "MPC" tc "black"
plot for [i=2+5*nt:6*nt:2] inFile using i:i+1 with lines lw 2 notitle, \
"obst1.csv" w lines lc rgb "black" lw 10 notitle , \
"obst2.csv" w lines lc rgb "black" lw 10 notitle

set title "Dynamic fabric" tc "black"
plot for [i=2+3*nt:4*nt:2] inFile using i:i+1 with lines lw 2 notitle, \
"obst1.csv" w lines lc rgb "black" lw 10 notitle , \
"obst2.csv" w lines lc rgb "black" lw 10 notitle
