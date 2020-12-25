connection <- read.csv("mouse_expression_data_sets.csv", header = TRUE)
colClasses = c("integer")
df <- read.csv(text="data_set_id", colClasses = colClasses)
for(i in 0:length(connection[,1])) {
  data <- connection[i,1]
  df[i,1] <- data
}
write.csv(df,"new_mouse_expression_data_sets.csv", row.names = FALSE)