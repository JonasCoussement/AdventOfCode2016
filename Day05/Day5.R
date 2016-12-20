library(digest)
sumof5 <- 8
number <- 1
startstring <- "ffykfhsq"
while(sumof5>0){
  string <- paste0(startstring,number)
  hash <- digest(string, algo="md5", serialize=F)
  hashstart <- sapply(hash, function(x) strsplit(as.character(x),""))[[1]][1:6]
  if(prod(hashstart[1:5]==rep("0",5))){
    print(number)
    print(hashstart[6])
    sumof5 = sumof5-1
  }
  number <- number+1
}

#part 2: step 1: fill in the numbers we already know
numbers <- c("515840","844745","2968550","4034943","5108969","5257971","5830668","5833677")
passcode <- rep(as.numeric(NA),8)
for(i in 1:length(numbers)){
  string <- paste0(startstring,numbers[i])
  hash <- digest(string, algo="md5", serialize=F)
  hashstart <- sapply(hash, function(x) strsplit(as.character(x),""))[[1]][1:7]
  number6 <- suppressWarnings(as.numeric(hashstart[6]))
  print(string)
  if(is.na(number6)){
    
  } else {
    if(is.na(passcode[number6+1])){
      passcode[number6+1] <- hashstart[7]
    }
  }
}
#part 2: step 2: continue brute-forcing from there
number <- 5833678
while(sum(is.na(passcode))>0){
  string <- paste0(startstring,number)
  hash <- digest(string, algo="md5", serialize=F)
  hashstart <- sapply(hash, function(x) strsplit(as.character(x),""))[[1]][1:7]
  if(prod(hashstart[1:5]==rep("0",5))){
    number6 <- suppressWarnings(as.numeric(hashstart[6]))
    if(is.na(number6)){
      
    } else {
      if(is.na(passcode[number6+1])){
        print(number)
        print(hashstart)
        passcode[number6+1] <- hashstart[7]
      }
    }
  }
  number <- number+1
}
resultnumbers <- c("6497076","23867827","26383109","8962195","24090051","6681564")