input <- unlist(read.csv("Day4.txt",header=FALSE))
cumroomcode <- 0
for(i in 1:length(input)){
  current <- as.character(input[i])
  #wirte current string as vector of chars
  vectorinput <- unlist(strsplit(current,""))
  #try to convert each char to numeric
  numeric <- suppressWarnings(as.numeric(vectorinput))
  #find index of numbers
  numberindex <- which(sapply(numeric,is.na)==FALSE)
  #final code is a fixed width and fixed distance away from numbers
  roomcodeindex <- max(numberindex)+2:6
  #vector of the encryption characters
  encryptname <- vectorinput[1:(min(numberindex)-2)]
  #sort vector alphabetically and remove "-"
  encrypt.sort <- sort(encryptname)[-which(sort(encryptname)=="-")]
  #count the occurence of each char
  occurence <- sapply(unique(encrypt.sort),function(x) sum(encrypt.sort == x))
  #sort by occurence
  occurence.sort <- sort(occurence,decreasing=TRUE)
  roomcode.name <- names(occurence.sort[1:5])
  roomcode.name.check <- vectorinput[roomcodeindex]
  if(sum(roomcode.name==roomcode.name.check)==5){
    cumroomcode <- cumroomcode+sum(numeric[numberindex]*c(100,10,1))
  }
  #FOR PART 2 check if the string corresponds to north pole objects
  skipinalphabet <- sum(numeric[numberindex]*c(100,10,1))%%26
  newname <- sapply(encryptname, function(x) letters[(match(x,letters)+skipinalphabet-1)%%26+1])
  newname[which(is.na(newname))] <- " "
  newname.string <- paste(newname, sep="", collapse="")
  if(newname.string=="northpole object storage"){
    print("Northpole Object Storage room ID:")
    print(sum(numeric[numberindex]*c(100,10,1)))
  }
}
cumroomcode
