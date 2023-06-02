  
  def missing_nan(self, array) :

      nan_indices = np.isnan(array)

      non_nan_indices = np.where(~nan_indices)[0]

      for i in np.where(nan_indices)[0]:

        prev_index = non_nan_indices[non_nan_indices < i][-1]
        next_index = non_nan_indices[non_nan_indices > i][0]
        
        mean = (array[prev_index] + array[next_index]) / 2
        
        array[i] = mean

      return  array
