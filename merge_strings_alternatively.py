class MergeStringsAlternatively:
  def merge_strings_alternatively(self, word1, word2):
    list_one = list(word1)
    list_two = list(word2)
  
    print(f'list_one: {list_one}')
    print(f'list_two: {list_two}')

    zipped_list = tuple(zip(*list_one, *list_two))
    print(f'zipped_list: {zipped_list}')
    
  
  def main(self):
    self.merge_strings_alternatively('abc', 'pqr')
    # assert merge_strings_alternatively('abc', 'pqr') == 'a p b q c r'
    # assert merge_strings_alternatively('ab', 'pqrs') == 'a p b q   r   s'
    # assert merge_strings_alternatively('abcd', 'pq') == 'a p b q c   d'

  