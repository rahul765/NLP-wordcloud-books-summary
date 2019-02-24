
library(webshot)
#webshot::install_phantomjs()
library("htmlwidgets")
require(devtools)
library(wordcloud2)
abc = demoFreq

setwd("~/Work/Python/MIS_PROJECT/csv")
book_name = list.files(pattern="*.csv")
for(book in book_name) {
  setwd("~/Work/Python/csv")
  book_n <- gsub(".csv","",book)
  print(book_n)
  MyData <- read.csv(file=book, header=TRUE, sep=",")
  my_graph <- wordcloud2(MyData, color = "random-light", backgroundColor = "white")
  saveWidget(my_graph,paste(book_n,".html",sep = ""),selfcontained = F)
  webshot(paste(book_n,".html",sep = ""),paste(book_n,".pdf",sep = ""), delay =5, vwidth = 480, vheight=480)
}

current_folder <- getwd()
new_folder <- "/Users/rahulpal/Work/Python/MIS_PROJECT/wordcloud"
list_of_files <- list.files(current_folder, ".pdf$") 
# ".py$" is the type of file you want to copy. Remove if copying all types of files. 
file.copy(file.path(current_folder,list_of_files), new_folder)
