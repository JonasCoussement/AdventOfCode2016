input <- as.matrix(unlist(read.table("Day7.txt")))
valid <- rep(FALSE,length(input))
for(i in 1:length(input)){
  input.vector <- unlist(strsplit(input[i],""))
  input.vector.idopen <- which(input.vector=="[")
  input.vector.idclosed <- which(input.vector=="]")
  outside.startids <- c(1,input.vector.idclosed+1)
  outside.stopids <- c(input.vector.idopen-4,length(input.vector)-3)
  inside.startids <- input.vector.idopen+1
  inside.stopids <- input.vector.idclosed-4
  #check for pattern outside brackets
  for(j in 1:length(outside.startids)){ #for every sequence outside brackets
    for(k in outside.startids[j]:outside.stopids[j]){
      notequaltonext <- input.vector[k]!=input.vector[k+1]
      equaltofourth <- input.vector[k]==input.vector[k+3]
      secondandthird <- input.vector[k+1]==input.vector[k+2]
      if(sum(c(notequaltonext,equaltofourth,secondandthird))==3){
        valid[i] = TRUE
        #print(input[i])
        #print(input.vector[k:(k+3)])
      }
    }
  }
  if(valid[i]){
    #when all patterns outside brackets are checked, check inside and override false valids
    for(j in 1:length(inside.startids)){ #for every sequence outside brackets
      for(k in inside.startids[j]:inside.stopids[j]){
        notequaltonext <- input.vector[k]!=input.vector[k+1]
        equaltofourth <- input.vector[k]==input.vector[k+3]
        secondandthird <- input.vector[k+1]==input.vector[k+2]
        if(sum(c(notequaltonext,equaltofourth,secondandthird))==3){
          valid[i] = FALSE
          #print(input.vector[k:(k+3)])
        }
      }
    }
  } 
}
sum(valid)

#PART 2
valid <- rep(FALSE,length(input))
for(i in 1:length(input)){
  input.vector <- unlist(strsplit(input[i],""))
  input.vector.idopen <- which(input.vector=="[")
  input.vector.idclosed <- which(input.vector=="]")
  outside.startids <- c(1,input.vector.idclosed+1)
  outside.stopids <- c(input.vector.idopen-3,length(input.vector)-2)
  inside.startids <- input.vector.idopen+1
  inside.stopids <- input.vector.idclosed-3
  #check for pattern outside brackets
  for(j in 1:length(outside.startids)){ #for every sequence outside brackets
    for(k in outside.startids[j]:outside.stopids[j]){
      pattern <- input.vector[k]!=input.vector[k+1]&&input.vector[k]==input.vector[k+2]
      if(pattern){
        #check if we find corresponding pattern within brackets
        for(l in 1:length(inside.startids)){ #for every sequence outside brackets
          for(m in inside.startids[l]:inside.stopids[l]){
            pattern <- input.vector[k+1]==input.vector[m]&&input.vector[k]==input.vector[m+1]&&input.vector[k+1]==input.vector[m+2]
            if(pattern){
              valid[i] = TRUE
              #print(input[i])
              #print(input.vector[k:(k+2)])
              #print(input.vector[m:(m+2)])
            }
          }
        }
      }
    }
  }
}
sum(valid)
