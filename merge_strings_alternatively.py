import itertools

class MergeStringsAlternatively:
  def merge_strings_alternatively(self, word1, word2):
    list_one = list(word1)
    list_two = list(word2)

    zipped_list = list(zip(list_one, list_two))
    print(f'zipped_list: {zipped_list}')
    
    flattened_list = list(itertools.chain(*zipped_list))
    print(f'flattened_list: {flattened_list}')
    
    remainder = None
    starting_point = abs(len(list_one) - len(list_two))
    
    if len(list_one) > len(list_two):
      remainder = list_one[starting_point:]
    elif len(list_one) < len(list_two):
      remainder = list_two[starting_point:]

    print(f'remainder: {remainder}')
    
    return " ".join(flattened_list)
    
  
  def main(self):
    # print(self.merge_strings_alternatively('abc', 'pqr') == 'a p b q c r')
    # print(self.merge_strings_alternatively('ab', 'pqrs') == 'a p b q   r   s')
    print(self.merge_strings_alternatively('abcd', 'pq') == 'a p b q c   d')

  