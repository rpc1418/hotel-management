# Versatile Hotel Management System

![GitHub repo size](https://img.shields.io/github/repo-size/rpc1418/hotel-management) ![License](https://img.shields.io/github/license/rpc1418/hotel-management) ![Contributors](https://img.shields.io/github/contributors/rpc1418/hotel-management)

Versatile is a hotel management system built in Python that allows users to book rooms, manage customer records, and view room information. It utilizes `Pandas` for data management, `SQLAlchemy` for ORM, and `MySQL` for database storage.

## Features

- **Booking System:** Handles room booking, check-in, and check-out process, and allocates room numbers.
- **Customer Record:** Stores customer details such as name, phone number, address, check-in/check-out date, and room type.
- **Room Information:** Displays detailed information about different room types.
- **Database Integration:** Customer records are stored in a MySQL database for easy retrieval.
- **Random Room & Customer ID Generation:** Automatically generates room numbers and customer IDs for new bookings.

## Prerequisites

- Python 3.x
- MySQL Database
- Required Python packages:
  - `pandas`
  - `pymysql`
  - `sqlalchemy`
  - `mysql-connector-python`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/versatile-hotel-management.git
    cd versatile-hotel-management
    ```

2. **Install the required dependencies:**

    ```bash
    pip install pandas pymysql sqlalchemy mysql-connector-python
    ```

3. **Setup your MySQL database. Create a database named `versatile` and adjust the MySQL credentials in the code:**

    ```sql
    CREATE DATABASE versatile;
    ```

4. **Create a table named `booking` for storing the booking information:**

    ```sql
    CREATE TABLE booking (
        name VARCHAR(100),
        phno VARCHAR(15),
        address TEXT,
        checkin DATE,
        checkout DATE,
        prices INT,
        room_no INT,
        cust_id INT
    );
    ```

5. **Start the application by running the `main.py` script:**

    ```bash
    python main.py
    ```

## Folder Structure

```plaintext
versatile-hotel-management/
├── main.py          # Main driver code for the hotel management system
├── requirements.txt # Contains required Python packages
└── README.md        # Project documentation
```

## Database Integration

The project uses MySQL as a backend database. The MySQL connection is established using the `mysql-connector-python` library, and data is inserted or retrieved using `Pandas` for simplicity.

Ensure that your MySQL server is running, and the required table is set up in the database.

## Usage

Run the program and select one of the options in the menu:

- **Booking**: Allows customers to book a room.
- **Rooms Info**: Displays available room types and their amenities.
- **Record**: Displays the customer records stored in the database.
- **Customer Info**: Retrieves specific customer information based on phone number.
- **Exit**: Exits the program.

For booking, the program checks for valid check-in/check-out dates, ensures the room is available, and generates a unique room number and customer ID.

The customer records can be viewed, and specific customer data can be retrieved using their phone number.

## Database Connection

The connection to MySQL is handled using the `sqlalchemy.create_engine()` method in the booking function:

```python
engine = create_engine("mysql+pymysql://root:root123@localhost/versatile")
conn = engine.connect()
```

## Database Connection

Adjust the connection string to match your database credentials. 

Example:

```python
engine = create_engine("mysql+pymysql://<username>:<password>@<host>/<database>")
conn = engine.connect()
```

## Screenshots

### Menu

```text
WELCOME TO VERSATILE

1 Booking
2 Rooms Info
3 Record
4 Customer Info
0 Exit
```
### Booking Process
```text
BOOKING ROOMS

Name: John Doe
Phone No.: 1234567890
Address: 123 Main St.
Check-In: 12/12/2023
Check-Out: 14/12/2023
----SELECT ROOM TYPE----
1. Standard Non-AC
2. Standard AC
3. 3-Bed Non-AC
4. 3-Bed AC
Press 0 for Room Prices
Room No. - 301
Customer Id - 15

```
## 📜 License

This project is licensed under the MIT License.

## 🔗 Visit My GitHub:

Explore the code and my other projects here: [GitHub - rpc1418](https://github.com/rpc1418)


Check out my portfolio website: [Rudraksh Chourey's Portfolio](https://rpc1418.github.io/portfolio/)
