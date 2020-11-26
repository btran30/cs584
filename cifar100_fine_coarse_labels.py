# <a href="https://colab.research.google.com/github/btran30/cs584/blob/brenda/cifar100_fine_coarse_labels.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

import pprint as pp


fine_labels = [
    'apple',  # id 0
    'aquarium_fish',
    'baby',
    'bear',
    'beaver',
    'bed',
    'bee',
    'beetle',
    'bicycle',
    'bottle',
    'bowl',
    'boy',
    'bridge',
    'bus',
    'butterfly',
    'camel',
    'can',
    'castle',
    'caterpillar',
    'cattle',
    'chair',
    'chimpanzee',
    'clock',
    'cloud',
    'cockroach',
    'couch',
    'crab',
    'crocodile',
    'cup',
    'dinosaur',
    'dolphin',
    'elephant',
    'flatfish',
    'forest',
    'fox',
    'girl',
    'hamster',
    'house',
    'kangaroo',
    'computer_keyboard',
    'lamp',
    'lawn_mower',
    'leopard',
    'lion',
    'lizard',
    'lobster',
    'man',
    'maple_tree',
    'motorcycle',
    'mountain',
    'mouse',
    'mushroom',
    'oak_tree',
    'orange',
    'orchid',
    'otter',
    'palm_tree',
    'pear',
    'pickup_truck',
    'pine_tree',
    'plain',
    'plate',
    'poppy',
    'porcupine',
    'possum',
    'rabbit',
    'raccoon',
    'ray',
    'road',
    'rocket',
    'rose',
    'sea',
    'seal',
    'shark',
    'shrew',
    'skunk',
    'skyscraper',
    'snail',
    'snake',
    'spider',
    'squirrel',
    'streetcar',
    'sunflower',
    'sweet_pepper',
    'table',
    'tank',
    'telephone',
    'television',
    'tiger',
    'tractor',
    'train',
    'trout',
    'tulip',
    'turtle',
    'wardrobe',
    'whale',
    'willow_tree',
    'wolf',
    'woman',
    'worm',
]

mapping_coarse_fine = {
    'aquatic mammals': ['beaver', 'dolphin', 'otter', 'seal', 'whale'],
    'fish': ['aquarium_fish', 'flatfish', 'ray', 'shark', 'trout'],
    'flowers': ['orchid', 'poppy', 'rose', 'sunflower', 'tulip'],
    'food containers': ['bottle', 'bowl', 'can', 'cup', 'plate'],
    'fruit and vegetables': ['apple', 'mushroom', 'orange', 'pear',
                             'sweet_pepper'],
    'household electrical device': ['clock', 'computer_keyboard', 'lamp',
                                    'telephone', 'television'],
    'household furniture': ['bed', 'chair', 'couch', 'table', 'wardrobe'],
    'insects': ['bee', 'beetle', 'butterfly', 'caterpillar', 'cockroach'],
    'large carnivores': ['bear', 'leopard', 'lion', 'tiger', 'wolf'],
    'large man-made outdoor things': ['bridge', 'castle', 'house', 'road',
                                      'skyscraper'],
    'large natural outdoor scenes': ['cloud', 'forest', 'mountain', 'plain',
                                     'sea'],
    'large omnivores and herbivores': ['camel', 'cattle', 'chimpanzee',
                                       'elephant', 'kangaroo'],
    'medium-sized mammals': ['fox', 'porcupine', 'possum', 'raccoon', 'skunk'],
    'non-insect invertebrates': ['crab', 'lobster', 'snail', 'spider', 'worm'],
    'people': ['baby', 'boy', 'girl', 'man', 'woman'],
    'reptiles': ['crocodile', 'dinosaur', 'lizard', 'snake', 'turtle'],
    'small mammals': ['hamster', 'mouse', 'rabbit', 'shrew', 'squirrel'],
    'trees': ['maple_tree', 'oak_tree', 'palm_tree', 'pine_tree',
              'willow_tree'],
    'vehicles 1': ['bicycle', 'bus', 'motorcycle', 'pickup_truck', 'train'],
    'vehicles 2': ['lawn_mower', 'rocket', 'streetcar', 'tank', 'tractor'],
}


def print_fine_labels():
    for id, label in enumerate(fine_labels):
        print(id, " ", label)

