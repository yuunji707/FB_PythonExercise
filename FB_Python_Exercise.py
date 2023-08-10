import numpy as np
import pandas as pd

#Generate 100x100 array with values between 0 to 20
array = np.random.randint(0, 21, size=(100, 100))

#Create dataframe for results
results = pd.DataFrame(columns=['Row', 'Column', 'Value'])

#Check for adjacent pixels with same value. Record coords
for row in range(99):
    for col in range(99):
        if array[row, col] == array[row + 1, col] or array[row, col] == array[row, col + 1]:
            results = results._append({'Row': row, 'Column': col, 'Value': array[row, col]}, ignore_index=True)

#Save results to sheet1 as Adjacent_pixels
results.to_csv('Adjacent_Pixels.csv', index=False)

#Save the original array to sheet2
np.savetxt('Original_Array.csv', array, delimiter=',', fmt='%d', header='Original Array', comments='')

#Find max num in each column two different ways
max_col_np = np.max(array, axis=0)
max_col_pd = array.max(axis=0)

#Create dataframe for max values
max_values_df = pd.DataFrame({'Max_Column_Numpy': max_col_np, 'Max_Column_Pandas': max_col_pd})

# Save the max values DataFrame to CSV sheet3
max_values_df.to_csv('Max_Values.csv', index_label='Column')

