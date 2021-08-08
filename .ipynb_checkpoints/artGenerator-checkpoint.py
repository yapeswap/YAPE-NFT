{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "85ee8012",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import torch\n",
    "import torchvision\n",
    "import pandas as pd\n",
    "import torch.nn as nn\n",
    "import torch.nn.functional as F\n",
    "from tqdm.notebook import tqdm\n",
    "import torchvision.models as models\n",
    "from torch.utils.data import Dataset\n",
    "from torch.utils.data import DataLoader\n",
    "from torch.utils.data import random_split\n",
    "from torchvision.utils import make_grid\n",
    "import torchvision.transforms as transforms\n",
    "from torchvision.datasets.folder import default_loader\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "949a98f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "artists = pd.read_csv(\"../input/best-artworks-of-all-time/artists.csv\")\n",
    "\n",
    "for i in artists['name']:\n",
    "    print(i,end=\" | \")\n",
    "    \n",
    "##REMOVE THIS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90e438e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
