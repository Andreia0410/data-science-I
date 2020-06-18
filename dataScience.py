{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "introdução.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOyFT3EzDXPbYLywdshUe9K",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Andreia0410/Albuquerque/blob/master/dataScience.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bqJ5Eg_hLHBf",
        "colab_type": "text"
      },
      "source": [
        "# **Analisando as notas em geral!**\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "thQkgf6rF_sZ",
        "colab_type": "code",
        "outputId": "59f51754-7e4e-499b-bcf8-4ef6c36fa4bf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 163
        }
      },
      "source": [
        "print(sns.__version__)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-6-f656a9a2faef>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__version__\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'sns' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X1LfieU2VFsD",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "P7GeC5y0nuPv",
        "colab_type": "code",
        "outputId": "9b0de427-a449-488b-a7ff-8f6f5582184d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "#Columns --> Retorna os valores das colunas\n",
        "#Head --> Cabeçalho\n",
        "\n",
        "notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']\n",
        "notas.head()\n",
        "#print(notas)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>usuarioId</th>\n",
              "      <th>filmeId</th>\n",
              "      <th>nota</th>\n",
              "      <th>momento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982703</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964981247</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>6</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982224</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>47</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964983815</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>50</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964982931</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   usuarioId  filmeId  nota    momento\n",
              "0          1        1   4.0  964982703\n",
              "1          1        3   4.0  964981247\n",
              "2          1        6   4.0  964982224\n",
              "3          1       47   5.0  964983815\n",
              "4          1       50   5.0  964982931"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RbL8jCJgmtdn",
        "colab_type": "code",
        "outputId": "d0390bdb-94bb-4dea-adfc-f42b9fdce4a4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "notas = pd.read_csv('ratings.csv')\n",
        "notas.head()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>userId</th>\n",
              "      <th>movieId</th>\n",
              "      <th>rating</th>\n",
              "      <th>timestamp</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982703</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964981247</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>6</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982224</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>47</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964983815</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>50</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964982931</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   userId  movieId  rating  timestamp\n",
              "0       1        1     4.0  964982703\n",
              "1       1        3     4.0  964981247\n",
              "2       1        6     4.0  964982224\n",
              "3       1       47     5.0  964983815\n",
              "4       1       50     5.0  964982931"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n94MdyP-LKje",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uWso_33o6m2c",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ov3eePmcoYXz",
        "colab_type": "code",
        "outputId": "728d780b-511f-42bc-96c8-5e12475e3ef9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#Unique --> Itens únicos são retornados em ordem de aparência.\n",
        "#Isso não os classifica.\n",
        "\n",
        "notas['nota'].unique()"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([4. , 5. , 3. , 2. , 1. , 4.5, 3.5, 2.5, 0.5, 1.5])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KP6xz_M1rSSd",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K0m2bq5FrWde",
        "colab_type": "code",
        "outputId": "f3fb788d-b71b-466b-fc42-9533a15babf4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "#value_counts --> Retorna a contagem da quantidade de pessoas\n",
        "#que avaliaram os filmes conforme as notas.\n",
        "\n",
        "notas['nota'].value_counts()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.0    26818\n",
              "3.0    20047\n",
              "5.0    13211\n",
              "3.5    13136\n",
              "4.5     8551\n",
              "2.0     7551\n",
              "2.5     5550\n",
              "1.0     2811\n",
              "1.5     1791\n",
              "0.5     1370\n",
              "Name: nota, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XeYw-ddh4cHP",
        "colab_type": "code",
        "outputId": "3d216d58-e6e5-47d8-da4d-4afa18b2e61a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#mean --> Retorna a média das avalições\n",
        "\n",
        "notas['nota'].mean()\n"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.501556983616962"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_9qrpjw36UGt",
        "colab_type": "code",
        "outputId": "0c647fa8-0762-4670-ea16-cb53176a5bb0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 221
        }
      },
      "source": [
        "#Retorna os valores da coluna\n",
        "\n",
        "notas['nota']"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0         4.0\n",
              "1         4.0\n",
              "2         4.0\n",
              "3         5.0\n",
              "4         5.0\n",
              "         ... \n",
              "100831    4.0\n",
              "100832    5.0\n",
              "100833    5.0\n",
              "100834    5.0\n",
              "100835    3.0\n",
              "Name: nota, Length: 100836, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k4pyxVmm6oSR",
        "colab_type": "code",
        "outputId": "6a254325-94a5-4239-d645-a001b23348af",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        }
      },
      "source": [
        "notas['nota'].head()"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    4.0\n",
              "1    4.0\n",
              "2    4.0\n",
              "3    5.0\n",
              "4    5.0\n",
              "Name: nota, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W5HYfrwK6xwh",
        "colab_type": "code",
        "outputId": "ef5f6a44-b909-4cd6-8a10-5fdc24ad6b82",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        }
      },
      "source": [
        "#DataFrame Plot --> Retorna a plotagem de todas as colunas com rótulos\n",
        "\n",
        "#import matplotlib\n",
        "#import matplotlib_venn\n",
        "\n",
        "notas.nota.plot(kind = 'hist')"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f40debbffd0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V4GAYPgQ_fWZ",
        "colab_type": "code",
        "outputId": "1aa049d1-3c3f-41e9-b147-bc8aed3b795e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print('Mediana', notas['nota'].median())"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mediana 3.5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qZAYVh0rEFTf",
        "colab_type": "code",
        "outputId": "20eb6097-a6bf-4000-df08-86333d9b54d4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "print('Descrição\\n', notas['nota'].describe(), '\\n')"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Descrição\n",
            " count    100836.000000\n",
            "mean          3.501557\n",
            "std           1.042529\n",
            "min           0.500000\n",
            "25%           3.000000\n",
            "50%           3.500000\n",
            "75%           4.000000\n",
            "max           5.000000\n",
            "Name: nota, dtype: float64 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hkm-QuytEZXU",
        "colab_type": "code",
        "outputId": "8507ad4a-3695-4caf-9759-b95c818a8ea3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print('Media', notas['nota'].mean())"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Media 3.501556983616962\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G8NRbRcLEm8s",
        "colab_type": "code",
        "outputId": "fb21b6e5-1d63-4c07-a50f-389ac11dbed9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 350
        }
      },
      "source": [
        "import seaborn as sns\n",
        "\n",
        "sns.boxplot(notas['nota'])"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.\n",
            "  import pandas.util.testing as tm\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f40d3f76710>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Jkz8s06sE_eo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IDy7VM6aLrj-",
        "colab_type": "text"
      },
      "source": [
        "# **Olhando os filmes!**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G3zOMiLUFEx7",
        "colab_type": "code",
        "outputId": "6646d355-c405-4232-b516-67acb3431a88",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "filmes = pd.read_csv('movies.csv')\n",
        "filmes.head\n",
        "\n",
        "filmes.columns = ['Filme', 'Titulo', 'Genero']\n",
        "filmes.head()"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Filme</th>\n",
              "      <th>Titulo</th>\n",
              "      <th>Genero</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Toy Story (1995)</td>\n",
              "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>Jumanji (1995)</td>\n",
              "      <td>Adventure|Children|Fantasy</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>Grumpier Old Men (1995)</td>\n",
              "      <td>Comedy|Romance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>Waiting to Exhale (1995)</td>\n",
              "      <td>Comedy|Drama|Romance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>Father of the Bride Part II (1995)</td>\n",
              "      <td>Comedy</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Filme  ...                                       Genero\n",
              "0      1  ...  Adventure|Animation|Children|Comedy|Fantasy\n",
              "1      2  ...                   Adventure|Children|Fantasy\n",
              "2      3  ...                               Comedy|Romance\n",
              "3      4  ...                         Comedy|Drama|Romance\n",
              "4      5  ...                                       Comedy\n",
              "\n",
              "[5 rows x 3 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ekJp_INoF7hA",
        "colab_type": "code",
        "outputId": "4a819ff7-999c-4269-9ac1-aeb776dce76b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "notas.head()"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>usuarioId</th>\n",
              "      <th>filmeId</th>\n",
              "      <th>nota</th>\n",
              "      <th>momento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982703</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964981247</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>6</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982224</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>47</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964983815</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>50</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964982931</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   usuarioId  filmeId  nota    momento\n",
              "0          1        1   4.0  964982703\n",
              "1          1        3   4.0  964981247\n",
              "2          1        6   4.0  964982224\n",
              "3          1       47   5.0  964983815\n",
              "4          1       50   5.0  964982931"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PV7DQYjRKmdP",
        "colab_type": "text"
      },
      "source": [
        "#**Analisando notas específicas por filme**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XUE6an_2KbSI",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fukf6PaOHROQ",
        "colab_type": "code",
        "outputId": "01f392db-c517-45d4-f20d-c69863affe3b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 221
        }
      },
      "source": [
        "#Trabalhando com query(s) --> Perguntas que vc pode fazer aos dados \n",
        "\n",
        "\n",
        "notas.query('filmeId == 1').nota  #Comparando, quais as notas dos filmeId = 1\n",
        "                                  #só que trazendo os valores somente da coluna nota."
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        4.0\n",
              "516      4.0\n",
              "874      4.5\n",
              "1434     2.5\n",
              "1667     4.5\n",
              "        ... \n",
              "97364    2.5\n",
              "98479    4.0\n",
              "98666    2.5\n",
              "99497    3.0\n",
              "99534    5.0\n",
              "Name: nota, Length: 215, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DubESY2eJNOZ",
        "colab_type": "code",
        "outputId": "7b6328c5-ab4c-41b0-e09f-88ad3fe6f25b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        }
      },
      "source": [
        "notas.query('filmeId == 1')  #Comparando, quais as notas dos filmeId = 1"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>usuarioId</th>\n",
              "      <th>filmeId</th>\n",
              "      <th>nota</th>\n",
              "      <th>momento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982703</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>516</th>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>847434962</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>874</th>\n",
              "      <td>7</td>\n",
              "      <td>1</td>\n",
              "      <td>4.5</td>\n",
              "      <td>1106635946</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1434</th>\n",
              "      <td>15</td>\n",
              "      <td>1</td>\n",
              "      <td>2.5</td>\n",
              "      <td>1510577970</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1667</th>\n",
              "      <td>17</td>\n",
              "      <td>1</td>\n",
              "      <td>4.5</td>\n",
              "      <td>1305696483</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>97364</th>\n",
              "      <td>606</td>\n",
              "      <td>1</td>\n",
              "      <td>2.5</td>\n",
              "      <td>1349082950</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>98479</th>\n",
              "      <td>607</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964744033</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>98666</th>\n",
              "      <td>608</td>\n",
              "      <td>1</td>\n",
              "      <td>2.5</td>\n",
              "      <td>1117408267</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99497</th>\n",
              "      <td>609</td>\n",
              "      <td>1</td>\n",
              "      <td>3.0</td>\n",
              "      <td>847221025</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99534</th>\n",
              "      <td>610</td>\n",
              "      <td>1</td>\n",
              "      <td>5.0</td>\n",
              "      <td>1479542900</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>215 rows × 4 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "       usuarioId  filmeId  nota     momento\n",
              "0              1        1   4.0   964982703\n",
              "516            5        1   4.0   847434962\n",
              "874            7        1   4.5  1106635946\n",
              "1434          15        1   2.5  1510577970\n",
              "1667          17        1   4.5  1305696483\n",
              "...          ...      ...   ...         ...\n",
              "97364        606        1   2.5  1349082950\n",
              "98479        607        1   4.0   964744033\n",
              "98666        608        1   2.5  1117408267\n",
              "99497        609        1   3.0   847221025\n",
              "99534        610        1   5.0  1479542900\n",
              "\n",
              "[215 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LEN2VGv-JAT8",
        "colab_type": "code",
        "outputId": "de578683-482d-4cb6-c3f2-699383313947",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "#Comparando, quais as notas dos filmeId = 1\n",
        "#Retornando a média.\n",
        "\n",
        "notas.query('filmeId == 1').nota.mean()"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.9209302325581397"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Lhy6udCOMe2O",
        "colab_type": "code",
        "outputId": "39abdc01-9add-4b6c-d6d4-6376bc215576",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "notas.query('filmeId == 2').nota.mean()"
      ],
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.4318181818181817"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o9_MzFcuMo1C",
        "colab_type": "code",
        "outputId": "55e8e4ea-a564-4bbf-8c53-1d387c572da3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# groupby --> Agrupando os filmes\n",
        "notas.groupby('filmeId')"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f40d37d4d68>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cGWwU02ONU2q",
        "colab_type": "code",
        "outputId": "1699d9fd-799d-456b-cb42-3b1c287c7cfa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 450
        }
      },
      "source": [
        "notas.groupby('filmeId').mean()"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>usuarioId</th>\n",
              "      <th>nota</th>\n",
              "      <th>momento</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>filmeId</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>306.530233</td>\n",
              "      <td>3.920930</td>\n",
              "      <td>1.129835e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>329.554545</td>\n",
              "      <td>3.431818</td>\n",
              "      <td>1.135805e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>283.596154</td>\n",
              "      <td>3.259615</td>\n",
              "      <td>1.005110e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>219.857143</td>\n",
              "      <td>2.357143</td>\n",
              "      <td>8.985789e+08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>299.571429</td>\n",
              "      <td>3.071429</td>\n",
              "      <td>9.926643e+08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>193581</th>\n",
              "      <td>184.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.537109e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>193583</th>\n",
              "      <td>184.000000</td>\n",
              "      <td>3.500000</td>\n",
              "      <td>1.537110e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>193585</th>\n",
              "      <td>184.000000</td>\n",
              "      <td>3.500000</td>\n",
              "      <td>1.537110e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>193587</th>\n",
              "      <td>184.000000</td>\n",
              "      <td>3.500000</td>\n",
              "      <td>1.537110e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>193609</th>\n",
              "      <td>331.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.537158e+09</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>9724 rows × 3 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "          usuarioId      nota       momento\n",
              "filmeId                                    \n",
              "1        306.530233  3.920930  1.129835e+09\n",
              "2        329.554545  3.431818  1.135805e+09\n",
              "3        283.596154  3.259615  1.005110e+09\n",
              "4        219.857143  2.357143  8.985789e+08\n",
              "5        299.571429  3.071429  9.926643e+08\n",
              "...             ...       ...           ...\n",
              "193581   184.000000  4.000000  1.537109e+09\n",
              "193583   184.000000  3.500000  1.537110e+09\n",
              "193585   184.000000  3.500000  1.537110e+09\n",
              "193587   184.000000  3.500000  1.537110e+09\n",
              "193609   331.000000  4.000000  1.537158e+09\n",
              "\n",
              "[9724 rows x 3 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3qJjCBfoNydy",
        "colab_type": "code",
        "outputId": "186f8f51-d22e-463b-dd9b-13a8df43c69c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 180
        }
      },
      "source": [
        "notas.groupby('filmeId').mean().nota\n",
        "media_filme.head()"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-46-6e10a032e902>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mnotas\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgroupby\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'filmeId'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnota\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mmedia_filme\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'media_filme' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1wpYTBDHOvbY",
        "colab_type": "code",
        "outputId": "5633136e-25fa-4670-b98e-0a89377019a6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 180
        }
      },
      "source": [
        "#media_filme.plot(kind = 'hist')\n",
        "media_filme.plot()"
      ],
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-47-fd3bb45fc82f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#media_filme.plot(kind = 'hist')\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mmedia_filme\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'media_filme' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CXfCeGisPJaF",
        "colab_type": "code",
        "outputId": "3f92dc42-aa29-4c85-9502-30cd34e3a55f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 248
        }
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "plt.figure(figsize= (5, 8))\n",
        "sns.boxplot(y=media_filme)\n",
        "\n",
        "#sns.boxplot(media_filme)\n",
        " #Visualização do gráfico no eixo y"
      ],
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-48-05c4b30ce90c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfigure\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfigsize\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m8\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0msns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mboxplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmedia_filme\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;31m#sns.boxplot(media_filme)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'media_filme' is not defined"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 360x576 with 0 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bthuALoLPTk9",
        "colab_type": "code",
        "outputId": "578db40b-be8c-43dd-84c8-6039135bbe4e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 170
        }
      },
      "source": [
        "#Avaliação considerada média de um filme de acordo com a contagem\n",
        "media_filme.describe()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count    9724.000000\n",
              "mean        3.262448\n",
              "std         0.869874\n",
              "min         0.500000\n",
              "25%         2.800000\n",
              "50%         3.416667\n",
              "75%         3.911765\n",
              "max         5.000000\n",
              "Name: nota, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 117
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tGfeqWYVPj_s",
        "colab_type": "code",
        "outputId": "ff30411a-5829-4d8f-e8e8-17cb11c950b4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        }
      },
      "source": [
        "# Distribuição das notas - Quantas barras escolher para avaliar as notas?\n",
        "# Ou seja, quantos bins()\n",
        "\n",
        "sns.distplot(media_filme)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f83716725f8>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 126
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "auyXIWdcQkjf",
        "colab_type": "code",
        "outputId": "627e124d-eaf6-43b0-9c7a-a6bb3db98cce",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        }
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.hist(media_filme)\n",
        "plt.title('Histogrma das médias dos filmes\\n')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'Histogrma das médias dos filmes\\n')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 131
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gs9xk7XGJVuq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CzR7ucnm5mvS",
        "colab_type": "code",
        "outputId": "ce0331dc-7c56-43fc-a129-a32c5e44ac21",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 717
        }
      },
      "source": [
        "tmdb = pd.read_csv('tmdb_5000_movies.csv')\n",
        "tmdb.head()"
      ],
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>budget</th>\n",
              "      <th>genres</th>\n",
              "      <th>homepage</th>\n",
              "      <th>id</th>\n",
              "      <th>keywords</th>\n",
              "      <th>original_language</th>\n",
              "      <th>original_title</th>\n",
              "      <th>overview</th>\n",
              "      <th>popularity</th>\n",
              "      <th>production_companies</th>\n",
              "      <th>production_countries</th>\n",
              "      <th>release_date</th>\n",
              "      <th>revenue</th>\n",
              "      <th>runtime</th>\n",
              "      <th>spoken_languages</th>\n",
              "      <th>status</th>\n",
              "      <th>tagline</th>\n",
              "      <th>title</th>\n",
              "      <th>vote_average</th>\n",
              "      <th>vote_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>237000000</td>\n",
              "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
              "      <td>http://www.avatarmovie.com/</td>\n",
              "      <td>19995</td>\n",
              "      <td>[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...</td>\n",
              "      <td>en</td>\n",
              "      <td>Avatar</td>\n",
              "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
              "      <td>150.437577</td>\n",
              "      <td>[{\"name\": \"Ingenious Film Partners\", \"id\": 289...</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>2009-12-10</td>\n",
              "      <td>2787965087</td>\n",
              "      <td>162.0</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...</td>\n",
              "      <td>Released</td>\n",
              "      <td>Enter the World of Pandora.</td>\n",
              "      <td>Avatar</td>\n",
              "      <td>7.2</td>\n",
              "      <td>11800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>300000000</td>\n",
              "      <td>[{\"id\": 12, \"name\": \"Adventure\"}, {\"id\": 14, \"...</td>\n",
              "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
              "      <td>285</td>\n",
              "      <td>[{\"id\": 270, \"name\": \"ocean\"}, {\"id\": 726, \"na...</td>\n",
              "      <td>en</td>\n",
              "      <td>Pirates of the Caribbean: At World's End</td>\n",
              "      <td>Captain Barbossa, long believed to be dead, ha...</td>\n",
              "      <td>139.082615</td>\n",
              "      <td>[{\"name\": \"Walt Disney Pictures\", \"id\": 2}, {\"...</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>2007-05-19</td>\n",
              "      <td>961000000</td>\n",
              "      <td>169.0</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>Released</td>\n",
              "      <td>At the end of the world, the adventure begins.</td>\n",
              "      <td>Pirates of the Caribbean: At World's End</td>\n",
              "      <td>6.9</td>\n",
              "      <td>4500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>245000000</td>\n",
              "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
              "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
              "      <td>206647</td>\n",
              "      <td>[{\"id\": 470, \"name\": \"spy\"}, {\"id\": 818, \"name...</td>\n",
              "      <td>en</td>\n",
              "      <td>Spectre</td>\n",
              "      <td>A cryptic message from Bond’s past sends him o...</td>\n",
              "      <td>107.376788</td>\n",
              "      <td>[{\"name\": \"Columbia Pictures\", \"id\": 5}, {\"nam...</td>\n",
              "      <td>[{\"iso_3166_1\": \"GB\", \"name\": \"United Kingdom\"...</td>\n",
              "      <td>2015-10-26</td>\n",
              "      <td>880674609</td>\n",
              "      <td>148.0</td>\n",
              "      <td>[{\"iso_639_1\": \"fr\", \"name\": \"Fran\\u00e7ais\"},...</td>\n",
              "      <td>Released</td>\n",
              "      <td>A Plan No One Escapes</td>\n",
              "      <td>Spectre</td>\n",
              "      <td>6.3</td>\n",
              "      <td>4466</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>250000000</td>\n",
              "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 80, \"nam...</td>\n",
              "      <td>http://www.thedarkknightrises.com/</td>\n",
              "      <td>49026</td>\n",
              "      <td>[{\"id\": 849, \"name\": \"dc comics\"}, {\"id\": 853,...</td>\n",
              "      <td>en</td>\n",
              "      <td>The Dark Knight Rises</td>\n",
              "      <td>Following the death of District Attorney Harve...</td>\n",
              "      <td>112.312950</td>\n",
              "      <td>[{\"name\": \"Legendary Pictures\", \"id\": 923}, {\"...</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>2012-07-16</td>\n",
              "      <td>1084939099</td>\n",
              "      <td>165.0</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>Released</td>\n",
              "      <td>The Legend Ends</td>\n",
              "      <td>The Dark Knight Rises</td>\n",
              "      <td>7.6</td>\n",
              "      <td>9106</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>260000000</td>\n",
              "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
              "      <td>http://movies.disney.com/john-carter</td>\n",
              "      <td>49529</td>\n",
              "      <td>[{\"id\": 818, \"name\": \"based on novel\"}, {\"id\":...</td>\n",
              "      <td>en</td>\n",
              "      <td>John Carter</td>\n",
              "      <td>John Carter is a war-weary, former military ca...</td>\n",
              "      <td>43.926995</td>\n",
              "      <td>[{\"name\": \"Walt Disney Pictures\", \"id\": 2}]</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>2012-03-07</td>\n",
              "      <td>284139100</td>\n",
              "      <td>132.0</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>Released</td>\n",
              "      <td>Lost in our world, found in another.</td>\n",
              "      <td>John Carter</td>\n",
              "      <td>6.1</td>\n",
              "      <td>2124</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      budget  ... vote_count\n",
              "0  237000000  ...      11800\n",
              "1  300000000  ...       4500\n",
              "2  245000000  ...       4466\n",
              "3  250000000  ...       9106\n",
              "4  260000000  ...       2124\n",
              "\n",
              "[5 rows x 20 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S6uyuOLH7-1I",
        "colab_type": "code",
        "outputId": "b4198297-ef7b-4410-b084-002cdb337f0b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        }
      },
      "source": [
        "tmdb.original_language.unique() # categoria nominal"
      ],
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['en', 'ja', 'fr', 'zh', 'es', 'de', 'hi', 'ru', 'ko', 'te', 'cn',\n",
              "       'it', 'nl', 'ta', 'sv', 'th', 'da', 'xx', 'hu', 'cs', 'pt', 'is',\n",
              "       'tr', 'nb', 'af', 'pl', 'he', 'ar', 'vi', 'ky', 'id', 'ro', 'fa',\n",
              "       'no', 'sl', 'ps', 'el'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qFciVWhY8Itb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# primeiro grau\n",
        "# segundo grau\n",
        "# terceiro grau\n",
        "# 1 grau < 2 grau < 3 grau  # categorica ordinal"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PNML6XtU_jhe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# budget --> orçamento --> quantitativo continuo"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "siaZiAJ5AJhl",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# quantidade de votos => 1, 2, 3, 4 não têm 2.5 votos\n",
        "# notas do movielens => 0.5, 1, 1.5..."
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "me6q1GF0A6Dq",
        "colab_type": "code",
        "outputId": "88803e9d-c676-4b19-cf9a-c6073b62cee0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 663
        }
      },
      "source": [
        "# comparando categorias\n",
        "# Serie --> Quando você extrai dados de uma única coluna,\n",
        "# ou uma única serie. Diferente de um, Dataframe que são várias colunas\n",
        "\n",
        "tmdb['original_language'].value_counts()"
      ],
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "en    4505\n",
              "fr      70\n",
              "es      32\n",
              "zh      27\n",
              "de      27\n",
              "hi      19\n",
              "ja      16\n",
              "it      14\n",
              "cn      12\n",
              "ko      11\n",
              "ru      11\n",
              "pt       9\n",
              "da       7\n",
              "sv       5\n",
              "nl       4\n",
              "fa       4\n",
              "he       3\n",
              "th       3\n",
              "cs       2\n",
              "id       2\n",
              "ro       2\n",
              "ta       2\n",
              "ar       2\n",
              "te       1\n",
              "is       1\n",
              "ky       1\n",
              "hu       1\n",
              "el       1\n",
              "no       1\n",
              "af       1\n",
              "xx       1\n",
              "pl       1\n",
              "tr       1\n",
              "vi       1\n",
              "nb       1\n",
              "ps       1\n",
              "sl       1\n",
              "Name: original_language, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RXzXxBJxCabg",
        "colab_type": "code",
        "outputId": "282a764f-52d1-46b0-9b6c-30d421d38dcd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "# Retornando os dados como um Dataframe\n",
        "\n",
        "contagem_linguas = tmdb['original_language'].value_counts().to_frame().reset_index()\n",
        "contagem_linguas.columns = ['original_language', 'total']\n",
        "contagem_linguas.head()\n",
        "\n",
        "\n",
        "#tmdb['original_language'].value_counts().to_frame()"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>original_language</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>en</td>\n",
              "      <td>4505</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>fr</td>\n",
              "      <td>70</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>es</td>\n",
              "      <td>32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>zh</td>\n",
              "      <td>27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>de</td>\n",
              "      <td>27</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  original_language  total\n",
              "0                en   4505\n",
              "1                fr     70\n",
              "2                es     32\n",
              "3                zh     27\n",
              "4                de     27"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FW5vXnwZDw3v",
        "colab_type": "code",
        "outputId": "53521f47-29f0-4b65-ee78-6af287f4cfee",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        }
      },
      "source": [
        "import seaborn as sns\n",
        "#sns.barplot(data = contagem_linguas)\n",
        "\n",
        "sns.barplot(x = 'original_language', y = 'total', data = contagem_linguas)"
      ],
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f40d22eea58>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 54
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "58WS8kxzFXHl",
        "colab_type": "code",
        "outputId": "f4d93cb1-0c5b-4420-b40d-3fcfccdce652",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 386
        }
      },
      "source": [
        "sns.catplot(x = 'original_language', kind = 'count', data = tmdb)"
      ],
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x7f40d2165208>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 55
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 360x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YU_B2_tnCIpP",
        "colab_type": "code",
        "outputId": "3f4e5cb6-4c6e-4b2a-d026-411aca97320a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 102
        }
      },
      "source": [
        "\n",
        "tmdb['original_language'].value_counts().index"
      ],
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['en', 'fr', 'es', 'zh', 'de', 'hi', 'ja', 'it', 'cn', 'ko', 'ru', 'pt',\n",
              "       'da', 'sv', 'nl', 'fa', 'he', 'th', 'cs', 'id', 'ro', 'ta', 'ar', 'te',\n",
              "       'is', 'ky', 'hu', 'el', 'no', 'af', 'xx', 'pl', 'tr', 'vi', 'nb', 'ps',\n",
              "       'sl'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "t96h-HzUB2b1",
        "colab_type": "code",
        "outputId": "51fbc2e6-0008-46e9-b11d-04e9610679bd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        }
      },
      "source": [
        "tmdb['original_language'].value_counts().values"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([4505,   70,   32,   27,   27,   19,   16,   14,   12,   11,   11,\n",
              "          9,    7,    5,    4,    4,    3,    3,    2,    2,    2,    2,\n",
              "          2,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,\n",
              "          1,    1,    1,    1])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4vh5Vpu8Hruy",
        "colab_type": "code",
        "outputId": "e510f1e3-0e8d-4161-c108-752463ea8bc9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "plt.pie(contagem_linguas['total'], labels = contagem_linguas['original_language'])"
      ],
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "([<matplotlib.patches.Wedge at 0x7f40cf80ec18>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf81c198>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf81c6a0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf81cba8>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf8280f0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf8285f8>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf828b00>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf828fd0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf833550>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf833a58>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7f9978>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7c2470>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7c2978>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7c2e80>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7cb3c8>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7cb8d0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7cbdd8>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7d7320>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7d7828>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7d7d30>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7e3278>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7e3780>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7e3c88>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7f21d0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7f26d8>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7f2be0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf77c128>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf77c630>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf77cb38>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf787080>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf787588>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf787a90>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf787f98>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7924e0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf7929e8>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf792ef0>,\n",
              "  <matplotlib.patches.Wedge at 0x7f40cf79e438>],\n",
              " [Text(-1.0791697536499925, 0.2130554923183512, 'en'),\n",
              "  Text(1.0355355017029462, -0.3710339940124459, 'fr'),\n",
              "  Text(1.0579676486019882, -0.3011718023181785, 'es'),\n",
              "  Text(1.0687996606645356, -0.26012936274741094, 'zh'),\n",
              "  Text(1.0773191105706255, -0.22222406260195313, 'de'),\n",
              "  Text(1.0835167978583342, -0.18971386021801853, 'hi'),\n",
              "  Text(1.0875756432724297, -0.16486121484618815, 'ja'),\n",
              "  Text(1.0906010773146022, -0.14348968659882622, 'it'),\n",
              "  Text(1.092883487371409, -0.12492270822755745, 'cn'),\n",
              "  Text(1.0946390911069936, -0.10846778425161549, 'ko'),\n",
              "  Text(1.0960865535188649, -0.09270527058984593, 'ru'),\n",
              "  Text(1.0972054830031333, -0.07835896928789601, 'pt'),\n",
              "  Text(1.097965443340663, -0.06687215586282344, 'da'),\n",
              "  Text(1.0984565010300316, -0.05825217030171998, 'sv'),\n",
              "  Text(1.0987803851616647, -0.0517847968421653, 'nl'),\n",
              "  Text(1.0990363161210686, -0.04603450713357274, 'fa'),\n",
              "  Text(1.0992355702663055, -0.04100196411527794, 'he'),\n",
              "  Text(1.0993880184234357, -0.03668766750546649, 'th'),\n",
              "  Text(1.0995021239019234, -0.033091985965784415, 'cs'),\n",
              "  Text(1.099584941078101, -0.03021518416739545, 'id'),\n",
              "  Text(1.0996602312343366, -0.027338175536150495, 'ro'),\n",
              "  Text(1.099727993855245, -0.024460979766119193, 'ta'),\n",
              "  Text(1.0997882284769684, -0.02158361655264929, 'ar'),\n",
              "  Text(1.0998284639438185, -0.01942549610642471, 'te'),\n",
              "  Text(1.0998529348820232, -0.01798670707495573, 'is'),\n",
              "  Text(1.0998755236058106, -0.01654788726224571, 'ky'),\n",
              "  Text(1.0998962300765243, -0.01510903913059323, 'hu'),\n",
              "  Text(1.0999150542587282, -0.013670165142345335, 'el'),\n",
              "  Text(1.0999319961202083, -0.012231267759896247, 'no'),\n",
              "  Text(1.0999470556319713, -0.01079234944567632, 'af'),\n",
              "  Text(1.099960232768245, -0.00935341266215563, 'xx'),\n",
              "  Text(1.0999715275064792, -0.007914459871831963, 'pl'),\n",
              "  Text(1.0999809398273452, -0.006475493537234394, 'tr'),\n",
              "  Text(1.0999884697147349, -0.005036516120911278, 'vi'),\n",
              "  Text(1.0999941171557621, -0.0035975300854338356, 'nb'),\n",
              "  Text(1.0999978821407626, -0.0021585378933851127, 'ps'),\n",
              "  Text(1.0999997646632929, -0.0007195420073586872, 'sl')])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 58
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X343ZSuRJbhx",
        "colab_type": "code",
        "outputId": "c7cb43e1-f342-46b6-c167-25e760743b0f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "total_lingua = tmdb['original_language'].value_counts()\n",
        "total_geral = total_lingua.sum()\n",
        "total_ingles = total_lingua.loc['en']\n",
        "total_resto = total_geral - total_ingles\n",
        "print(total_ingles, total_resto)"
      ],
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "4505 298\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "m_eb1C5gjxJV",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 111
        },
        "outputId": "008e5ad2-a0fa-4b36-b2b4-3b863428c7b2"
      },
      "source": [
        "dados = {\n",
        "    'língua': ['ingles', 'outros'],\n",
        "    'total': [total_ingles, total_resto]\n",
        "}\n",
        "dados = pd.DataFrame(dados)\n",
        "dados\n"
      ],
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>língua</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>ingles</td>\n",
              "      <td>4505</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>outros</td>\n",
              "      <td>298</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   língua  total\n",
              "0  ingles   4505\n",
              "1  outros    298"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3Ijzm56DZSjI",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "11963acf-c815-4ce5-fd8a-62ea7259c52f"
      },
      "source": [
        "sns.barplot(x = 'língua', y = 'total', data = dados)"
      ],
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f40cd7c3d68>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 70
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d5xFSF42aHB6",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 646
        },
        "outputId": "0bb30f73-8ecf-41fa-d5dc-c8e64c068a57"
      },
      "source": [
        "total_lingua_outros_filmes = tmdb.query(\"original_language != 'en'\").original_language.value_counts()\n",
        "total_lingua_outros_filmes"
      ],
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "fr    70\n",
              "es    32\n",
              "zh    27\n",
              "de    27\n",
              "hi    19\n",
              "ja    16\n",
              "it    14\n",
              "cn    12\n",
              "ko    11\n",
              "ru    11\n",
              "pt     9\n",
              "da     7\n",
              "sv     5\n",
              "nl     4\n",
              "fa     4\n",
              "th     3\n",
              "he     3\n",
              "cs     2\n",
              "ar     2\n",
              "ta     2\n",
              "id     2\n",
              "ro     2\n",
              "ps     1\n",
              "nb     1\n",
              "ky     1\n",
              "tr     1\n",
              "xx     1\n",
              "sl     1\n",
              "is     1\n",
              "af     1\n",
              "no     1\n",
              "pl     1\n",
              "el     1\n",
              "hu     1\n",
              "te     1\n",
              "vi     1\n",
              "Name: original_language, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 73
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Efpws-m6ofvd",
        "colab_type": "text"
      },
      "source": [
        "# Revisando o papel da média, mediana de tendência central, dispersão, desvio padrão, boxplot, histograma."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Wc5KsM5FbOmp",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 339
        },
        "outputId": "a0bfbced-1653-473c-fd01-45873b7148ab"
      },
      "source": [
        "filmes_sem_lingua_original_ingles = tmdb.query(\"original_language != 'en'\")\n",
        "\n",
        "sns.catplot(x = 'original_language', kind = 'count', \n",
        "            data = filmes_sem_lingua_original_ingles,\n",
        "            aspect = 2, order = total_lingua_outros_filmes.index,\n",
        "            palette = 'GnBu_d')"
      ],
      "execution_count": 85,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x7f40ccb2bb00>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 85
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x01-P_m5cSti",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 111
        },
        "outputId": "2a42461c-7c1d-4c88-be42-5d546b234f22"
      },
      "source": [
        "filmes.head(2)\n",
        "notas.head(2)"
      ],
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>usuarioId</th>\n",
              "      <th>filmeId</th>\n",
              "      <th>nota</th>\n",
              "      <th>momento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982703</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964981247</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   usuarioId  filmeId  nota    momento\n",
              "0          1        1   4.0  964982703\n",
              "1          1        3   4.0  964981247"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 87
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XHVWI1-ef18t",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "f95c553d-2673-4a6d-ddc0-cd2b53d57854"
      },
      "source": [
        "notas_toy_story = notas.query('filmeId == 1')\n",
        "notas_Jumanji = notas.query('filmeId == 2')\n",
        "print(len(notas_toy_story), len(notas_Jumanji))"
      ],
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "215 110\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cpBvd1Kygq_S",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "cf2503b2-cecc-4f0a-fd60-edb151c7c459"
      },
      "source": [
        "#Média\n",
        "print('Nota média Toy Store %.2f' % notas_toy_story.nota.mean())\n",
        "print('Nota média Jumanji %.2f' % notas_Jumanji.nota.mean())"
      ],
      "execution_count": 100,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Nota média Toy Store 3.92\n",
            "Nota média Jumanji 3.43\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xcpKgh5ChX3g",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "f16a4671-7bf1-402d-eb3a-04b40e1285af"
      },
      "source": [
        "#Mediana\n",
        "print('Nota média Toy Store %.2f' % notas_toy_story.nota.median())\n",
        "print('Nota média Jumanji %.2f' % notas_Jumanji.nota.median())"
      ],
      "execution_count": 101,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Nota média Toy Store 4.00\n",
            "Nota média Jumanji 3.50\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7LV9RknhhiOz",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "9b37bf7b-2985-4112-8e4d-dd211e5ffd61"
      },
      "source": [
        "#Desvio padrão\n",
        "#NumPay --> Trabalha com array's númericas\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))\n",
        "filme2 = np.append(np.array([5] * 10), np.array([1] * 10))\n",
        "\n",
        "print(filme1.mean(), filme2.mean())\n",
        "print(np.median(filme1), np.median(filme2))\n"
      ],
      "execution_count": 114,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3.0 3.0\n",
            "3.0 3.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rC0ez827jnwl",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 316
        },
        "outputId": "209a25af-ae13-4c1b-ad02-5d825d3d539a"
      },
      "source": [
        "plt.hist(filme1)\n",
        "plt.hist(filme2)"
      ],
      "execution_count": 116,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([10.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 10.]),\n",
              " array([1. , 1.4, 1.8, 2.2, 2.6, 3. , 3.4, 3.8, 4.2, 4.6, 5. ]),\n",
              " <a list of 10 Patch objects>)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 116
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zTPvyjqNkRdn",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E1lIBKomkDHE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 520
        },
        "outputId": "e5acb713-51ed-4203-bbc6-a22d69ad2d4e"
      },
      "source": [
        "plt.boxplot([filme1, filme2])"
      ],
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'boxes': [<matplotlib.lines.Line2D at 0x7f40cc66d3c8>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc5f8be0>],\n",
              " 'caps': [<matplotlib.lines.Line2D at 0x7f40cc66ddd8>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc5f8198>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc605630>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc605978>],\n",
              " 'fliers': [<matplotlib.lines.Line2D at 0x7f40cc5f8898>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc60d048>],\n",
              " 'means': [],\n",
              " 'medians': [<matplotlib.lines.Line2D at 0x7f40cc5f8518>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc605cc0>],\n",
              " 'whiskers': [<matplotlib.lines.Line2D at 0x7f40cc66d6d8>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc66da58>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc5f8f60>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cc6052e8>]}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 118
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oAVxv_EAkYF6",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 520
        },
        "outputId": "bac66b29-5cc0-41ef-a8d5-1313c747dce3"
      },
      "source": [
        "plt.boxplot([notas_toy_story.nota, notas_Jumanji.nota])\n",
        "#sns.boxplot(notas_toy_story)\n",
        "#sns.boxplot(notas_Jumanji)\n"
      ],
      "execution_count": 124,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'boxes': [<matplotlib.lines.Line2D at 0x7f40ccc18320>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40ccb682e8>],\n",
              " 'caps': [<matplotlib.lines.Line2D at 0x7f40ccda02e8>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40ccda06a0>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40ccb68fd0>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40ccc4f240>],\n",
              " 'fliers': [<matplotlib.lines.Line2D at 0x7f40ccc113c8>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cccdad68>],\n",
              " 'means': [],\n",
              " 'medians': [<matplotlib.lines.Line2D at 0x7f40ccc2e6a0>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40cccda978>],\n",
              " 'whiskers': [<matplotlib.lines.Line2D at 0x7f40ccc27198>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40ccc27eb8>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40ccb68978>,\n",
              "  <matplotlib.lines.Line2D at 0x7f40ccb68400>]}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 124
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AxPdGPlClit2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        },
        "outputId": "4709f8bb-7ef2-4967-dc11-1de67ba9033a"
      },
      "source": [
        "sns.boxplot(x = 'filmeId', y = 'nota', data = notas.query(\"filmeId in [1, 2]\"))"
      ],
      "execution_count": 127,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f40cc9c12b0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 127
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXgAAAEGCAYAAABvtY4XAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAOvUlEQVR4nO3df2zd1X3G8eeJzYopsAqTMmYwUXsrOg06aG/3x2DTQMnmpduE1GqrtBYjVYr2Q47LNk0r2x9j2pDWqWzBm8Si0tXRum6TALVCwWrSgRAag9opJUDQarEE4bESzK9kSQN2PvvD18SAk16Izz3XH79fkuVr36+/54n56tHh3O/1cUQIAJDPutoBAABlUPAAkBQFDwBJUfAAkBQFDwBJ9dYOsNT5558fGzZsqB0DAFaNqampFyJi/XLPdVXBb9iwQZOTk7VjAMCqYfvAyZ5jiQYAkqLgASApCh4AkqLgASApCh4Akip6F43t/ZIOSZqXNBcRzZLjAQBO6MRtktdExAsdGAcAsERX3QefwdjYmKanp6tmmJmZkSQNDAxUzSFJjUZDIyMjtWNA3XFtSt1zfa6Fa7P0GnxI+pbtKdtbljvA9hbbk7YnDx48WDjO2nD06FEdPXq0dgxgWVyfneOSG37YHoiIGdvvl7RL0khEPHCy45vNZvBO1tM3OjoqSdq2bVvlJMDbcX2uLNtTJ3t9s+gMPiJmWp+fl3S3pJ8tOR4A4IRiBW/7vbbPWXws6ZckPV5qPADAm5V8kfUCSXfbXhznnyNiouB4AIAlihV8RDwt6WdKnR8AcGq8kxUAkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4Akiq54UdHdcuO8d1g8fewuPflWtdoNDQyMlI7BtBxaQp+enpajz6+T/NnnVc7SnXrXlvYSH3q6R9UTlJfz5EXa0cAqklT8JI0f9Z5OvrhzbVjoIv0PbWzdgSgGtbgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASApCh4AkqLgASCp4gVvu8f2d23fU3osAMAJnZjBj0ra14FxAABLFN2T1fZFkj4h6S8l/X7JsWZmZtRz5BX24MSb9ByZ1czMXO0YGhsb0/T0dO0YXWHx9zA6Olo5SXdoNBoaGRkpcu7Sm27/raQ/knTOyQ6wvUXSFkkaHBwsHAeoY3p6Wt9/4rsaPHu+dpTqfuz1hYWDYwcmKyep75nDPUXPX6zgbf+qpOcjYsr2L57suIjYLmm7JDWbzXi34w0MDOh/j/Xq6Ic3v9tTIKG+p3ZqYOCC2jEkSYNnz+umj75aOwa6yC17zi16/pJr8FdJ+nXb+yX9i6Rrbf9TwfEAAEsUK/iI+EJEXBQRGyR9WtK/R8RnSo0HAHgz7oMHgKRKv8gqSYqI+yXd34mxAAALmMEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFId+XvwndJz5EX1PbWzdozq1v1wYd/P42eW3e9xNeg58qKk+nuyzszM6P8O9RTfgxOry4FDPXrvzEyx86cp+EajUTtC15iePiRJanygfrHVdwHXBtasNAU/MjJSO0LXGB0dlSRt27atchIsGhgY0LG553TTR1+tHQVd5JY95+o9AwPFzs8aPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkRcEDQFIUPAAkVazgbZ9p+xHb37P9hO2bS40FAHi7klv2HZN0bUQctn2GpAdt3xsR/1lwTABAS7GCj4iQdLj15Rmtjyg1HtDtnjnco1v2nFs7RnU/OLKwcHDBWccrJ6nvmcM9+lDB8xfddNt2j6QpSQ1Jfx8RDy9zzBZJWyRpcHCwZBygmkajUTtC13htelqS9J5L+J18SGWvjaIFHxHzkq6w/T5Jd9u+LCIef8sx2yVtl6Rms8kMHymNjIzUjtA1RkdHJUnbtm2rnCS/jtxFExEvS7pP0lAnxgMAvIMZvO1PSPppSWcufi8i/vwUx6+X9HpEvGy7T9ImSX91GlkBAO9AWwVv+3ZJZ0m6RtKXJX1K0iM/4sculDTeWodfJ+nfIuKe08gKAHgH2p3B/1xEfMT2YxFxs+0vSbr3VD8QEY9JuvK0EwIA3pV21+CPtj4fsf2Tkl7XwgwdANCl2p3B39O6E+avJe3Rwv3sXy6WCgBw2tot+C9GxDFJd9q+RwsvtP6wXCwAwOlqd4nmocUHEXEsIl5Z+j0AQPc55Qze9k9IGpDUZ/tKSW49da4W7qoBAHSpH7VE88uSbpB0kaRbl3z/kKSbCmUCAKyAUxZ8RIxr4V72T0bEnR3KBABYAe2uwX/b9q22J1sfX7L940WTAQBOS7sFf4cWlmV+o/XxqqR/LBUKAHD62r1N8oMR8cklX99s+9ESgQAAK6Ptd7LavnrxC9tX6cS7WwEAXajdGfzvaOHF1sV195ckDZeJBABYCe0W/D5JX5T0QUnvk/SKpOskPVYoFwDgNLVb8N+Q9LIW/g7NTLk4AICV0m7BXxQR7MYEAKtIuy+y/ofty4smAQCsqHZn8FdLusH2f0s6poW/SRMR8ZFiyQAAp6Xdgv+VoikAACuurYKPiAOlgwAAVla7a/AAgFWGggeApCh4AEiKggeApCh4AEiKggeApCh4AEiKggeApCh4AEiKggeApCh4AEiKggeApCh4AEiKggeApCh4AEiKggeApIoVvO2Lbd9n+0nbT9geLTUWAODt2t2y792Yk/QHEbHH9jmSpmzviognC44JAGgpVvAR8Zyk51qPD9neJ2lAUuqCHxsb0/T0dNUMi+OPjtb/n6ZGo6GRkZHaMYA1qeQM/g22N0i6UtLDyzy3RdIWSRocHOxEnPT6+vpqRwDQBYoXvO2zJd0p6fMR8epbn4+I7ZK2S1Kz2YzSeUpjtgqgWxS9i8b2GVoo969FxF0lxwIAvFnJu2gs6Q5J+yLi1lLjAACWV3IGf5Wkz0q61vajrY/NBccDACxR8i6aByW51PkBAKfGO1kBICkKHgCSouABICkKHgCSouABICkKHgCSouABICkKHgCSouABICkKHgCSouABICkKHgCSouATmp2d1datWzU7O1s7CoCKKPiExsfHtXfvXu3YsaN2FAAVUfDJzM7OamJiQhGhiYkJZvHAGtaRTbfROePj4zp+/LgkaX5+Xjt27NCNN95YORW6wdjYmKanp2vHeCPD6Oho1RyNRiP9HsrM4JPZvXu35ubmJElzc3PatWtX5UTAm/X19amvr692jDWBGXwyGzdu1M6dOzU3N6fe3l5t2rSpdiR0ieyzVbwdM/hkhoeHtW7dwn/Wnp4eXX/99ZUTAaiFgk+mv79fQ0NDsq2hoSH19/fXjgSgEpZoEhoeHtb+/fuZvQNrHAWfUH9/v2677bbaMQBUxhINACRFwQNAUhQ8ACRFwQNAUhQ8ACRFwQNAUhQ8ACRFwQNAUhQ8ACRFwQNAUhQ8ACRFwQNAUhQ8gI6anZ3V1q1b2S+4A4oVvO2v2H7e9uOlxgCw+oyPj2vv3r3asWNH7SjplZzBf1XSUMHzA1hlZmdnNTExoYjQxMQEs/jCihV8RDwg6cVS5wew+oyPj+v48eOSpPn5eWbxhVVfg7e9xfak7cmDBw/WjgOgoN27d2tubk6SNDc3p127dlVOlFv1go+I7RHRjIjm+vXra8cBUNDGjRvV27uwkVxvb682bdpUOVFu1QsewNoxPDysdesWaqenp4d9gwuj4AF0TH9/v4aGhmRbQ0ND6u/vrx0ptZK3SX5d0kOSLrX9rO3PlRoLwOoxPDysyy+/nNl7Bzgiamd4Q7PZjMnJydoxAGDVsD0VEc3lnmOJBgCSouABICkKHgCSouABICkKHgCSouABICkKHgCSouABICkKHgCSouABICkKHgCSouABICkKPiF2rUc34/rsHAo+IXatRzfj+uwcCj4Zdq1HN+P67CwKPhl2rUc34/rsLAo+GXatRzfj+uwsCj4Zdq1HN+P67CwKPhl2rUc34/rsLAo+GXatRzfj+uys3toBsPKGh4e1f/9+ZkfoSlyfneOIqJ3hDc1mMyYnJ2vHAIBVw/ZURDSXe44lGgBIioIHgKQoeABIioIHgKS66kVW2wclHaidI4nzJb1QOwRwElyfK+eSiFi/3BNdVfBYObYnT/bKOlAb12dnsEQDAElR8ACQFAWf1/baAYBT4PrsANbgASApZvAAkBQFDwBJUfDJ2P6K7edtP147C7CU7Ytt32f7SdtP2B6tnSk71uCTsf0Lkg5L2hERl9XOAyyyfaGkCyNij+1zJE1Jui4inqwcLS1m8MlExAOSXqydA3iriHguIva0Hh+StE/SQN1UuVHwADrO9gZJV0p6uG6S3Ch4AB1l+2xJd0r6fES8WjtPZhQ8gI6xfYYWyv1rEXFX7TzZUfAAOsK2Jd0haV9E3Fo7z1pAwSdj++uSHpJ0qe1nbX+udiag5SpJn5V0re1HWx+ba4fKjNskASApZvAAkBQFDwBJUfAAkBQFDwBJUfAAkBQFjzXB9lbb+2y/ZPuPW9/7M9t/uELn32/7/GW+v2JjAO9Ub+0AQIf8rqSNEfFs7SBApzCDR3q2b5f0AUn32r7R9t8tc8z9tv/G9mRrpv9x23fZ/r7tv1hy3GdsP9J6k84/2O5Z5lx/Yvu/bD8o6dKi/zjgFCh4pBcRvy3pfyRdI+mlUxz6WkQ0Jd0u6RuSfk/SZZJusN1v+6ck/aakqyLiCknzkn5r6Qlsf0zSpyVdIWmzpI+v8D8HaBtLNMAJ32x93ivpiYh4TpJsPy3pYklXS/qYpO8s/FkV9Ul6/i3n+HlJd0fEkdbPflNAJRQ8cMKx1ufjSx4vft0ryZLGI+ILnQ4GvBss0QDt+7akT9l+vyTZPs/2JW855gFJ19nua21L92udDgksYgYPtCkinrT9p5K+ZXudpNe1sE5/YMkxe2z/q6TvaWH55jtVwgLir0kCQFos0QBAUhQ8ACRFwQNAUhQ8ACRFwQNAUhQ8ACRFwQNAUv8Pfc62syk6fi8AAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i3zKXidJhAcu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "62812a88-a481-46f1-cfd7-65a6fb1cf325"
      },
      "source": [
        "#Desvio Padrão --> pandas.DataFrame.std\n",
        "print(notas_toy_story.nota.std(), notas_Jumanji.nota.std())"
      ],
      "execution_count": 128,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.8348591407114045 0.8817134921476455\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oTjh__dnnyR1",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Usamos a média, mediana e o desvio padrão para entender e analisar,\n",
        "# um padrão, a desperção e a distribuição de como os dados se comportam"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1Vyho_xtnhlG",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Desvio Padrão --> numpy.std\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lJrOn1PKpAiW",
        "colab_type": "text"
      },
      "source": [
        "#Sites para baixar e trabalhar com dados --> Kagle, google dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gvm4sJakpJ_4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#A medida que exploramos os dados, fazemos os dados estáticos,\n",
        "#entender como os dados influênciam para fazer previsão futuras."
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}