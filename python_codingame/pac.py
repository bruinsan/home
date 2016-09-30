'''
// in, out are m x n images (integer data)
// K is the kernel size (KxK) - currently needs to be an odd number, e.g. 3
// coeffs[K][K] is a 2D array of integer coefficients
// scale is a scaling factor to normalise the filter gain

for (i = K / 2; i < m - K / 2; ++i) // iterate through image
{
  for (j = K / 2; j < n - K / 2; ++j)
  {
    int sum = 0; // sum will be the sum of input data * coeff terms

    for (ii = - K / 2; ii <= K / 2; ++ii) // iterate over kernel
    {
      for (jj = - K / 2; jj <= K / 2; ++jj)
      {
        int data = in[i + ii][j +jj];
        int coeff = coeffs[ii + K / 2][jj + K / 2];

        sum += data * coeff;
      }
    }
    out[i][j] = sum / scale; // scale sum of convolution products and store in output
  }
}
'''

input_img = ['..0.0.0.0.0..', '.............', '.0.0.0.0.0.0.', '.............', '...0.0.0.0...', '.0.........0.', '...0.0.0.0...', '.............', '.0.0.0.0.0.0.', '.............', '..0.0.0.0.0..']


def convert_point_to_number(instant_map):
    new_map = []
    for i in instant_map:
        new_map.append(i.replace('.','1'))
    
    test = []    
    for j in new_map:
        test.append([1 - int(val) for val in j])
    
    return test
'''
mask = 3    # mask size 3x3
width = 13  # grid size
height = 11

for i in range(mask/2, width - k/2):
    for j in range(mask/2, height - mask/2):
        _sum = 0
        for m_i in range(-mask/2, mask/2):
            for m_j in range(-mask/2, mask/2):
                data = input_img[i+m_i][j+j_m]
                coef = mask_coeffs[m_i+mask/2]+[m_j+mask/2]

                _sum += data * coeff

        output_img[i][j] = _sum
'''
print convert_point_to_number(input_img)

