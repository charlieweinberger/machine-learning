nPerfectCubes n = [ a*a*a | a <- [0..n] ]
pSum n = sum (nPerfectCubes n)

main = print (pSum 10) -- 3025