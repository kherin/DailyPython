def extract():
  filenames = [
    'German_shorthaired_pointer_04986.jpg', 
    'Dalmatian_04068.jpg', 
    'Basset_hound_01034.jpg', 
    'fox_squirrel_01.jpg'
  ]
  
  for filename in filenames:
    pet_label = ' '.join(
      list(
        filter(lambda token: token.isalpha(), filename.lower().strip().split('_'))
      )
    )
    print(f'${filename} is {pet_label}')