{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "# Libraries\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import random\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from tensorflow.keras import Sequential\n",
        "from tensorflow.keras.layers import Dense, Activation, BatchNormalization\n",
        "from tensorflow.keras.initializers import he_normal\n",
        "from tensorflow.keras.optimizers import Adam\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "import pdb"
      ],
      "metadata": {
        "id": "cErcP-vW4UrJ"
      },
      "execution_count": 162,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Generate data\n",
        "def generate_data(total_data=10):\n",
        "  x = []\n",
        "  y = []\n",
        "  for each in range(total_data):\n",
        "    x1_val = random.randint(-11, 11)\n",
        "    x2_val = random.randint(-9, 9)\n",
        "    x3_val = random.randint(-7, 7)\n",
        "    y1_val = (x1_val ** 2) + (7*x2_val) + (4*x3_val)\n",
        "    y2_val = (x1_val ** 2) + (6*x2_val) + (3*x3_val)\n",
        "    y3_val = (x1_val ** 2) + (5*x2_val) + (-21*x3_val)\n",
        "    y4_val = (x1_val ** 2) + (9*x2_val) + (-11*x3_val)\n",
        "    x.append([x1_val, x2_val, x3_val])\n",
        "    y.append([y1_val, y2_val, y3_val, y4_val])\n",
        "  return x, y\n",
        "\n",
        "X, Y = generate_data(total_data=10000)\n",
        "print(X)\n",
        "print(Y)\n",
        "\n",
        "data = pd.DataFrame({\n",
        "        'X1' : [rec[0] for rec in X],\n",
        "        'X2' : [rec[1] for rec in X],\n",
        "        'X3' : [rec[2] for rec in X],\n",
        "        'Y1' : [rec[0] for rec in Y],\n",
        "        'Y2' : [rec[1] for rec in Y],\n",
        "        'Y3' : [rec[2] for rec in Y],\n",
        "        'Y4' : [rec[3] for rec in Y]})\n",
        "data"
      ],
      "metadata": {
        "id": "Dx_WNXoH6vQX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Do normalizataion of the input. average = 0, std_deviation = 1\n",
        "norm_x = StandardScaler()\n",
        "norm_y = StandardScaler()"
      ],
      "metadata": {
        "id": "qz6gbIXk6zgZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def build_model_for_inputs():\n",
        "  model = Sequential()\n",
        "\n",
        "  # Hidden layer\n",
        "  model.add(Dense(10, input_dim=3, kernel_initializer=he_normal(), activation='relu'))\n",
        "  # output Layer\n",
        "  model.add(Dense(4))\n",
        "\n",
        "  model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')\n",
        "  return model\n",
        "\n",
        "model2 = build_model_for_inputs()\n",
        "model2"
      ],
      "metadata": {
        "id": "MWo2MLYK62Aa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def train_model_for_inputs(model, x, y):\n",
        "  xnorm = norm_x.fit_transform(np.array(x))\n",
        "  ynorm = norm_y.fit_transform(np.array(y))\n",
        "\n",
        "  # Train the model\n",
        "  model.fit(xnorm, ynorm, epochs=200, batch_size=10, verbose=1)\n",
        "train_model_for_inputs(model2, X, Y)"
      ],
      "metadata": {
        "id": "OUDusRqp65vO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Do some predictions\n",
        "def predict_outputs(model=None, total_data=10):\n",
        "  X1, YT = generate_data(total_data=20)\n",
        "  print (X1)\n",
        "  print (YT)\n",
        "  xnorm = norm_x.transform(np.array(X1))\n",
        "  predictions = model.predict(xnorm)\n",
        "\n",
        "  YP = norm_y.inverse_transform(predictions)\n",
        "\n",
        "  return X1, YT, YP\n",
        "\n",
        "X1, YTrue, YPred = predict_outputs(total_data=20, model=model2)\n",
        "\n",
        "data = pd.DataFrame({\n",
        "        'X1_data' : [rec[0] for rec in X1],\n",
        "        'X2_data' : [rec[1] for rec in X1],\n",
        "        'X3_data' : [rec[2] for rec in X1],\n",
        "        'Y1_expected' : [rec[0] for rec in YTrue],\n",
        "        'Y1_predicted' : [rec[0] for rec in YPred],\n",
        "        'Y2_expected' : [rec[1] for rec in YTrue],\n",
        "        'Y2_predicted' : [rec[1] for rec in YPred],\n",
        "        'Y3_expected' : [rec[2] for rec in YTrue],\n",
        "        'Y3_predicted' : [rec[2] for rec in YPred],\n",
        "        'Y4_expected' : [rec[3] for rec in YTrue],\n",
        "        'Y4_predicted' : [rec[3] for rec in YPred]\n",
        "        })\n",
        "data"
      ],
      "metadata": {
        "id": "3it8KdLu69F4"
      },
      "execution_count": null,
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