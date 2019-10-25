# Import pandas package 
import pandas as pd 
import plotting_sample01 as ps
import plotting_3d as p3d


# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data) 
  
# select two columns 
df[['Name', 'Qualification']] 

print(df)

#ps.plot_sample()
p3d.plot_3d()


# comment
