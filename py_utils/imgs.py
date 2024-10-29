from typing import List, Union, Set
from pathlib import Path
from PIL import Image

def getValuesInImg(img_fpath_ : str) -> Set[Union[int, List[int]]]:
    """
    Get the set of values present in the given image.

    Args:
        img_fpath_ (str): Path to the image file.

    Returns:
        The set of values found in the image.

    Example:
        img = [ [0, 1, 0], [0, 1, 3], [1, 1, 3] ]
        values = getValuesInImg(path_to_img)
        print(values)
        [0, 1, 3]
    """
    
    assert(Path(img_fpath_).is_file())

    img = Image.open(img_fpath_)

    return set(list(img.getdata()))
