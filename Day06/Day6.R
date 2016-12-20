input <- as.matrix(read.table("Day6.txt",header=FALSE))
inputmatrix <- sapply(input,function(x) unlist(strsplit(x,"")))
columns <- apply(inputmatrix,1,table)
message <- sapply(1:length(columns[1,]), function(x) which(columns[,x]==max(columns[,x])))
message
message.new <- sapply(1:length(columns[1,]), function(x) which(columns[,x]==min(columns[,x])))
message.new