def new_dicts():
    # fine label name -> id of fine label
    fine_id = dict()
    # id of fine label -> fine label name
    id_fine = dict()
    for id, label in enumerate(fine_labels):
        fine_id[label] = id
        id_fine[id] = label

    # coarse label name -> id of coarse label
    coarse_id = dict()
    # id of coarse label -> name of the coarse label
    id_coarse = dict()
    # name of fine label -> name of coarse label
    fine_coarse = dict()
    # id of fine label -> id of coarse label
    fine_id_coarse_id = dict()
    # id of coarse label -> id of fine label
    coarse_id_fine_id = dict()
    for id, (coarse, fines) in enumerate(mapping_coarse_fine.items()):
        coarse_id[coarse] = id
        id_coarse[id] = coarse
        fine_labels_ids = []
        for fine in fines:
            fine_coarse[fine] = coarse
            fine_label_id = fine_id[fine]
            fine_id_coarse_id[fine_label_id] = id
            fine_labels_ids.append(fine_label_id)
        coarse_id_fine_id[id] = fine_labels_ids

    dicts = ['fine_id', 'id_fine', 'coarse_id', 'id_coarse', 'fine_coarse',
             'fine_id_coarse_id', 'coarse_id_fine_id']
    for dic in dicts:
        dic_value = locals()[dic]
        print(dic + ' = ')
        pp.pprint(dic_value)



class Fine100:
  def __init__(self, fine_labels):
    self.fine_labels = fine_labels
    self.fine_id = dict()
    self.id_fine = dict() # id of fine label -> fine label name
    for id, label in enumerate(fine_labels):
        self.fine_id[label] = id
        self.id_fine[id] = label

  def id_to_label(self, id):
    return self.id_fine[id]
   
  def label_to_id(self, label):
    return self.fine_id[label]


class Coarse100:
  def __init__(self,mapping_coarse_fine, fine_labels):
      self.fine_labels = fine_labels
      # fine label name -> id of fine label
      self.fine_id = dict()
      # id of fine label -> fine label name
      self.id_fine = dict()
      for id, label in enumerate(fine_labels):
          self.fine_id[label] = id
          self.id_fine[id] = label

      self.mapping_coarse_fine = mapping_coarse_fine
      # coarse label name -> id of coarse label
      self.coarse_id = dict()
      # id of coarse label -> name of the coarse label
      self.id_coarse = dict()
      # name of fine label -> name of coarse label
      self.fine_coarse = dict()
      # id of fine label -> id of coarse label
      self.fine_id_coarse_id = dict()
      # id of coarse label -> id of fine label
      self.coarse_id_fine_id = dict()
      for id, (coarse, fines) in enumerate(mapping_coarse_fine.items()):
          self.coarse_id[coarse] = id
          self.id_coarse[id] = coarse
          fine_labels_ids = []
          for fine in fines:
              self.fine_coarse[fine] = coarse
              fine_label_id = self.fine_id[fine]
              self.fine_id_coarse_id[fine_label_id] = id
              fine_labels_ids.append(fine_label_id)
          self.coarse_id_fine_id[id] = fine_labels_ids

      self.dicts = ['fine_id', 'id_fine', 'coarse_id', 'id_coarse', 'fine_coarse',
              'fine_id_coarse_id', 'coarse_id_fine_id']

  def coarse_id_to_coarse_label(self, id):
      return self.id_coarse[id]

  def fine_id_to_coarse_id(self,id):
    return self.fine_id_coarse_id[id]

  def fine_id_to_coarse_label(self, id):
    coarse_id = self.fine_id_coarse_id[id]
    return self.id_coarse[coarse_id]

if __name__ == "__main__":
    #print_fine_labels()
    #pp.pprint(mapping_coarse_fine)
    #new_dicts()
    fine_id = 2. #baby
    fine = Fine100(fine_labels)
    print('expect:baby, is:{}'.format(fine.id_to_label(fine_id)))

    coarse = Coarse100(mapping_coarse_fine, fine_labels)
    print('expect:people, is:{}'.format(coarse.fine_id_to_coarse_label(fine_id)))
    fine_id=1 # fish
    print('expect:fish, is:{}'.format(coarse.coarse_id_to_coarse_label(fine_id)))

