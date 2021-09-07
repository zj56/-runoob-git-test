import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crime = pd.read_csv("d:/ee/crimeRatesByState.csv")
crime2 = crime[(crime.state != "United States") & (crime.state !=
"DIstrict of Columbia")] 
g = sns.jointplot(x = 'murder',y = 'burglary',data=crime2,kind="reg",size=5,ratio=3,color="g")
plt.show()
# print(crime2)
# sns.scatterplot()