# ReadWriteContracts
read write for a multitude of networks
Smart Contract ReadWriter

Smart Contract ReadWriter is a powerful tool designed to interact with smart contracts easily and efficiently. By providing a contract address, the application scans an array of RPCs to locate all contracts deployed under the given address. It then generates a functions sheet using the contract's ABI, allowing users with any level of authorization to interact with the contract seamlessly.
![Screenshot from 2023-03-29 18-33-14](https://user-images.githubusercontent.com/57512254/228692417-a1135273-f6be-4719-a4da-6b6d8e1e4802.png)

Features:

Scans an array of RPCs to find all contracts deployed under a specific address.
Generates a functions sheet from the contract's ABI.
Allows users with any level of authorization to interact with the smart contract.
How to Use:

Input the contract address you wish to interact with.
The application will scan an array of RPCs and locate all contracts deployed under the given address.
A functions sheet will be generated using the contract's ABI, allowing you to interact with the contract.
Requirements:

Python 3.7 or higher
PySimpleGUI
Web3.py
Dependencies:

hexbytes
os
datetime
webbrowser
json
Installation:

To install Smart Contract ReadWriter, follow these steps:

Clone the repository or download the source code.
Install the required dependencies using pip:
Copy code
pip install -r requirements.txt
Run the main script:
css
Copy code
python main.py
Now you can interact with your smart contracts quickly and easily using the Smart Contract ReadWriter!
