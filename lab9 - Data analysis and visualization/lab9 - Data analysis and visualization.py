import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 30 points
def read_and_filter(filepath, upper_bound, lower_bound):
    #TODO Implement
    veri = pd.read_csv(filepath)
    veri=veri[(veri['Y'] < upper_bound) & (veri['Y'] > lower_bound)]
    veri_cleaned=veri['Y']
    return veri_cleaned
    pass # pass is a placeholder statement that does nothing, you can remove after your implementation is complete.

# 30 points
def plot_data(data, title, label_of_x, label_of_y, output_path):
    #TODO Implement
    x_axis=range(1,len(data)+1)
    plt.plot(x_axis, data)
    plt.xlabel(label_of_x)
    plt.ylabel(label_of_y)
    plt.title(title)
    # FOLLOWING CODE BLOCK IS CONTROL LOGIC FOR DEBUGGING AND TESTING PURPOSES
    # WRITE YOUR CODE ABOVE THIS PART
    # DO NOT DELETE OR CHANGE BELOW!
    if output_path == "":
        plt.show()
    else:
        plt.savefig(output_path)

# 10 points
def difference_with_average(arr):
    #TODO Implement
    data2=arr
    data2_avg=data2.mean()
    data2_differences=np.round(data2-data2_avg,1)
    return data2_differences

# 10 points
def normalize_the_data(arr):
    #TODO Implement
    b=np.zeros(len(arr))
    for i in range(len(arr)):
      b[i]=(arr.iloc[i]-min(arr))/(max(arr)-min(arr))
    return b

# 20 points
def get_averages_in_periods(data, period):
    #TODO Implement
    avg_periods=[]
    for i in range(0,len(data),period):
        avg_periods.append(data[i:i+period].mean())
    return(np.round(avg_periods,1))



# Testing function, you can change it as you wish, it will not be graded.
def test():        
    try:
        arr = read_and_filter("data.csv", 100, 0)
        plot_data(arr, "CCI", "Months", "Percentage", "")
    except Exception as e:
        print("ERROR:",e)

    try:
        diff_arr = difference_with_average(arr)
        plot_data(diff_arr, "DIFFERENCE WITH AVERAGE", "Months", "Percentage", "")
    except Exception as e:
        print("ERROR:",e)
        
   
    try: 
        normalized_data = normalize_the_data(arr)
        plot_data(normalized_data, "NORMALIZED CCI", "Months", "Percentage", "")
    except Exception as e:
        print("ERROR:",e)

    try:    
        avg_data = get_averages_in_periods(arr, 3)
        plot_data(avg_data, "AVERAGE CCI", "Quarters", "Percentage", "")
    except Exception as e:
        print("ERROR:",e)
        
# Calling test function to ease your debugging.
# This condition ensures that this function will not be called when your code is imported in the actual evaluation.
if __name__ == "__main__":
    test()
