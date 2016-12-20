input <- c("L2", "L3", "L3", "L4", "R1", "R2", "L3", "R3", "R3", "L1", "L3", "R2", "R3", "L3", "R4", "R3", "R3", "L1", "L4", "R4", "L2", "R5", "R1", "L5", "R1", "R3", "L5", "R2", "L2", "R2", "R1", "L1", "L3", "L3", "R4", "R5", "R4", "L1", "L189", "L2", "R2", "L5", "R5", "R45", "L3", "R4", "R77", "L1", "R1", "R194", "R2", "L5", "L3", "L2", "L1", "R5", "L3", "L3", "L5", "L5", "L5", "R2", "L1", "L2", "L3", "R2", "R5", "R4", "L2", "R3", "R5", "L2", "L2", "R3", "L3", "L2", "L1", "L3", "R5", "R4", "R3", "R2", "L1", "R2", "L5", "R4", "L5", "L4", "R4", "L2", "R5", "L3", "L2", "R4", "L1", "L2", "R2", "R3", "L2", "L5", "R1", "R1", "R3", "R4", "R1", "R2", "R4", "R5", "L3", "L5", "L3", "L3", "R5", "R4", "R1", "L3", "R1", "L3", "R3", "R3", "R3", "L1", "R3", "R4", "L5", "L3", "L1", "L5", "L4", "R4", "R1", "L4", "R3", "R3", "R5", "R4", "R3", "R3", "L1", "L2", "R1", "L4", "L4", "L3", "L4", "L3", "L5", "R2", "R4", "L2")
curDir <- "N"
start <- c(0,0)
part2 <-matrix(0, nrow=length(input),ncol=2)
for(i in 1:length(input)){
  instruct <- substr(input[i],0,1)
  length <- as.numeric(substr(input[i],2,50))
  if(curDir =="N"){
    if(instruct=="L"){
      start[1] <- start[1]-length
      curDir = "W"
    } else {
      start[1] <- start[1]+length
      curDir = "E"
    }
  } else if(curDir =="E"){
    if(instruct=="L"){
      start[2] <- start[2]+length
      curDir = "N"
    } else {
      start[2] <- start[2]-length
      curDir = "S"
    }
  } else if(curDir =="S"){
    if(instruct=="L"){
      start[1] <- start[1]+length
      curDir = "E"
    } else {
      start[1] <- start[1]-length
      curDir = "W"
    }
  } else if(curDir =="W"){
    if(instruct=="L"){
      start[2] <- start[2]-length
      curDir = "S"
    } else {
      start[2] <- start[2]+length
      curDir = "N"
    }
  }
  part2[i,] <- start
}
blocks <- sum(abs(start))
blocks

##PART 2
plot(part2[1:150,],type="l")
#visual solution, click on the interception point
point<-locator(n=1)
point
