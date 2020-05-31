# Supermarket-Optimization

Better placement of items is the key driver for increased sales in supermarkets. To achieve that, the buyer transaction data has to analyze to understand buyer's preference.

The goal of this application is to identify frequent itemsets of size 3 or more that appears at least 0.016% of all transactions in the provided database

## Getting Started

The below instructions will get you a copy of the project up and running on your local machine

### Prerequisites

Python3 should be installed as the minimum requirement. 

Python3 can be installed using Homebrew
```
brew update

brew install python3
```

### Installation


Clone the repo

```
git clone https://github.com/meghanareddyy/Supermarket-Optimization.git
```

open Supermarket-Optimization folder

```
cd Supermarket-Optimization
```

create a python3 virtual environment

```
pip install virtualenv
```
```
virtualenv env --python=python3
```
```
.env/bin/activate
```

install dependencies from requirements.txt

```
pip install -r requirements.txt
```

Now the project is ready to be run.

## Running the Application

Run the application using the below command

```
python3 main.py
```
The above command takes the [retail_25k.dat](retail_25k.dat) file as input.

To run the application with a different dat file, Run

```
python3 main.py <filepath>
```

the extracted output will be in the executed folder named as [frequently_purchased_items.csv](frequently_purchased_items.csv)


## Contact

**Meghana Reddy** - meghana.kotrakona@gmail.com

Project Link: [https://github.com/meghanareddyy/Supermarket-Optimization](https://github.com/meghanareddyy/Supermarket-Optimization)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

