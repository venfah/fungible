{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rX8mhOLljYeM"
      },
      "source": [
        "##### Copyright 2019 The TensorFlow Authors."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cellView": "form",
        "id": "BZSlp3DAjdYf"
      },
      "outputs": [],
      "source": [
        "#@title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3wF5wszaj97Y"
      },
      "source": [
        "# TensorFlow 2 quickstart for beginners"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DUNzJc4jTj6G"
      },
      "source": [
        "<table class=\"tfo-notebook-buttons\" align=\"left\">\n",
        "  <td>\n",
        "    <a target=\"_blank\" href=\"https://www.tensorflow.org/tutorials/quickstart/beginner\"><img src=\"https://www.tensorflow.org/images/tf_logo_32px.png\" />View on TensorFlow.org</a>\n",
        "  </td>\n",
        "  <td>\n",
        "    <a target=\"_blank\" href=\"https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb\"><img src=\"https://www.tensorflow.org/images/colab_logo_32px.png\" />Run in Google Colab</a>\n",
        "  </td>\n",
        "  <td>\n",
        "    <a target=\"_blank\" href=\"https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb\"><img src=\"https://www.tensorflow.org/images/GitHub-Mark-32px.png\" />View source on GitHub</a>\n",
        "  </td>\n",
        "  <td>\n",
        "    <a href=\"https://storage.googleapis.com/tensorflow_docs/docs/site/en/tutorials/quickstart/beginner.ipynb\"><img src=\"https://www.tensorflow.org/images/download_logo_32px.png\" />Download notebook</a>\n",
        "  </td>\n",
        "</table>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "04QgGZc9bF5D"
      },
      "source": [
        "This short introduction uses [Keras](https://www.tensorflow.org/guide/keras/overview) to:\n",
        "\n",
        "1. Load a prebuilt dataset.\n",
        "1. Build a neural network machine learning model that classifies images.\n",
        "2. Train this neural network.\n",
        "3. Evaluate the accuracy of the model."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import random\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from tensorflow.keras import Sequential\n",
        "from tensorflow.keras.layers import Dense, Activation, BatchNormalization\n",
        "from tensorflow.keras.initializers import he_normal\n",
        "from tensorflow.keras.optimizers import Adam\n",
        "from sklearn.preprocessing import StandardScaler\n"
      ],
      "metadata": {
        "id": "Rash8aKY5TJ-"
      },
      "execution_count": 5,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "beginner.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}