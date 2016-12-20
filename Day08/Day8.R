input <- as.matrix(read.table("Day8.txt",fill=TRUE))
grid <- matrix(rep(0,50*6),ncol=50)
for(i in 1:length(input[,1])){
  if(input[i,1]=="rect"){
    dimensions <- as.numeric(unlist(strsplit(input[i,2],"x")))
    grid[1:dimensions[2],1:dimensions[1]] <- 1
  } else if (input[i,2] == "row"){
    row <- as.numeric(unlist(strsplit(input[i,3],"y=")))[2]+1 
    shift <- as.numeric(input[i,5])
    newrow <- c(grid[row,((50-shift+1):50)],grid[row,(1:(50-shift))])
    grid[row,] <- newrow
  } else {
    col <- as.numeric(unlist(strsplit(input[i,3],"x=")))[2]+1
    shift <- as.numeric(input[i,5])
    newcol <- c(grid[(6-shift+1):6,col],grid[1:(6-shift),col])
    grid[,col] <- newcol
  }
}
image(grid)
sum(grid)
