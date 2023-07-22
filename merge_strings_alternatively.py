import itertools

class MergeStringsAlternatively:
  def merge_strings_alternatively(self, word1, word2):
    list_one = list(word1)
    list_two = list(word2)

    max_length = max(len(list_one), len(list_two))
    result = []

    for index in range(max_length):
      if index > len(list_one) - 1:
        result.append(' ')
      else:
        result.append(list_one[index])

      if index > len(list_two) - 1:
        result.append(' ')
      else:
        result.append(list_two[index])

    return ' '.join(result).strip()
    
  
  def main(self):
    print(self.merge_strings_alternatively('abc', 'pqr') == 'a p b q c r')
    print(self.merge_strings_alternatively('ab', 'pqrs') == 'a p b q   r   s')
    print(self.merge_strings_alternatively('abcd', 'pq') == 'a p b q c   d')

  