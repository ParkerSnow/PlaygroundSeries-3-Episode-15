
setwd('D:/Projects/PlaygroundSeries Season 3, Episode 15/Data')
library(tidyverse)

data <- read_csv('data.csv',col_types = 'iffddddddd')

summary(data$geometry)

ggplot(gather(subset(data,select = -c(id,author,geometry))),aes(value)) + geom_histogram(bins = 10) + facet_wrap(~key,scales='free_x')

ggplot(gather(subset(data,select = c(author,geometry))),aes(value)) + geom_histogram(stat = 'count') + facet_wrap(~key,scales='free_x')
