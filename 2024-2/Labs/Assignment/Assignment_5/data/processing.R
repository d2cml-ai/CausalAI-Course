library(causaldata)
library(tidyverse)

data("nsw_mixtape")
data("cps_mixtape")

nsw_data_control <- cps_mixtape %>%
        bind_rows(nsw_mixtape %>% filter(treat == 1)) %>%
        transform(re74 = re74 / 1000,
                  re75 = re75 / 1000,
                  re78 = re78 / 1000) %>%
        mutate(agesq = age^2,
               agecube = age^3,
               educsq = educ*educ,
               u74 = case_when(re74 == 0 ~ 1, TRUE ~ 0),
               u75 = case_when(re75 == 0 ~ 1, TRUE ~ 0),
               interaction1 = educ*re74,
               re74sq = re74^2,
               re75sq = re75^2) %>%
        select(-data_id)

nsw_experiment <- nsw_mixtape %>% select(-data_id)

write.csv(nsw_experiment, "C:/Users/Work/Desktop/experimental_control.csv", row.names = F)
write.csv(nsw_data_control, "C:/Users/Work/Desktop/biased_control.csv", row.names = F)

