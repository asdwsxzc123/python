import numpy as np

# print(t1)
def fill_ndarray(t1):
  for i in range(t1.shape[1]):
    # 列
    temp_col = t1[:,i]
    # 有nan
    nan_num = np.count_nonzero(temp_col !=temp_col)
    if nan_num != 0:
      # 不为nan的数组
      temp_not_nan_col = temp_col[temp_col==temp_col]
      # 选中当前为nan的位置,吧值赋值为不为nan的均值
      temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()

if __name__ == "__main__":
    t1 = np.arange(12).reshape((3,4)).astype('float')
    t1[1,2:] = np.nan
    fill_ndarray(t1)
    print(t1)