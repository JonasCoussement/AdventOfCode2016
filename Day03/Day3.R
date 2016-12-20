input <-read.csv("Day3.csv",header=FALSE)
sorted <- apply(input, 1, sort)
check <- apply(sorted,2,function(x) sum(x[1:2])>x[3])
solution <- sum(check)
solution

#part 2
vectorinput <- as.vector(unlist(input))
grouped <- t(sapply(seq(1,length(vectorinput),by=3), function(x) vectorinput[x:(x+2)]))
sorted <- apply(grouped, 1, sort)
check <- apply(sorted,2,function(x) sum(x[1:2])>x[3])
solution <- sum(check)
solution
